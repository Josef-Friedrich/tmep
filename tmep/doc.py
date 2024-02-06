"""Extract docstrings from func.py to document the template functions."""

from __future__ import annotations

import re
import textwrap
from pathlib import Path
from typing import Literal, Optional

from tmep.functions import Functions

fns = Functions().functions()
OutputFormat = Literal["txt", "rst"]


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


class FnDoc:
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

    def format(self, output_format: OutputFormat = "txt") -> str:
        if output_format == "txt":
            output = _underline(self.name) + "\n\n"
            if self.synopsis:
                output += _wrap(self.synopsis) + "\n"
            if self.description:
                output += _wrap(self.description, indent=8) + "\n"
            if self.example:
                output += _wrap(self.example, indent=8) + "\n"
            return output
        elif output_format == "rst":
            output = f"- **{self.name}**: {self.synopsis}\n\n{self.description} Example: {self.example}\n"
            return textwrap.fill(output, width=78, subsequent_indent="  ")


class FnDocCollection:
    fn_names: list[str]
    fn_docs: list[FnDoc]

    def __init__(self) -> None:
        self.fn_docs = []
        self.fn_names = []
        for name, _ in fns.items():
            self.fn_docs.append(FnDoc(name=name))
        self.fn_names.sort()

    def format(self, output_format: OutputFormat = "txt") -> str:
        """Retrieve a formated text string"""
        output: list[str] = []
        for fun_doc in self.fn_docs:
            output.append(fun_doc.format(output_format))
        return "\n".join(output)


def format(output_format: OutputFormat = "rst") -> str:
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
    return FnDocCollection().format(output_format)


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
    print(format())


def read_help_text_rst() -> str:
    with open(Path(__file__).parent / "help.rst", "r") as file:
        return file.read()
