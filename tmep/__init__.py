
from tmep import tmpl
from tmep import func
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


class Template(tmpl.Template):
    def __init__(self, template):
        super(Template, self).__init__(template)


class Functions(func.Functions):
    def __init__(self, values):
        super(Functions, self).__init__(values)


def parse(template, values=None, additional_functions=None, functions=None):
    t = tmpl.Template(template)
    if not functions:
        f = func.Functions(values)
        functions = f.functions()

    if additional_functions:
        for k, v in additional_functions.items():
            functions[k] = v

    return t.substitute(values, functions)
