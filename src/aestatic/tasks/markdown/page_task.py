from dataclasses import dataclass
from pathlib import Path
from typing import FrozenSet, List
import os
from datetime import datetime

from aestatic.processor import Processor, BaseTask
from bs4 import BeautifulSoup
import mistune
from mistune.directives import RSTDirective
from jinja2 import Environment, FileSystemLoader
import htmlmin

from aestatic.tasks.markdown.page_renderer import PageRenderer, Admonition, Figure


def resolve(p: Path):
    return p.resolve().relative_to(Path(".").resolve())


renderer = PageRenderer(escape=False)
markdown_convert = mistune.create_markdown(
    escape=False,
    renderer=renderer,
    plugins=[
        RSTDirective([Admonition(), Figure()]),
        "strikethrough",
        "footnotes",
        "table",
        "speedup",
    ],
)


@dataclass
class Page:
    path: Path
    url: str
    content: str
    title: str
    english: bool = False
    latex: bool = False
    comments: bool = True
    date: datetime = None
    thumbnail: Path = None
    translation: Path = None
    template: str = "page.html"
    parent: str = None
    next: str = None
    prev: str = None
    draft: bool = False

    @property
    def summary(self) -> str:
        paragraphs = BeautifulSoup(self.content, "html.parser").find_all(['p', 'ul', 'ol'])

        if not paragraphs:
            return ""

        summary = []
        for paragraph in paragraphs:
            if paragraph.contents[0].name == 'img':
                continue

            summary.append(paragraph)

            if sum(len(p.text) for p in summary) > 300:
                if len(summary) == 1:
                    continue
                summary.pop()
                break

        return "".join(str(p) for p in summary)

    @classmethod
    def from_path(cls, path: Path) -> "Page":
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

        meta["path"] = path.relative_to("content")
        meta["url"] = path.with_suffix(".html").relative_to("content")
        meta["english"] = meta.get("english", "").lower() == "true"
        renderer.english = meta["english"]
        renderer.path = "output" / meta["path"].parent
        renderer.root_path = os.path.relpath("output", renderer.path)
        try:
            meta["content"] = markdown_convert(source_content)
        except Exception as e:
            raise ValueError(f"Problem parsing content from {path}") from e

        meta["latex"] = meta.get("latex", "").lower() == "true"
        meta["comments"] = meta.get("comments", "true").lower() == "true"
        meta["draft"] = meta.get("draft", "false").lower() == "true"

        if meta.get("date", False):
            meta["date"] = datetime.strptime(meta["date"], "%Y-%m-%d")

        if meta.get("thumbnail", False):
            meta["thumbnail"] = meta["path"].parent / meta["thumbnail"]

        if meta.get("translation", False):
            meta["translation"] = meta["path"].parent / meta["translation"]

        return Page(**meta)


class PageTask(BaseTask):
    filename_suffix = ".md"

    def process(self, files: FrozenSet[Path], processor: Processor):
        articles: List[Page] = list()

        pages = [Page.from_path(p) for p in files]
        pages = [p for p in pages if not p.draft]

        lookup_files = {page.path: page for page in pages}

        for page in pages:
            if page.path.parts[0] == "blog":
                articles.append(page)

            if page.next is not None:
                next_path = resolve(page.path.parent / page.next)
                next_page = lookup_files[next_path]
                next_page.prev = page
                page.next = next_page

            if page.parent is not None:

                def resolve_parent(page):
                    parent_path = resolve(page.path.parent / page.parent)
                    parent_page = lookup_files[parent_path]
                    if parent_page.parent is None:
                        return [parent_page]
                    if isinstance(parent_page.parent, list):
                        return parent_page.parent + [parent_page]
                    return resolve_parent(parent_page) + [parent_page]

                page.parent = resolve_parent(page)

        articles.sort(key=lambda p: p.date, reverse=True)

        for is_english in (True, False):
            lang_articles = [p for p in articles if is_english == p.english]

            for page, next_page in zip(lang_articles, lang_articles[1:]):
                page.next = next_page
                next_page.prev = page

        processor.environment["articles"] = articles

        env = Environment(loader=FileSystemLoader("templates"))

        for page in pages:
            output_path = "output" / page.path.with_suffix(".html")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            template = env.get_template(page.template)
            html = template.render(
                       page=page,
                       root_path=os.path.relpath("output", output_path.parent),
                       env=processor.environment,
                   )
            output_path.write_text(htmlmin.minify(html))
