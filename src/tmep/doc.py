"""Extract docstrings from func.py to document the template functions."""

from __future__ import annotations

import argparse
import re
import textwrap
from pathlib import Path
from typing import Literal, Optional

from tmep.functions import DefaultTemplateFunctions

fns = DefaultTemplateFunctions().get()
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
            body = _wrap(f"{self.synopsis}:\n\n{self.description}", indent=2)
            if self.example:
                body += "\n\n" + _wrap(f"**Example:** {self.example}", indent=2)
            return self.name + "\n" + body + "\n"


class FnDocCollection:
    fn_names: list[str]
    fn_docs: list[FnDoc]

    def __init__(self) -> None:
        self.fn_docs = []
        self.fn_names = []
        for name, _ in fns.items():
            self.fn_names.append(name)
            self.fn_docs.append(FnDoc(name=name))
        self.fn_names.sort()

    def format(self, output_format: OutputFormat = "txt") -> str:
        """Retrieve a formated text string"""
        output: list[str] = []
        for fn_name in self.fn_names:
            output.append(FnDoc(fn_name).format(output_format))
        return "\n".join(output)


def _format_fn_docs(output_format: OutputFormat = "rst") -> str:
    """
    Format the documentation of the template functions in different formats.

    :return: The documentation string.
    """
    return FnDocCollection().format(output_format)


def _read_general_introduction_rst() -> str:
    with open(Path(__file__).parent / "help.rst", "r") as file:
        return file.read()


DocOutput = Literal[
    "functions_rst",
    "functions_txt",
    "introduction_rst",
]


def get_doc(doc: DocOutput = "functions_txt") -> str:
    """O
    Get the documentation in the specified format.

    :param doc: The format of the documentation to retrieve.
      Default is ``functions_txt``. Possible values are ``functions_rst``,
      ``functions_txt``, and ``introduction_rst``.

    :return: The documentation in the specified format.
    """
    if doc == "functions_rst":
        return _format_fn_docs("rst")
    if doc == "functions_txt":
        return _format_fn_docs("txt")
    if doc == "introduction_rst":
        return _read_general_introduction_rst()


def print_doc() -> None:
    """
    Little command line interface to print the documentation.
    """

    parser = argparse.ArgumentParser(
        prog="tmep-doc", description="Print documentation about TMEP"
    )
    parser.add_argument(
        "--introduction-rst",
        help="Print the help text in reStructuredText format.",
        action="store_true",
    )
    parser.add_argument(
        "--functions-rst",
        help="Print the functions documentation in reStructuredText format.",
        action="store_true",
    )

    parser.add_argument(
        "--functions-txt",
        help="Print the functions documentation in plain text format.",
        action="store_true",
    )

    args = parser.parse_args()

    if args.introduction_rst:
        print(_read_general_introduction_rst())
    if args.functions_rst:
        print(_format_fn_docs("rst"))
    if args.functions_txt:
        print(_format_fn_docs("txt"))


__all__: list[str] = ["get_doc", "print_doc"]
