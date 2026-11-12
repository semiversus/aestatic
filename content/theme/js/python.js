/* Runs the code of ".. python::" snippets in the browser using Pyodide.
   Pyodide is loaded lazily from the CDN on the first click on a run button.
   input() is served by an in-page input field (not a blocking window.prompt
   dialog), so print output stays visible while waiting for input. */
(function () {
  "use strict";

  var PYODIDE_BASE_URL = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
  var pyodidePromise = null;

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

  function getPyodide() {
    if (!pyodidePromise) {
      pyodidePromise = new Promise(function (resolve, reject) {
        var script = document.createElement("script");
        script.src = PYODIDE_BASE_URL + "pyodide.js";
        script.onload = function () {
          // window.loadPyodide is defined by the CDN script loaded above
          window.loadPyodide({ indexURL: PYODIDE_BASE_URL }).then(function (pyodide) {
            pyodide.runPython(SETUP_CODE);
            resolve(pyodide);
          }, reject);
        };
        script.onerror = function () {
          pyodidePromise = null;
          reject(new Error("Could not load Pyodide from " + script.src));
        };
        document.head.appendChild(script);
      });
    }
    return pyodidePromise;
  }

  function runSnippet(container) {
    var button = container.querySelector(".python-run");
    var code = container.querySelector(".python-code code").textContent;
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

  function init() {
    document
      .querySelectorAll(".python-snippet .python-run")
      .forEach(function (button) {
        button.addEventListener("click", function () {
          runSnippet(button.closest(".python-snippet"));
        });
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
