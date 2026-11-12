/* Runs the code of ".. python::" snippets in the browser using Pyodide.
   Pyodide is loaded lazily from the CDN on the first click on a run button. */
(function () {
  "use strict";

  var PYODIDE_BASE_URL = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
  var pyodidePromise = null;

  function getPyodide() {
    if (!pyodidePromise) {
      pyodidePromise = new Promise(function (resolve, reject) {
        var script = document.createElement("script");
        script.src = PYODIDE_BASE_URL + "pyodide.js";
        script.onload = function () {
          // window.loadPyodide is defined by the CDN script loaded above
          window.loadPyodide({ indexURL: PYODIDE_BASE_URL }).then(resolve, reject);
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
        return pyodide.runPythonAsync(code);
      })
      .catch(function (err) {
        output.classList.add("is-error");
        output.textContent = String(err && err.message ? err.message : err);
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
