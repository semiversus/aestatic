from importlib import import_module

_plugins = {
    'speedup': 'mistune_.plugins.speedup.speedup',
    'strikethrough': 'mistune_.plugins.formatting.strikethrough',
    'mark': 'mistune_.plugins.formatting.mark',
    'insert': 'mistune_.plugins.formatting.insert',
    'superscript': 'mistune_.plugins.formatting.superscript',
    'subscript': 'mistune_.plugins.formatting.subscript',
    'footnotes': 'mistune_.plugins.footnotes.footnotes',
    'table': 'mistune_.plugins.table.table',
    'url': 'mistune_.plugins.url.url',
    'abbr': 'mistune_.plugins.abbr.abbr',
    'def_list': 'mistune_.plugins.def_list.def_list',
    'math': 'mistune_.plugins.math.math',
    'ruby': 'mistune_.plugins.ruby.ruby',
    'task_lists': 'mistune_.plugins.task_lists.task_lists',
    'spoiler': 'mistune_.plugins.spoiler.spoiler',
}
_cached_modules = {}


def import_plugin(name):
    if name in _cached_modules:
        return _cached_modules[name]

    if callable(name):
        return name

    if name in _plugins:
        module_path, func_name = _plugins[name].rsplit(".", 1)
    else:
        module_path, func_name = name.rsplit(".", 1)

    module = import_module(module_path)
    plugin = getattr(module, func_name)
    _cached_modules[name] = plugin
    return plugin
