import sass

from aestatic.processor import Processor, BaseTask


class SassTask(BaseTask):
    folder_suffix = ".sass"

    def process(self, files, processor: Processor):
        git_sha = processor.environment["git_sha"][:7]

        for file in files:
            output_path = "output" / file.relative_to("content").with_suffix(
                f".{git_sha}.css"
            )
            output_path.parent.mkdir(parents=True, exist_ok=True)
            css = sass.compile(
                filename=str(file / file.name), output_style="compressed"
            )
            output_path.write_text(css)
