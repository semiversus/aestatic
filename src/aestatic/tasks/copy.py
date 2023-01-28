import shutil

from aestatic.processor import BaseTask

class CopyTask(BaseTask):
    def process(self, files, processor):
        for file in files:
            output_path = 'output' / file.relative_to('content')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(file, output_path)
