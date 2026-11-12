import subprocess
from pathlib import Path

from aestatic.processor import Processor, BaseTask

BUILD_DIR = Path("build/codemirror")
OUTPUT_FILE = Path("output/theme/js/codemirror.bundle.js")


class CodeMirrorTask(BaseTask):
    """Bundles CodeMirror 6 (build/codemirror/editor.js, pinned in its
    package.json) with esbuild into output/theme/js/codemirror.bundle.js,
    so the website serves the editor locally. Silent unless it fails."""

    quiet = True

    def select_files(self, files):
        # driven by the build folder, not by content files
        return {BUILD_DIR}

    def process(self, files, processor: Processor):
        if not (BUILD_DIR / "node_modules").is_dir():
            self._run(["npm", "ci"])
        out_path = OUTPUT_FILE.resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        self._run(
            [
                "npx",
                "esbuild",
                "editor.js",
                "--bundle",
                "--minify",
                "--format=iife",
                f"--outfile={out_path}",
            ]
        )

    def _run(self, cmd):
        result = subprocess.run(cmd, cwd=BUILD_DIR, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(
                f'command failed: {" ".join(cmd)}\n{result.stdout}{result.stderr}'
            )
