import mistune_
from mistune_.directives import DirectivePlugin
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html as pygments_html


class SlideRenderer(mistune_.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = pygments_html.HtmlFormatter(nowrap=True)
            highlighted = highlight(code, lexer, formatter)
            return '<pre>' + highlighted + '</pre>'
        return '<pre><code>' + mistune_.escape(code) + '</code></pre>'

    def list_item(self, text: str) -> str:
        return '<li class="fragment">' + text + '</li>\n'


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

    def render(self, image, title, author='', source='', license='', scale=50):
        h = f'<figure><img src="{image}" style="height: {scale}; width: {scale}"><figcaption>{title}'

        if author:
            h += f' (Quelle: <a href="{source}">{author}</a>'
            if license:
                h += f', Lizenz {license}'
            h += ')'

        return h + '</figcaption></figure>'


class Notes(DirectivePlugin):
    def parse(self, block, m, state):
        #self.parse_type(m)
        title = self.parse_title(m)
        content = self.parse_content(m).strip()

        return {
                    'type': 'notes',
                    'children': self.parse_tokens(block, content, state),
                }

    def __call__(self, directive, md):
        directive.register('notes', self.parse)

        if md.renderer.NAME == 'html':
            md.renderer.register('notes', Notes.render)

    def render(self, text):
        return f'<aside class="notes">{text}</aside>'
