import functemplate
import functions

class Template(functemplate.Template):

    def __init__(self, template):
        super(Template, self).__init__(template)

class Functions(functions.Functions):

    def __init__(self, values):
        super(Functions, self).__init__(values)
