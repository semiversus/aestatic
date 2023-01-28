import sass

from aestatic.processor import Processor, BaseTask

class SassTask(BaseTask):
    folder_suffix = '.sass'

    def process(self, files, processor: Processor):
        for file in files:
            output_path = 'output' / file.relative_to('content').with_suffix('.css')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            css = sass.compile(filename=str(file / file.name), output_style='compressed')
            output_path.write_text(css)
            processor.add_cache_entry(file.relative_to('content'), output_path.relative_to('output'))
