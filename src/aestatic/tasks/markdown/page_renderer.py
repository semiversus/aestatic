import mistune
from mistune.directives import DirectivePlugin
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html as pygments_html

from slugify import slugify


class PageRenderer(mistune.HTMLRenderer):
    def heading(self, text, level, **attrs):
        anchor = slugify(text)
        return f'<h{level} id="{anchor}">{text}<a href="#{anchor}" class="headerlink" title="Permalink"><span class="icon ml-4 is-size-5"><i class="icon-link"></i></span></a></h{level}>\n'

    def block_code(self, code, info=None):
        if info:
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = pygments_html.HtmlFormatter(nowrap=True)
            highlighted = highlight(code, lexer, formatter)
            return '<pre>' + highlighted + '</pre>'
        return '<pre><code>' + mistune.escape(code) + '</code></pre>'

    def link(self, text: str, url: str, title=None):
        if url.startswith('http'):
            icon = f'<span class="icon"><i class="icon-share is-size-7"></i></span>'
        elif not url.partition('#')[0].endswith('html'):
            icon = f'<span class="icon"><i class="icon-download2 is-size-7"></i></span>'
        else:
            icon = ''

        return f'<a href="{self.safe_url(url)}">{text}{icon}</a>'


class Admonition(DirectivePlugin):
    SUPPORTED_NAMES = {"info", "warning", "danger"}

    def parse(self, block, m, state):
        name = self.parse_name(m)
        attrs = {'name': name}

        title = self.parse_title(m)
        content = self.parse_content(m).strip()

        icons = {'info': 'info', 'warning': 'notification', 'danger': 'notification'}

        if content:
            children = [
                {
                    'type': 'admonition_title',
                    'text': title,
                    'attrs': {'icon': icons[name]}
                },
                {
                    'type': 'admonition_content',
                    'children': self.parse_tokens(block, content, state),
                }
            ]
        else:
            children = [
                {
                    'type': 'admonition_content',
                    'text': title,
                }
            ]

        return {
            'type': 'admonition',
            'children': children,
            'attrs': attrs,
        }

    def __call__(self, directive, md):
        for name in self.SUPPORTED_NAMES:
            directive.register(name, self.parse)

        if md.renderer.NAME == 'html':
            md.renderer.register('admonition', Admonition.render_admonition)
            md.renderer.register('admonition_title', Admonition.render_admonition_title)
            md.renderer.register('admonition_content', Admonition.render_admonition_content)

    def render_admonition(self, text, name):
        return f'<section class="message is-{name}">{text}</section>\n'

    def render_admonition_title(self, text, icon):
        return '<div class="message-header"><span>' + text + f'</span><span class="icon"><i class="icon-{icon}"></i></span></div>\n'

    def render_admonition_content(self, text):
        return '<div class="message-body">' + text + '</div>\n'


class Figure(DirectivePlugin):
    def parse(self, block, m, state):
        attrs = dict(self.parse_options(m))
        attrs['image'] = self.parse_title(m)
        attrs['source'] = attrs.get('source', '')

        return {
            'type': 'figure',
            'attrs': attrs,
        }

    def __call__(self, directive, md):
        directive.register('figure', self.parse)

        if md.renderer.NAME == 'html':
            md.renderer.register('figure', Figure.render)

    def render(self, image, title, author='', source='', license=''):
        h = f'<div class="card mb-4"><div class="card-image"><figure class="image"><img src="{image}"></figure></div><div class="card-content has-text-centered">{title}'

        if author:
            h += f' ({"Source" if self.english else "Quelle"}: <a href="{source}">{author}</a>'
            if license:
                h += f', {"license" if self.english else "Lizenz"} {license}'
            h += ')'

        return h + '</div></div>'
