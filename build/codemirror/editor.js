import { EditorView, basicSetup } from "codemirror";
import { python } from "@codemirror/lang-python";

// exposed as a global so that theme/js/python.js can build the editors
window.AestaticCM = { EditorView, basicSetup, python };
