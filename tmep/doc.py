"""Extract docstrings from func.py to document the template functions."""

import re
import textwrap
import typing
from pathlib import Path
from typing import Dict, List

from tmep import functions

Functions = functions.Functions


FunctionDoc = Dict[str, str]


class Doc:
    synopsises: FunctionDoc
    examples: FunctionDoc
    descriptions: FunctionDoc
    functions: List[str]

    def __init__(self):
        functions_ = Functions()
        functions = functions_.functions()
        self.synopsises: FunctionDoc = {}
        self.examples: FunctionDoc = {}
        self.descriptions: FunctionDoc = {}
        self.functions: List[str] = []
        for name, function in functions.items():
            self.functions.append(name)
            doc = function.__doc__
            if doc:
                doc = self.prepare_docstrings(doc)
                synopse = self.extract_value(doc, "synopsis")
                if synopse:
                    self.synopsises[name] = synopse

                example = self.extract_value(doc, "example")
                if example:
                    self.examples[name] = example

                description = self.extract_value(doc, "description", False)
                if description:
                    self.descriptions[name] = description
        self.functions.sort()

    def prepare_docstrings(self, string: str) -> str:
        return re.sub(r" {2,}", " ", string)

    def extract_value(
        self, string: str, key: str, inline_code: bool = True
    ) -> typing.Optional[str]:
        """Extract strings from the docstrings

        .. code-block:: text

            * synopsis: ``%shorten{text, max_size}``
            * example: ``%shorten{$title, 32}``
            * description: Shorten “text” on word boundarys.

        """
        regex: str = r"\* " + key + ": "
        if inline_code:
            regex = regex + "``(.*)``"
        else:
            regex = regex + "(.*)"
        value = re.findall(regex, string)
        if value:
            return value[0].replace("``", "")
        return None

    def underline(self, text: str, indent: int = 4) -> str:
        """Underline a given text"""
        length = len(text)
        indentation = " " * indent
        return indentation + text + "\n" + indentation + ("-" * length)

    def format(self, text: str, width: int = 78, indent: int = 4) -> str:
        """Apply textwrap to a given text string"""
        return textwrap.fill(
            text,
            width=width,
            initial_indent=" " * indent,
            subsequent_indent=" " * indent,
        )

    def get(self) -> str:
        """Retrieve a formated text string"""
        output = ""
        for function_name in self.functions:
            output += self.underline(function_name) + "\n\n"
            if function_name in self.synopsises:
                output += self.format(self.synopsises[function_name]) + "\n"
            if function_name in self.descriptions:
                output += self.format(self.descriptions[function_name], indent=8) + "\n"
            if function_name in self.examples:
                output += self.format(self.examples[function_name], indent=8) + "\n"
            output += "\n"
        return output


def get_doc() -> str:
    """
    Get the documentation string.

    .. code-block:: text

        alpha
        -----

        %alpha{text}
            This function first ASCIIfies the given text, then all non alphabet
            characters are replaced with whitespaces.

        alphanum
        --------

        %alphanum{text}
            This function first ASCIIfies the given text, then all non alpanumeric
            characters are replaced with whitespaces.

        ...


    :return: The documentation string.
    """
    return Doc().get()


def print_doc() -> None:
    """
    Print the documentation string.

    .. code-block:: text

        alpha
        -----

        %alpha{text}
            This function first ASCIIfies the given text, then all non alphabet
            characters are replaced with whitespaces.

        alphanum
        --------

        %alphanum{text}
            This function first ASCIIfies the given text, then all non alpanumeric
            characters are replaced with whitespaces.

        ...


    """
    print(get_doc())


def read_help_text_rst() -> str:
    with open(Path(__file__).parent / "help.rst", "r") as file:
        return file.read()
