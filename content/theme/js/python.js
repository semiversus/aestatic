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

  // edited code is kept in localStorage, keyed by page URL and the
  // snippet's position on the page, so changes survive a page reload
  var STORAGE_PREFIX = "aestatic:python:";

  function storageKey(container, index) {
    return STORAGE_PREFIX + window.location.pathname + ":" + index;
  }

  function loadSavedCode(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (err) {
      return null;
    }
  }

  function saveCode(key, code) {
    try {
      window.localStorage.setItem(key, code);
    } catch (err) {
      // storage full or unavailable: editing still works, just not persisted
    }
  }

  function removeSavedCode(key) {
    try {
      window.localStorage.removeItem(key);
    } catch (err) {
      // ignore
    }
  }

  function currentCode(container) {
    var editor = container._cmEditor;
    if (editor) return editor.getValue();
    var textarea = container.querySelector("textarea.python-code");
    return textarea ? textarea.value : "";
  }

  function setCode(container, code) {
    if (container._cmView) {
      container._cmView.dispatch({
        changes: {
          from: 0,
          to: container._cmView.state.doc.length,
          insert: code,
        },
      });
    } else {
      var textarea = container.querySelector("textarea.python-code");
      if (textarea) textarea.value = code;
    }
  }

  // shows the reset button and persists the code as soon as it differs
  // from the original snippet; hides the button and drops the stored
  // code when the content is back to the original state
  function updateResetState(container) {
    var code = currentCode(container);
    var changed = code !== container._originalCode;
    var button = container.querySelector(".python-reset");
    if (button) button.hidden = !changed;
    if (changed) {
      saveCode(container._storageKey, code);
    } else {
      removeSavedCode(container._storageKey);
    }
  }

  // absolute URL of the site root, derived from this script's own URL
  // (document.currentScript.src is always resolved to an absolute URL)
  var ROOT_URL = SCRIPT_SRC
    ? SCRIPT_SRC.replace(/theme\/js\/python\.js$/, "")
    : window.location.origin + "/";

  function bytesToBase64Url(bytes) {
    var bin = "";
    for (var i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
    return btoa(bin)
      .replace(/\+/g, "-")
      .replace(/\//g, "_")
      .replace(/=+$/, "");
  }

  function base64UrlToBytes(b64) {
    b64 = b64.replace(/-/g, "+").replace(/_/g, "/");
    while (b64.length % 4 !== 0) b64 += "=";
    var bin = atob(b64);
    var bytes = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    return bytes;
  }

  // compresses with gzip (if supported) and base64url-encodes the result,
  // so it can be used as a GET parameter
  async function encodeCode(code) {
    var bytes = new TextEncoder().encode(code);
    if (typeof CompressionStream !== "undefined") {
      var compressed = new Blob([bytes])
        .stream()
        .pipeThrough(new CompressionStream("gzip"));
      bytes = new Uint8Array(await new Response(compressed).arrayBuffer());
    }
    return bytesToBase64Url(bytes);
  }

  // inverse of encodeCode; falls back to plain base64 (no compression)
  // when the data is not gzip-compressed
  async function decodeCode(param) {
    var bytes = base64UrlToBytes(param);
    if (typeof DecompressionStream !== "undefined") {
      try {
        var plain = new Blob([bytes])
          .stream()
          .pipeThrough(new DecompressionStream("gzip"));
        return await new Response(plain).text();
      } catch (err) {
        // not gzip-compressed, decode as plain base64 below
      }
    }
    return new TextDecoder().decode(bytes);
  }

  function flashButton(button) {
    if (!button || !button.dataset.copied) return;
    var original = button.textContent;
    button.textContent = button.dataset.copied;
    button.disabled = true;
    setTimeout(function () {
      button.textContent = original;
      button.disabled = false;
    }, 1500);
  }

  function copyToClipboard(text, button) {
    var clipboard = window.navigator && window.navigator.clipboard;
    if (clipboard && clipboard.writeText) {
      clipboard.writeText(text).then(
        function () {
          flashButton(button);
        },
        function () {
          window.prompt(text, text);
        }
      );
    } else {
      window.prompt(text, text);
    }
  }

  // builds a python.html URL containing the current code and copies it
  function shareSnippet(container, button) {
    encodeCode(currentCode(container))
      .then(function (encoded) {
        copyToClipboard(ROOT_URL + "python.html?code=" + encoded, button);
      })
      .catch(function (err) {
        console.error(err);
      });
  }

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

    snippets.forEach(function (container, index) {
      var textarea = container.querySelector("textarea.python-code");
      container._originalCode = textarea ? textarea.value : "";
      container._storageKey = storageKey(container, index);

      // restore the persisted edit (if any) before the editor is created
      var saved = loadSavedCode(container._storageKey);
      if (saved !== null && saved !== container._originalCode && textarea) {
        textarea.value = saved;
      }

      container.querySelector(".python-run").addEventListener("click", function () {
        runSnippet(container);
      });

      var resetButton = container.querySelector(".python-reset");
      if (resetButton) {
        resetButton.addEventListener("click", function () {
          setCode(container, container._originalCode);
          // setCode does not fire an "input" event on a plain textarea
          updateResetState(container);
          if (container._cmView) container._cmView.focus();
        });
      }

      var shareButton = container.querySelector(".python-share");
      if (shareButton) {
        shareButton.addEventListener("click", function () {
          shareSnippet(container, shareButton);
        });
      }

      // fallback path while CodeMirror is not (yet) available
      if (textarea) {
        textarea.addEventListener("input", function () {
          updateResetState(container);
        });
      }

      // reflect a restored edit (button visibility) also without CodeMirror
      updateResetState(container);
    });

    // a shared snippet (?code=... in the URL, see shareSnippet) is loaded
    // into the first snippet of the page, overriding any stored edit
    var sharedParam = new URLSearchParams(window.location.search).get("code");
    if (sharedParam && snippets.length > 0) {
      decodeCode(sharedParam)
        .then(function (code) {
          if (!code) return;
          var container = snippets[0];
          setCode(container, code);
          updateResetState(container);
        })
        .catch(function (err) {
          console.error(err);
        });
    }

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
                  CM.EditorView.updateListener.of(function (update) {
                    if (update.docChanged) updateResetState(container);
                  }),
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
