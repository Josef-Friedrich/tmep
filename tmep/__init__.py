from tmep import doc, functions, template
from importlib import metadata

__version__: str = metadata.version('tmep')

doc


class Template(template.Template):
    def __init__(self, template):
        super(Template, self).__init__(template)


class Functions(functions.Functions):
    def __init__(self, values=None):
        super(Functions, self).__init__(values)


def parse(template: str, values=None, additional_functions=None,
          functions=None):
    template_ = Template(template)
    if not functions:
        functions_ = Functions(values)
        functions = functions_.functions()

    if additional_functions:
        for k, v in additional_functions.items():
            functions[k] = v

    return template_.substitute(values, functions)
