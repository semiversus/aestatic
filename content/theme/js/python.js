/* Runs the code of ".. python::" snippets in the browser using Pyodide.
   The code is edited with a CodeMirror editor; Pyodide is loaded lazily from
   the CDN on the first click on a run button. input() is served by an in-page
   input field (not a blocking window.prompt dialog), so print output stays
   visible while waiting for input. */
(function () {
  "use strict";

  // the CodeMirror 6 bundle and the Pyodide runtime are built by aestatic
  // (BundleTask) and served next to this file
  var SCRIPT_SRC = (document.currentScript && document.currentScript.src) || "";
  var CM_BUNDLE_URL = SCRIPT_SRC.replace(/python\.js$/, "codemirror.bundle.js");
  var PYODIDE_LOCAL_URL = SCRIPT_SRC.replace(/\/js\/python\.js$/, "/pyodide/");
  var PYODIDE_CDN_URL = "https://cdn.jsdelivr.net/pyodide/v314.0.7/full/";
  var pyodidePromise = null;
  var codeMirrorPromise = null;

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = src;
      script.onload = resolve;
      script.onerror = function () {
        reject(new Error("Could not load " + src));
      };
      document.head.appendChild(script);
    });
  }

  // loads the locally bundled CodeMirror 6 (window.AestaticCM)
  function loadCodeMirror() {
    if (!codeMirrorPromise) {
      codeMirrorPromise = loadScript(CM_BUNDLE_URL)
        .then(function () {
          if (!window.AestaticCM) {
            throw new Error("CodeMirror bundle did not expose window.AestaticCM");
          }
          return window.AestaticCM;
        })
        .catch(function (err) {
          codeMirrorPromise = null;
          throw err;
        });
    }
    return codeMirrorPromise;
  }

  // shows an inline input field inside the given snippet container and
  // resolves with the entered text (Enter) or null (Escape)
  function askInPage(promptText, container) {
    return new Promise(function (resolve) {
      var row = document.createElement("div");
      row.className = "python-input";
      var label = document.createElement("span");
      label.className = "python-input-prompt";
      label.textContent = promptText;
      var input = document.createElement("input");
      input.className = "input is-small";
      input.type = "text";
      row.appendChild(label);
      row.appendChild(input);
      container.appendChild(row); // input field goes below the output
      input.focus();
      var done = false;
      function finish(value) {
        if (done) return;
        done = true;
        row.remove();
        resolve(value);
      }
      input.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          finish(input.value);
        } else if (e.key === "Escape") {
          e.preventDefault();
          finish(null);
        }
      });
    });
  }

  // installed into the Pyodide session once it is loaded
  var SETUP_CODE = [
    "import ast",
    "import builtins",
    "import sys",
    "from js import window",
    "",
    "try:",
    "    sys.stdout.reconfigure(line_buffering=True)",
    "    sys.stderr.reconfigure(line_buffering=True)",
    "except Exception:",
    "    pass",
    "",
    "async def _pyodide_input(prompt=''):",
    "    # __ask is set per run by the JS runner and resolves with the",
    "    # text entered into the in-page input field (None on Escape)",
    "    result = await __ask(str(prompt))",
    "    if result is None:",
    "        raise EOFError",
    "    return result",
    "",
    "def _sync_input(prompt=''):",
    "    # fallback for input() calls the AST rewrite cannot handle",
    "    result = window.prompt(str(prompt))",
    "    if result is None:",
    "        raise EOFError",
    "    return result",
    "",
    "builtins.input = _sync_input",
    "",
    "class _InputRewriter(ast.NodeTransformer):",
    "    def __init__(self):",
    "        self.async_names = set()",
    "        self.wrapped = set()",
    "",
    "    def visit_Call(self, node):",
    "        self.generic_visit(node)",
    "        if isinstance(node.func, ast.Name):",
    "            if node.func.id == 'input':",
    "                return ast.copy_location(ast.Await(value=ast.Call(",
    "                    func=ast.Name(id='_pyodide_input', ctx=ast.Load()),",
    "                    args=node.args, keywords=node.keywords)), node)",
    "            if node.func.id in self.async_names and id(node) not in self.wrapped:",
    "                self.wrapped.add(id(node))",
    "                return ast.copy_location(ast.Await(value=node), node)",
    "        return node",
    "",
    "    def visit_FunctionDef(self, node):",
    "        self.generic_visit(node)",
    "        if not isinstance(node, ast.AsyncFunctionDef) and any(",
    "            isinstance(n, ast.Await) for n in ast.walk(node)",
    "        ):",
    "            self.async_names.add(node.name)",
    "            node.__class__ = ast.AsyncFunctionDef",
    "        return node",
    "",
    "    def visit_Lambda(self, node):",
    "        return node  # input() inside a lambda stays on the sync fallback",
    "",
    "def _prepare(code):",
    "    # rewrite input(...) to await _pyodide_input(...) so that the event",
    "    # loop keeps running (and print output stays visible) while waiting",
    "    tree = ast.parse(code)",
    "    rewriter = _InputRewriter()",
    "    for _ in range(50):",
    "        before = ast.dump(tree)",
    "        tree = rewriter.visit(tree)",
    "        ast.fix_missing_locations(tree)",
    "        if ast.dump(tree) == before:",
    "            break",
    "    return ast.unparse(tree)",
  ].join("\n");

  function loadPyodideFrom(baseUrl) {
    return new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = baseUrl + "pyodide.js";
      script.onload = function () {
        // window.loadPyodide is defined by the script loaded above
        window.loadPyodide({ indexURL: baseUrl }).then(resolve, reject);
      };
      script.onerror = function () {
        reject(new Error("Could not load Pyodide from " + script.src));
      };
      document.head.appendChild(script);
    });
  }

  function getPyodide() {
    if (!pyodidePromise) {
      pyodidePromise = loadPyodideFrom(PYODIDE_LOCAL_URL)
        .catch(function () {
          // fall back to the CDN if the local runtime is missing
          return loadPyodideFrom(PYODIDE_CDN_URL);
        })
        .then(function (pyodide) {
          pyodide.runPython(SETUP_CODE);
          return pyodide;
        })
        .catch(function (err) {
          pyodidePromise = null;
          throw err;
        });
    }
    return pyodidePromise;
  }

  function runSnippet(container) {
    var button = container.querySelector(".python-run");
    var editor = container._cmEditor;
    var code = editor
      ? editor.getValue()
      : container.querySelector("textarea.python-code").value;
    var output = container.querySelector(".python-output");

    button.disabled = true;
    output.hidden = false;
    output.classList.remove("is-error");
    output.textContent = container.dataset.loading || "Loading Python ...";

    getPyodide()
      .then(function (pyodide) {
        output.textContent = "";
        pyodide.setStdout({
          batched: function (line) {
            output.textContent += line + "\n";
          },
        });
        pyodide.setStderr({
          batched: function (line) {
            output.textContent += line + "\n";
          },
        });
        pyodide.globals.set("__ask", function (promptText) {
          return askInPage(promptText, container);
        });
        pyodide.globals.set("__snippet_code", code);
        var prepared = pyodide.runPython("_prepare(__snippet_code)");
        return pyodide.runPythonAsync(prepared);
      })
      .catch(function (err) {
        output.classList.add("is-error");
        output.textContent += String(err && err.message ? err.message : err);
      })
      .finally(function () {
        button.disabled = false;
      });
  }

  // blocks copy/cut/paste when the selection or the event target is inside
  // a snippet, so browser-provided clipboard actions (context menu, Ctrl+C/V)
  // cannot be used on the editor content either
  function selectionInSnippet() {
    var sel = window.getSelection();
    var node = sel && (sel.anchorNode || sel.focusNode);
    if (node && node.nodeType === Node.TEXT_NODE) node = node.parentNode;
    return !!(node && node.closest && node.closest(".python-snippet"));
  }

  function blockClipboardEvent(e) {
    var target = e.target;
    if (
      selectionInSnippet() ||
      (target && target.closest && target.closest(".python-snippet"))
    ) {
      e.preventDefault();
    }
  }

  function init() {
    ["copy", "cut", "paste"].forEach(function (type) {
      document.addEventListener(type, blockClipboardEvent);
    });

    var snippets = document.querySelectorAll(".python-snippet");

    snippets.forEach(function (container) {
      container.querySelector(".python-run").addEventListener("click", function () {
        runSnippet(container);
      });
    });

    if (snippets.length > 0) {
      loadCodeMirror()
        .then(function (CM) {
          // no clipboard interaction (copy/cut/paste) inside the editor
          function blockClipboard(event) {
            event.preventDefault();
            return true;
          }
          document
            .querySelectorAll(".python-snippet textarea.python-code")
            .forEach(function (textarea) {
              var container = textarea.closest(".python-snippet");
              var view = new CM.EditorView({
                doc: textarea.value,
                extensions: [
                  CM.basicSetup,
                  CM.python(),
                  CM.EditorView.lineWrapping,
                  CM.EditorView.domEventHandlers({
                    copy: blockClipboard,
                    cut: blockClipboard,
                    paste: blockClipboard,
                  }),
                ],
              });
              textarea.replaceWith(view.dom);
              container._cmView = view;
              container._cmEditor = {
                getValue: function () {
                  return view.state.doc.toString();
                },
              };
            });
        })
        .catch(function (err) {
          // editor stays a plain textarea, snippets remain runnable
          console.error(err);
        });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
