import tarfile
import urllib.request
from pathlib import Path

from aestatic.processor import Processor, BaseTask

BUILD_DIR = Path("build/pyodide")
OUTPUT_DIR = Path("output/theme/pyodide")

PYODIDE_VERSION = "0.26.4"
ARCHIVE_URL = (
    "https://github.com/pyodide/pyodide/releases/download/"
    f"{PYODIDE_VERSION}/pyodide-core-{PYODIDE_VERSION}.tar.bz2"
)
KEEP_FILES = [
    "pyodide.js",
    "pyodide.asm.js",
    "pyodide.asm.wasm",
    "python_stdlib.zip",
    "pyodide-lock.json",
]


class PyodideTask(BaseTask):
    """Downloads the Pyodide core runtime (cached in build/pyodide/.cache)
    and extracts the needed files into output/theme/pyodide/, so the
    website serves the python runtime locally."""

    def select_files(self, files):
        # driven by the build folder, not by content files
        return {BUILD_DIR}

    def process(self, files, processor: Processor):
        cache = BUILD_DIR / ".cache" / Path(ARCHIVE_URL).name
        if not cache.is_file():
            cache.parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(ARCHIVE_URL, cache)
        out_dir = OUTPUT_DIR.resolve()
        out_dir.mkdir(parents=True, exist_ok=True)
        with tarfile.open(cache, "r:*") as tar:
            for member in tar.getmembers():
                if member.isfile() and Path(member.name).name in KEEP_FILES:
                    (out_dir / Path(member.name).name).write_bytes(
                        tar.extractfile(member).read()
                    )
