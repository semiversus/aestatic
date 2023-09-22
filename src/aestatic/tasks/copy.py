import shutil
from typing import MutableSet
from pathlib import Path

from aestatic.processor import BaseTask


class CopyTask(BaseTask):
    def select_files(self, files: MutableSet[Path]) -> MutableSet[Path]:
        return set(f for f in files if f.suffix != ".md" and f.is_file())

    def process(self, files, processor):
        for file in files:
            output_path = "output" / file.relative_to("content")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(file, output_path)
