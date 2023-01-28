import shutil

from aestatic.processor import Processor, BaseTask

class SlidesTask(BaseTask):
    folder_suffix = '.slides'

    def process(self, files, processor: Processor):
        for file in files:
            output_path = 'output' / file.relative_to('content').with_suffix('.zip')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.make_archive(output_path, 'zip', file)

            processor.source_files.difference_update(file.rglob('*'))
