from pathlib import Path

import mistune
from mistune.directives import DirectivePlugin
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html as pygments_html

from slugify import slugify


def human_readable_size(size):
    """taken from https://stackoverflow.com/a/43690506"""
    for unit in ["B", "KiB", "MiB", "GiB"]:
        if size < 1024.0 or unit == "GiB":
            break
        size /= 1024.0
    return f"{size:.1f} {unit}"


class PageRenderer(mistune.HTMLRenderer):
    def heading(self, text, level, **attrs):
        anchor = slugify(text)
        return f'<h{level} id="{anchor}">{text} <a href="#{anchor}" class="headerlink" title="Permalink"><span class="icon"><img src="{self.root_path}/theme/img/link.svg" alt="link symbol"></span></a></h{level}>\n'

    def block_code(self, code, info=None):
        if info:
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = pygments_html.HtmlFormatter(nowrap=True)
            highlighted = highlight(code, lexer, formatter)
            return "<pre>" + highlighted + "</pre>"
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"

    def link(self, text: str, url: str, title=None):
        if url.startswith("http") or url.startswith("#"):
            icon = f' <svg class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><path d="M128 320c0 0 29.412-96 192-96v96l192-128-192-128v96c-128 0-192 79.836-192 160zM352 384h-288v-192h62.938c5.047-5.959 10.456-11.667 16.244-17.090 21.982-20.595 48.281-36.326 78.057-46.91h-221.239v320h416v-134.312l-64 42.667v27.645z"></path></svg>'
            return f'<a href="{self.safe_url(url)}">{text}{icon}</a>'

        if not url.partition("#")[0].endswith("html"):
            file_size = (self.path / url).stat().st_size
            icon = f' <svg class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><path d="M448 256h-80l-112 112-112-112h-80l-64 128v32h512v-32l-64-128zM0 448h512v32h-512v-32zM288 160v-128h-64v128h-112l144 144 144-144h-112z"></path></svg>'
            return f'<a href="{self.safe_url(url)}" title="{Path(url).name} - {human_readable_size(file_size)}">{text}{icon}</a>'

        return f'<a href="{self.safe_url(url)}">{text}</a>'


class Admonition(DirectivePlugin):
    SUPPORTED_NAMES = {"info", "warning", "danger"}

    def parse(self, block, m, state):
        name = self.parse_type(m)
        attrs = {"name": name}

        title = self.parse_title(m)
        content = self.parse_content(m).strip()

        icons = {"info": "info", "warning": "notification", "danger": "notification"}

        if content:
            children = [
                {
                    "type": "admonition_title",
                    "text": title,
                    "attrs": {"icon": icons[name]},
                },
                {
                    "type": "admonition_content",
                    "children": self.parse_tokens(block, content, state),
                },
            ]
        else:
            children = [
                {
                    "type": "admonition_content",
                    "text": title,
                }
            ]

        return {
            "type": "admonition",
            "children": children,
            "attrs": attrs,
        }

    def __call__(self, directive, md):
        for name in self.SUPPORTED_NAMES:
            directive.register(name, self.parse)

        if md.renderer.NAME == "html":
            md.renderer.register("admonition", Admonition.render_admonition)
            md.renderer.register("admonition_title", Admonition.render_admonition_title)
            md.renderer.register(
                "admonition_content", Admonition.render_admonition_content
            )

    def render_admonition(self, text, name):
        return f'<div class="message is-{name}">{text}</section>\n'

    def render_admonition_title(self, text, icon):
        return (
            '<div class="message-header"><span>'
            + text
            + f'</span><span class="icon"><img src="{self.root_path}//theme/img/{icon}.svg" alt="severity symbol"></span></div>\n'
        )

    def render_admonition_content(self, text):
        return '<div class="message-body">' + text + "</div>\n"


class Figure(DirectivePlugin):
    def parse(self, block, m, state):
        attrs = dict(self.parse_options(m))
        attrs["image"] = self.parse_title(m)
        attrs["source"] = attrs.get("source", "")

        return {
            "type": "figure",
            "attrs": attrs,
        }

    def __call__(self, directive, md):
        directive.register("figure", self.parse)

        if md.renderer.NAME == "html":
            md.renderer.register("figure", Figure.render)

    def render(self, image, title, author="", source="", license=""):
        h = f'<div class="card mb-4"><div class="card-image"><figure><img src="{image}"></figure></div><div class="card-content has-text-centered">{title}'

        if author or source:
            if source and not author:
                h += f' (<a href="{source}">{"Source" if self.english else "Quelle"}</a>'
            elif source:
                h += f' ({"Source" if self.english else "Quelle"}: <a href="{source}">{author}</a>'
            else:
                h += f' ({"Source" if self.english else "Quelle"}: {author}'
            if license:
                h += f', {"license" if self.english else "Lizenz"} {license}'
            h += ")"

        return h + "</div></div>"
