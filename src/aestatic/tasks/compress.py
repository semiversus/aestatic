import shutil

from aestatic.processor import Processor, BaseTask

class CompressTask(BaseTask):
    folder_suffix = '.compress'

    def process(self, files, processor: Processor):
        for file in files:
            output_path = 'output' / file.relative_to('content').with_suffix('.zip')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(file, output_path.parent / output_path.stem)
            shutil.make_archive(output_path.with_suffix(''), 'zip', output_path.parent, output_path.stem)
            shutil.rmtree(output_path.with_suffix(''))
            processor.add_cache_entry(file.relative_to('content'), output_path.relative_to('output'))
