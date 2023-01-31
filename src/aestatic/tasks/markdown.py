from dataclasses import dataclass
from pathlib import Path
from typing import FrozenSet, List
import os

from aestatic.processor import Processor, BaseTask

import markdown
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
    parent_list: List[str] = None

    @classmethod
    def from_path(cls, path: Path) -> 'Page':
        try:
            meta_block, source_content = path.read_text().split('\n\n', maxsplit=1)
            meta = dict([tuple(n.strip() for n in l.split(':', maxsplit=1)) for l in meta_block.splitlines()])
        except Exception:
            raise ValueError(f'Problem parsing meta data from {path}')

        html_content = markdown.markdown(source_content)
        return Page(path.relative_to('content'), path.with_suffix('.html'), html_content, **meta)


class MarkdownTask(BaseTask):
    filename_suffix = '.md'

    def process(self, files: FrozenSet[Path], processor: Processor):
        pages = [Page.from_path(p) for p in files]
        lookup_files = {page.path: page for page in pages}

        for page in pages:
            if page.next is not None:
                next_path = resolve(page.path.parent / page.next)
                lookup_files[next_path].prev = page

            if page.parent is not None:
                current_page = page
                parent_list = []

                while current_page.parent:
                    assert len(parent_list) < 10, f'Recusion of "parent" in {page.path}'
                    parent_path = resolve(current_page.path.parent / current_page.parent)
                    current_page = lookup_files[parent_path]
                    parent_list.append(current_page)

                parent_list.reverse()
                page.parent_list = parent_list

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('page.html')

        for page in pages:
            output_path = 'output' / page.path.with_suffix('.html')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(template.render(page=page, root_path=os.path.relpath('output', output_path.parent)))
            processor.add_cache_entry(page.path, page.path.with_suffix('.html'))