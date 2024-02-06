# Copyright 2016, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
"""This file originates from the file `beets/library.py
<https://github.com/beetbox/beets/blob/58afaf07a52df2b53bb2f8990cd06005cd063d9e/beets/library.py#L1341>`_
of the `beets project <http://beets.io>`_.
"""

import re
import textwrap
import time
import typing
from typing import Optional

from unidecode import unidecode

from tmep.types import FunctionCollection, Values


def _int_arg(s: str) -> int:
    """Convert a string argument to an integer for use in a template
    function. May raise a ValueError.
    """
    return int(s.strip())


class DefaultTemplateFunctions:
    """A container class for the default functions provided to path
    templates. These functions are contained in an object to provide
    additional context to the functions -- specifically, the Item being
    evaluated.
    """

    prefix = "fn_"

    values: Optional[Values]

    func_names: typing.List[str]

    def __init__(self, values: Optional[Values] = None):
        """Parametrize the functions."""
        self.values = values

    def functions(self) -> FunctionCollection:
        """Returns a dictionary containing the functions defined in this
        object. The keys are function names (as exposed in templates)
        and the values are Python functions.
        """
        out: FunctionCollection = {}
        for key in self.func_names:
            out[key[len(self.prefix) :]] = getattr(self, key)
        return out

    def fn_alpha(self, text: str) -> str:
        """
        * synopsis: ``%alpha{text}``
        * description: This function first ASCIIfies the given text, then all \
            non alphabet characters are replaced with whitespaces.
        * example: ``%alpha{a1b23c}`` → ``a b c``
        """
        text = self.fn_asciify(text)
        text = re.sub(r"[^a-zA-Z]+", " ", text)
        return re.sub(r"\s+", " ", text)

    def fn_alphanum(self, text: str) -> str:
        """
        * synopsis: ``%alphanum{text}``
        * description: This function first ASCIIfies the given text, then all \
            non alpanumeric characters are replaced with whitespaces.
        * example: ``%alphanum{après-évêque1}`` → ``apres eveque1``
        """
        text = self.fn_asciify(text)
        text = re.sub(r"[^a-zA-Z0-9]+", " ", text)
        return re.sub(r"\s+", " ", text)

    @staticmethod
    def fn_asciify(text: str) -> str:
        """
        * synopsis: ``%asciify{text}``
        * description: Translate non-ASCII characters to their ASCII \
            equivalents. For example, “café” becomes “cafe”. Uses the mapping \
            provided by the unidecode module.
        * example: ``%asciify{äÄöÖüÜ}`` → ``aeAeoeOeueUe``
        """
        ger_umlaute = {"ae": "ä", "oe": "ö", "ue": "ü", "Ae": "Ä", "Oe": "Ö", "Ue": "Ü"}
        for replace, search in ger_umlaute.items():
            text = text.replace(search, replace)
        return str(unidecode(text).replace("[?]", ""))

    @staticmethod
    def fn_delchars(text: str, chars: str) -> str:
        """
        * synopsis: ``%delchars{text,chars}``
        * description: Delete every single character of “chars“ in “text”.
        * example: ``%delchars{Schubert, ue}`` → ``Schbrt``
        """
        for char in chars:
            text = text.replace(char, "")
        return text

    @staticmethod
    def fn_deldupchars(text: str, chars: str = r"-_\.") -> str:
        """
        * synopsis: ``%deldupchars{text,chars}``
        * description: Search for duplicate characters and replace with only \
            one occurrance of this characters.
        * example: ``%deldupchars{a---b___c...d}`` → ``a-b_c.d``; \
            ``%deldupchars{a---b___c, -}`` → ``a-b___c``
        """
        import re

        return re.sub(r"([" + chars + r"])\1*", r"\1", text)

    @staticmethod
    def fn_first(
        text: str, count: int = 1, skip: int = 0, sep: str = "; ", join_str: str = "; "
    ) -> str:
        """
        * synopsis: ``%first{text}`` or ``%first{text,count,skip}`` or \
            ``%first{text,count,skip,sep,join}``
        * description: Returns the first item, separated by ``;``. You can use \
            ``%first{text,count,skip}``, where count is the number of items \
            (default 1) and skip is number to skip (default 0). You can also \
            use ``%first{text,count,skip,sep,join}`` where ``sep`` is the separator, \
            like ``;`` or ``/`` and join is the text to concatenate the items.
        * example: ``%first{Alice / Bob / Eve,2,0, / , & }`` → ``Alice & Bob``

        :param text: the string
        :param count: The number of items included
        :param skip: The number of items skipped
        :param sep: the separator. Usually is '; ' (default) or '/ '
        :param join_str: the string which will join the items, default '; '.
        """
        skip = int(skip)
        count = skip + int(count)
        return join_str.join(text.split(sep)[skip:count])

    @staticmethod
    def fn_if(condition: str, trueval: str, falseval: str = "") -> str:
        """If ``condition`` is nonempty and nonzero, emit ``trueval``;
        otherwise, emit ``falseval`` (if provided).

        * synopsis: ``%if{condition,trueval}`` or \
            ``%if{condition,trueval,falseval}``
        * description: If condition is nonempty (or nonzero, if it’s a \
            number), then returns the second argument. Otherwise, returns the \
            third argument if specified (or nothing if ``falseval`` is left off).
        * example: ``x%if{false,foo}`` → ``x``

        """
        c: typing.Union[str, int]
        c = condition
        try:
            int_condition = _int_arg(condition)
        except ValueError:
            if condition.lower() == "false":
                return falseval
        else:
            c = int_condition

        if c:
            return trueval
        else:
            return falseval

    def fn_ifdef(self, field: str, trueval: str = "", falseval: str = "") -> str:
        """If field exists return trueval or the field (default) otherwise,
        emit return falseval (if provided).

        * synopsis: ``%ifdef{field}``, ``%ifdef{field,trueval}`` or \
            ``%ifdef{field,trueval,falseval}``
        * description: If field exists, then return ``trueval`` or field \
            (default). Otherwise, returns ``falseval``. The field should be \
            entered without ``$``.
        * example: ``%ifdef{compilation,Compilation}``

        :param field: The name of the field
        :param trueval: The string if the condition is true
        :param falseval: The string if the condition is false
        :return: The string, based on condition
        """
        if self.values and field in self.values:
            return trueval
        else:
            return falseval

    def fn_ifdefempty(self, field: str, trueval: str = "", falseval: str = ""):
        """If field exists and is emtpy return trueval
        otherwise, emit return falseval (if provided).

        * synopsis: ``%ifdefempty{field,text}`` or \
            ``%ifdefempty{field,text,falsetext}``
        * description: If field exists and is empty, then return ``truetext``. \
            Otherwise, returns ``falsetext``. The field should be \
            entered without ``$``.
        * example: ``%ifdefempty{compilation,Album,Compilation}``

        :param field: The name of the field
        :param trueval: The string if the condition is true
        :param falseval: The string if the condition is false
        :return: The string, based on condition
        """
        if not self.values:
            return falseval
        if (
            field not in self.values
            or (field in self.values and not self.values[field])
            or re.search(r"^\s*$", self.values[field])
        ):
            return trueval
        else:
            return falseval

    def fn_ifdefnotempty(
        self, field: str, trueval: str = "", falseval: str = ""
    ) -> str:
        """If field is not emtpy return trueval or the field (default)
        otherwise, emit return falseval (if provided).

        * synopsis: ``%ifdefnotempty{field,text}`` or \
            ``%ifdefnotempty{field,text,falsetext}``
        * description: If field is not empty, then return ``truetext``. \
            Otherwise, returns ``falsetext``. The field should be \
            entered without ``$``.
        * example: ``%ifdefnotempty{compilation,Compilation,Album}``

        :param field: The name of the field
        :param trueval: The string if the condition is true
        :param falseval: The string if the condition is false
        :return: The string, based on condition
        """
        if not self.values:
            return trueval
        if (
            field not in self.values
            or (field in self.values and not self.values[field])
            or re.search(r"^\s*$", self.values[field])
        ):
            return falseval
        else:
            return trueval

    @staticmethod
    def fn_initial(text: str) -> str:
        """

        * synopsis: ``%initial{text}``
        * description: Get the first character of a text in lowercase. The \
            text is converted to ASCII. All non word characters are erased.
            Only letters and numbers are preserved. If the first character is
            a number, then the result is '0'.
        * example: ``%initial{Schubert}`` → ``s``

        :param string text: Input text to build initial from.
        :return: A single character
        """
        text = unidecode(text)
        text = re.sub(r"[^a-zA-Z0-9]+", "", text)
        text = text[0:1]
        text = text.lower()
        if not text:
            return "_"

        try:
            int(text)
            text = "0"
        except Exception:
            pass

        return text

    @staticmethod
    def fn_left(text: str, n: str) -> str:
        """Get the leftmost characters of a string.

        * synopsis: ``%left{text,n}``
        * description: Return the first “n” characters of “text”.
        * example: ``%left{Schubert, 3}`` → ``Sch``
        """
        return text[0 : _int_arg(n)]

    @staticmethod
    def fn_lower(text: str) -> str:
        """Convert a string to lower case

        * synopsis: ``%lower{text}``
        * description: Convert “text” to lowercase.
        * example: ``%lower{SCHUBERT}`` → ``schubert``
        """
        return text.lower()

    @staticmethod
    def fn_nowhitespace(text: str, replace: str = "-") -> str:
        """
        * synopsis: ``%nowhitespace{text,replace}``
        * description: Replace all whitespace characters with ``replace``. \
            By default: a dash (``-``)
        * example: ``%nowhitespace{a b}`` → ``a-b``; ``%nowhitespace{a b, _}`` → ``a_b``
        """
        return re.sub(r"\s+", replace, text)

    @staticmethod
    def fn_num(number: int, count: int = 2) -> str:
        """Pad decimal number with leading zeros

        * synopsis: ``%num{number,count}``
        * description: Pad decimal number with leading zeros.
        * example: ``%num{7,3}`` → ``007``
        """
        return str(number).zfill(int(count))

    @staticmethod
    def fn_replchars(text: str, replace: str, chars: str) -> str:
        """
        * synopsis: ``%replchars{text,chars,replace}``
        * description: Replace the characters “chars” in “text” with \
            “replace”.
        * example: ``%replchars{Schubert,-,ue}`` → ``Sch-b-rt``
        """
        for char in chars:
            text = text.replace(char, replace)
        return text

    @staticmethod
    def fn_right(text: str, n: str) -> str:
        """Get the rightmost characters of a string.

        * synopsis: ``%right{text,n}``
        * description: Return the last “n” characters of “text”.
        * example: ``%right{Schubert,3}`` → ``ert``
        """
        return text[-_int_arg(n) :]

    @staticmethod
    def fn_sanitize(text: str) -> str:
        """
        * synopsis: ``%sanitize{text}``
        * description: Delete characters that are not allowed in most file systems.
        * example: ``%sanitize{x:*?<>|/~&x}`` → ``xx``
        """
        for char in ':*?"<>|\/~&{}':  # noqa: W605
            text = text.replace(char, "")
        return text

    @staticmethod
    def fn_shorten(text: str, max_size: int = 32) -> str:
        """Shorten the given text to ``max_size``

        * synopsis: ``%shorten{text}`` or ``%shorten{text,max_size}``
        * description: Shorten “text” on word boundarys.
        * example: ``%shorten{Lorem ipsum dolor sit, 10}`` → ``Lorem``
        """
        max_size = int(max_size)
        if len(text) <= max_size:
            return text
        text = textwrap.wrap(text, max_size)[0]
        import re

        text = re.sub(r"\W+$", "", text)
        return text.strip()

    @staticmethod
    def fn_time(text: str, fmt: str, cur_fmt: str) -> str:
        """Format a time value using `strftime`.

        * synopsis: ``%time{date_time,format,curformat}``
        * description: Return the date and time in any format accepted by \
            ``strftime``. For example, to get the year, use ``%time{$added,%Y}``.
        * example: ``%time{30 Nov 2024,%Y,%d %b %Y}`` → ``2024``
        """
        return time.strftime(fmt, time.strptime(text, cur_fmt))

    @staticmethod
    def fn_title(text: str) -> str:
        """Convert a string to title case

        * synopsis: ``%title{text}``
        * description: Convert “text” to Title Case.
        * example: ``%title{franz schubert}`` → ``Franz Schubert``
        """
        return text.title()

    @staticmethod
    def fn_upper(text: str) -> str:
        """Covert a string to upper case

        * synopsis: ``%upper{text}``
        * description: Convert “text” to UPPERCASE.
        * example: ``%upper{foo}`` → ``FOO``
        """
        return text.upper()


# Get the name of fn_* functions in the above class.
DefaultTemplateFunctions.func_names = [
    s
    for s in dir(DefaultTemplateFunctions)
    if s.startswith(DefaultTemplateFunctions.prefix)
]
