import tmpl
import func

class Template(tmpl.Template):

    def __init__(self, template):
        super(Template, self).__init__(template)

class Functions(func.Functions):

    def __init__(self, values):
        super(Functions, self).__init__(values)

def parse(template, values=None, additional_functions=None, functions=None):
    t = tmpl.Template(template)
    if not functions:
        functions = func.Functions(values)

    return t.substitute(values, functions)