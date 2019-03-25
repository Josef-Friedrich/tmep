"""Extract docstrings from func.py to document the template functions."""

import re
from tmep import functions
import textwrap
Functions = functions.Functions


class Doc(object):

    def __init__(self):
        functions_ = Functions()
        functions = functions_.functions()
        self.synopsises = {}
        self.examples = {}
        self.descriptions = {}
        self.functions = []
        for name, function in functions.items():
            self.functions.append(name)
            doc = function.__doc__
            if doc:
                doc = self.prepare_docstrings(doc)
                self.synopsises[name] = self.extract_value(doc, 'synopsis')
                self.examples[name] = self.extract_value(doc, 'example')
                self.descriptions[name] = self.extract_value(
                    doc, 'description', False
                )
        self.functions.sort()

    def prepare_docstrings(self, string):
        return re.sub(r' {2,}', ' ', string)

    def extract_value(self, string, key, inline_code=True):
        """Extract strings from the docstrings

        .. code-block:: text

            * synopsis: ``%shorten{text, max_size}``
            * example: ``%shorten{$title, 32}``
            * description: Shorten “text” on word boundarys.

        """
        regex = r'\* ' + key + ': '
        if inline_code:
            regex = regex + '``(.*)``'
        else:
            regex = regex + '(.*)'
        value = re.findall(regex, string)
        if value:
            return value[0].replace('``', '')
        else:
            return False

    def underline(self, text, indent=4):
        """Underline a given text"""
        length = len(text)
        indentation = (' ' * indent)
        return indentation + text + '\n' + indentation + ('-' * length)

    def format(self, text, width=78, indent=4):
        """Apply textwrap to a given text string"""
        return textwrap.fill(
            text,
            width=width,
            initial_indent=' ' * indent,
            subsequent_indent=' ' * indent,
        )

    def get(self):
        """Retrieve a formated text string"""
        output = ''
        for f in self.functions:
            output += self.underline(f) + '\n\n'
            if f in self.synopsises and isinstance(self.synopsises[f], str):
                output += self.format(self.synopsises[f]) + '\n'
            if f in self.descriptions and isinstance(
                self.descriptions[f], str
            ):
                output += self.format(self.descriptions[f], indent=8) + '\n'
            if f in self.examples and isinstance(self.examples[f], str):
                output += self.format(self.examples[f], indent=8) + '\n'
            output += '\n'
        return output
