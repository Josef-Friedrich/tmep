import re
from tmep import func


class Doc(object):

    def __init__(self):
        f = func.Functions()
        functions = f.functions()
        self.doc_strings = {}
        self.synopsises = {}
        self.examples = {}
        self.descriptions = {}
        self.functions = []
        for name, function in functions.items():
            self.functions.append(name)
            doc = function.__doc__
            if doc:
                self.doc_strings[name] = doc
                self.synopsises[name] = self.extract_value(doc, 'synopsis')
                self.examples[name] = self.extract_value(doc, 'example')
                self.descriptions[name] = self.extract_value(
                    doc, 'description', False
                )
        self.functions.sort()

    def extract_value(self, string, key, inline_code=True):
        regex = r'\* ' + key + ': '
        if inline_code:
            regex = regex + '``(.*)``'
        else:
            regex = regex + '(.*)'
        value = re.findall(regex, string)
        if value:
            return value[0]
        else:
            return False

    def get(self):
        output = ''
        for f in self.functions:
            output += f + '\n'
            if f in self.synopsises and isinstance(self.synopsises[f], str):
                output += self.synopsises[f] + '\n'
            if f in self.descriptions and isinstance(
                self.descriptions[f], str
            ):
                output += self.descriptions[f] + '\n'
            if f in self.examples and isinstance(self.examples[f], str):
                output += self.examples[f] + '\n'
            output += '\n'
        return output
