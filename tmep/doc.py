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
        for name, function in functions.items():
            doc = function.__doc__
            if doc:
                self.doc_strings[name] = doc
                self.synopsises[name] = self.extract_value(doc, 'example')
                self.examples[name] = self.extract_value(doc, 'example')
                self.descriptions[name] = self.extract_value(doc, 'example')


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
            return ''

    def get_doc(self):
        f = func.Functions()
        functions = f.functions()
        for name, function in functions.items():
            print(name)
            if function.__doc__:
                example = docstring_key(function.__doc__, 'example')
                print(example)
