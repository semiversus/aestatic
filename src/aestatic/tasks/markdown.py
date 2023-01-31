from dataclasses import dataclass
from pathlib import Path
from typing import FrozenSet, List
import os

from aestatic.processor import Processor, BaseTask

import mistletoe
from jinja2 import Environment, FileSystemLoader


def resolve(p: Path):
    return p.resolve().relative_to(Path('.').resolve())


@dataclass
class Page:
    path: Path
    url: str
    content: str
    title: str
    parent: str = None
    next: str = None
    prev: str = None

    @classmethod
    def from_path(cls, path: Path) -> 'Page':
        try:
            meta_block, source_content = path.read_text().split('\n\n', maxsplit=1)
            meta = dict([tuple(n.strip() for n in l.split(':', maxsplit=1)) for l in meta_block.splitlines()])
        except Exception:
            raise ValueError(f'Problem parsing meta data from {path}')

        html_content = mistletoe.markdown(source_content)
        return Page(path.relative_to('content'), path.with_suffix('.html').relative_to('content'), html_content, **meta)


class MarkdownTask(BaseTask):
    filename_suffix = '.md'

    def process(self, files: FrozenSet[Path], processor: Processor):
        pages = [Page.from_path(p) for p in files]
        lookup_files = {page.path: page for page in pages}

        for page in pages:
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

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('page.html')

        for page in pages:
            output_path = 'output' / page.path.with_suffix('.html')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(template.render(page=page, root_path=os.path.relpath('output', output_path.parent)))
            processor.add_cache_entry(page.path, page.path.with_suffix('.html'))