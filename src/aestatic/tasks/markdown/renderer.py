import mistune
from slugify import slugify

class AestaticRenderer(mistune.HTMLRenderer):
    def heading(self, text, level, **attrs):
        anchor = slugify(text)
        return f"<h{level} id=\"{anchor}\">{text}<a href=\"#{anchor}\"><span class=\"icon has-text-grey-light ml-4 is-size-5\"><i class=\"icon-link\"></i></span></a></h{level}>\n"