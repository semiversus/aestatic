import shutil

from aestatic.processor import BaseTask

class SourceTask(BaseTask):
    folder_suffix = '.source'

    def process(self, files, processor):
        pass
