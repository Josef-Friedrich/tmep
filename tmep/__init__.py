from tmep import tmpl
from tmep import func


class Template(tmpl.Template):
    def __init__(self, template):
        super(Template, self).__init__(template)


class Functions(func.Functions):
    def __init__(self, values):
        super(Functions, self).__init__(values)


def get_doc():
    f = func.Functions()
    functions = f.functions()
    for name, function in functions.items():
        print(name)
        print(function.__doc__)


def parse(template, values=None, additional_functions=None, functions=None):
    t = tmpl.Template(template)
    if not functions:
        f = func.Functions(values)
        functions = f.functions()

    if additional_functions:
        for k, v in additional_functions.items():
            functions[k] = v

    return t.substitute(values, functions)
