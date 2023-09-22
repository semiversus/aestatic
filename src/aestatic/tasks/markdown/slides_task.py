from typing import FrozenSet, List
from pathlib import Path
import os
from dataclasses import dataclass

from jinja2 import Environment, FileSystemLoader
import mistune
from mistune.directives import RSTDirective
import qrcode

from aestatic.processor import Processor, BaseTask
from aestatic.tasks.markdown.slides_renderer import SlideRenderer, Figure, Notes


renderer = SlideRenderer(escape=False)
markdown_convert = mistune.create_markdown(
    escape=False,
    renderer=renderer,
    plugins=[
        RSTDirective([Figure(), Notes()]),
        "strikethrough",
        "footnotes",
        "table",
        "speedup",
    ],
)


@dataclass
class Slide:
    path: Path
    url: str
    content: str
    title: str
    latex: str = None

    @classmethod
    def from_path(cls, path: Path) -> "Slide":
        try:
            meta_block, source_content = path.read_text().split("\n\n", maxsplit=1)
            meta = dict(
                [
                    tuple(n.strip() for n in l.split(":", maxsplit=1))
                    for l in meta_block.splitlines()
                ]
            )
        except Exception:
            raise ValueError(f"Problem parsing meta data from {path}")

        slides_source = [markdown_convert(s) for s in source_content.split("---\n")]
        html_content = "".join("<section>" + s + "</section>" for s in slides_source)
        return Slide(
            path.relative_to("content"),
            path.with_suffix(".html").relative_to("content"),
            html_content,
            **meta,
        )


class SlidesTask(BaseTask):
    filename_suffix = ".slides"

    def process(self, files: FrozenSet[Path], processor: Processor):
        pages = [Slide.from_path(p) for p in files]

        env = Environment(loader=FileSystemLoader("templates"))

        for page in pages:
            output_path = "output" / page.path.with_suffix(".html")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            template = env.get_template("slides.html")
            output_path.write_text(
                template.render(
                    page=page,
                    root_path=os.path.relpath("output", output_path.parent),
                    env=processor.environment,
                )
            )
            qr_img = qrcode.make("https://semiversus.com/" + str(page.url))
            qr_img.save(str(output_path).replace(".html", "_qr.png"))
