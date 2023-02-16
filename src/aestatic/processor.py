import json
from typing import Dict, FrozenSet, List, MutableSet, Union
from pathlib import Path
import shutil
from abc import ABC, abstractmethod


def get_mtime(file: Path):
    if file.is_dir():
        return max(f.stat().st_mtime for f in file.rglob('*'))

    return file.stat().st_mtime


class BaseTask(ABC):
    filename_suffix = None
    folder_suffix = None

    def select_files(self, files: MutableSet[Path]) -> MutableSet[Path]:
        if self.filename_suffix is not None:
            return set(f for f in files if self.filename_suffix in (f.name, f.suffix) and f.is_file())

        if self.folder_suffix is not None:
            folders = set(f for f in files if self.folder_suffix in (f.name, f.suffix) and f.is_dir())
            for folder in folders:
                files.difference_update(folder.rglob('*'))
            return folders

        return set(f for f in files if f.is_file())

    def process_cache(self, files: FrozenSet[Path], processor: 'Processor'):
        cached_files = set(f for f in files if str(f) in processor.cache_dict)

        for file in tuple(cached_files):
            if get_mtime(file) > processor.cache_dict[str(file)]['timestamp']:
                cached_files.remove(file)
                continue

            if file.is_dir():
                cached_files.update(file.rglob('*'))

            for file in processor.cache_dict[str(file)]['output']:
                output_file = Path('output') / file
                output_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(Path('.cache') / file, output_file)

        return set(files) - cached_files

    @abstractmethod
    def process(self, env: Dict):
        raise NotImplementedError()


class Processor:
    def __init__(self):
        self._cache_file = Path('.cache/cache.json')
        self.environment = dict()

        try:
            self._cache_dict = json.loads(self._cache_file.read_text())
        except:
            self._cache_dict = dict()

        self._tasks: List[BaseTask] = list()
        self._source_files: MutableSet[Path] = set(Path('content').rglob('*'))

    @property
    def source_files(self):
        return self._source_files

    @property
    def cache_dict(self):
        return self._cache_dict

    def register(self, task: BaseTask):
        self._tasks.append(task)

    def add_cache_entry(self, source_file: Path, output: Union[Path, List[Path]]):
        if isinstance(output, Path):
            output = [output]

        for file in output:
            cache_file = '.cache' / file
            cache_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy('output' / file, cache_file)

        self._cache_dict[str('content' / source_file)] = {'timestamp': get_mtime('content' / source_file), 'output': [str(f) for f in output]}

    def run(self):
        shutil.rmtree('output', ignore_errors=True)

        for task in self._tasks:
            files = task.select_files(self._source_files)
            number_of_selected_files = len(files)
            files = task.process_cache(files, self)
            number_of_processed_files = len(files)
            task.process(files, self)
            print(f'{task.__class__.__name__}: {number_of_selected_files} files selected, {number_of_processed_files} files processed')

        self._cache_file.parent.mkdir(exist_ok=True)
        self._cache_file.write_text(json.dumps(self._cache_dict, indent=2))
