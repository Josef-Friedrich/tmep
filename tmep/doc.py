"""Extract docstrings from func.py to document the template functions."""

from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from tmep import functions

Functions = functions.Functions

FunctionDoc = Dict[str, str]

fns = Functions().functions()


def _underline(text: str, indent: int = 4) -> str:
    """Underline a given text"""
    length = len(text)
    indentation = " " * indent
    return indentation + text + "\n" + indentation + ("-" * length)


def _wrap(text: str, width: int = 78, indent: int = 4) -> str:
    """Apply textwrap to a given text string"""
    return textwrap.fill(
        text,
        width=width,
        initial_indent=" " * indent,
        subsequent_indent=" " * indent,
    )


@dataclass
class FunctionDocumentationData:
    name: str
    synopsis: Optional[str]
    example: Optional[str]
    description: Optional[str]


class FunctionDocumentation:
    name: str
    synopsis: Optional[str]
    example: Optional[str]
    description: Optional[str]

    def __init__(self, name: str):
        self.name = name

        doc = fns[name].__doc__
        if doc:
            self.synopsis = self.__extract_value(doc, "synopsis")
            self.example = self.__extract_value(doc, "example")
            self.description = self.__extract_value(doc, "description")

    def __extract_value(self, string: str, key: str) -> Optional[str]:
        """Extract strings from the docstrings

        .. code-block:: text

            * synopsis: ``%shorten{text, max_size}``
            * example: ``%shorten{$title, 32}``
            * description: Shorten “text” on word boundarys.

        """
        value = re.findall(r"\* " + key + ": (.*)", string)
        if value:
            return re.sub(r" {2,}", " ", value[0])
        return None

    def get(self) -> str:
        output = _underline(self.name) + "\n\n"
        if self.synopsis:
            output += _wrap(self.synopsis) + "\n"
        if self.description:
            output += _wrap(self.description, indent=8) + "\n"
        if self.example:
            output += _wrap(self.example, indent=8) + "\n"
        output += "\n"
        return output


class Doc:
    synopsises: FunctionDoc
    examples: FunctionDoc
    descriptions: FunctionDoc
    functions: List[str]
    function_docs: list[FunctionDocumentationData]

    def __init__(self):
        functions_ = Functions()
        functions = functions_.functions()
        self.function_docs = []

        self.synopsises: FunctionDoc = {}
        self.examples: FunctionDoc = {}
        self.descriptions: FunctionDoc = {}
        self.functions: List[str] = []
        for name, function in functions.items():
            self.functions.append(name)
            doc = function.__doc__
            if doc:
                doc = self.prepare_docstrings(doc)
                synopsis = self.extract_value(doc, "synopsis")
                if synopsis:
                    self.synopsises[name] = synopsis

                example = self.extract_value(doc, "example")
                if example:
                    self.examples[name] = example

                description = self.extract_value(doc, "description", False)
                if description:
                    self.descriptions[name] = description

                self.function_docs.append(
                    FunctionDocumentationData(
                        name=name,
                        synopsis=synopsis,
                        example=example,
                        description=description,
                    )
                )
        self.functions.sort()

    def prepare_docstrings(self, string: str) -> str:
        return re.sub(r" {2,}", " ", string)

    def extract_value(
        self, string: str, key: str, inline_code: bool = True
    ) -> Optional[str]:
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

    def get(self) -> str:
        """Retrieve a formated text string"""
        output = ""
        for function_name in self.functions:
            output += _underline(function_name) + "\n\n"
            if function_name in self.synopsises:
                output += _wrap(self.synopsises[function_name]) + "\n"
            if function_name in self.descriptions:
                output += _wrap(self.descriptions[function_name], indent=8) + "\n"
            if function_name in self.examples:
                output += _wrap(self.examples[function_name], indent=8) + "\n"
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
