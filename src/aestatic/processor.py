from typing import Dict, List, MutableSet
from pathlib import Path
import shutil
from abc import ABC, abstractmethod


class BaseTask(ABC):
    filename_suffix = None
    folder_suffix = None

    def select_files(self, files: MutableSet[Path]) -> MutableSet[Path]:
        if self.filename_suffix is not None:
            return set(
                f
                for f in files
                if self.filename_suffix in (f.name, f.suffix) and f.is_file()
            )

        if self.folder_suffix is not None:
            folders = set(
                f
                for f in files
                if self.folder_suffix in (f.name, f.suffix) and f.is_dir()
            )
            for folder in folders:
                files.difference_update(folder.rglob("*"))
            return folders

        return set(f for f in files if f.is_file())

    @abstractmethod
    def process(self, env: Dict):
        raise NotImplementedError()

    def __repr__(self):
        return self.__class__.__name__


class Processor:
    def __init__(self):
        self.environment = dict()

        self._tasks: List[BaseTask] = list()
        self._source_files: MutableSet[Path] = set(Path("content").rglob("*"))

    @property
    def source_files(self):
        return self._source_files

    def register(self, task: BaseTask):
        self._tasks.append(task)

    def run(self):
        shutil.rmtree("output", ignore_errors=True)

        for task in self._tasks:
            files = task.select_files(self._source_files)
            number_of_selected_files = len(files)
            try:
                task.process(files, self)
            except Exception as e:
                raise ValueError(
                    f'Exception while running task "{task}" for these files: {", ".join(str(f) for f in files)}'
                ) from e

            print(
                f"{task.__class__.__name__}: {number_of_selected_files} files processed"
            )
