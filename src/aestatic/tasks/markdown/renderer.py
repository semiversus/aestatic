import mistune
from mistune.directives import DirectivePlugin

from slugify import slugify

class AestaticRenderer(mistune.HTMLRenderer):
    def heading(self, text, level, **attrs):
        anchor = slugify(text)
        return f"<h{level} id=\"{anchor}\">{text}<a href=\"#{anchor}\"><span class=\"icon has-text-grey-light ml-4 is-size-5\"><i class=\"icon-link\"></i></span></a></h{level}>\n"


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
