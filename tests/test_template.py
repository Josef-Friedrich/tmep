# This file is part of beets.
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

# https://raw.githubusercontent.com/beetbox/beets/master/test/test_template.py

"""Tests for template engine."""

from __future__ import annotations

from typing import Any, Generator

from tmep import template as functemplate
from tmep.template import Call, Expression, Symbol
from tmep.types import FunctionCollection


def _normexpr(expr: Expression) -> Generator[str | Symbol | Call, Any, None]:
    """Normalize an Expression object's parts, collapsing multiple
    adjacent text blocks and removing empty text blocks. Generates a
    sequence of parts.
    """
    textbuf: list[str] = []
    for part in expr.parts:
        if isinstance(part, str):
            textbuf.append(part)
        else:
            if textbuf:
                text = "".join(textbuf)
                if text:
                    yield text
                    textbuf = []
            yield part
    if textbuf:
        text = "".join(textbuf)
        if text:
            yield text


def _normparse(text: str) -> Generator[str | Symbol | Call, Any, None]:
    """Parse a template and then normalize the resulting Expression."""
    return _normexpr(functemplate._parse(text))


class TestParse:
    def test_empty_string(self) -> None:
        assert list(_normparse("")) == []

    def _assert_symbol(self, obj: str | Symbol | Call, ident: str) -> None:
        """Assert that an object is a Symbol with the given identifier."""
        assert isinstance(obj, functemplate.Symbol), "not a Symbol: %s" % repr(obj)
        assert obj.ident == ident, "wrong identifier: %s vs. %s" % (
            repr(obj.ident),
            repr(ident),
        )

    def _assert_call(self, obj: str | Symbol | Call, ident: str, numargs: int) -> None:
        """Assert that an object is a Call with the given identifier and
        argument count.
        """
        assert isinstance(obj, functemplate.Call), "not a Call: %s" % repr(obj)
        assert obj.ident == ident, "wrong identifier: %s vs. %s" % (
            repr(obj.ident),
            repr(ident),
        )
        assert len(obj.args) == numargs, "wrong argument count in %s: %i vs. %i" % (
            repr(obj.ident),
            len(obj.args),
            numargs,
        )

    def test_plain_text(self) -> None:
        assert list(_normparse("hello world")) == ["hello world"]

    def test_escaped_character_only(self) -> None:
        assert list(_normparse("$$")) == ["$"]

    def test_escaped_character_in_text(self) -> None:
        assert list(_normparse("a $$ b")) == ["a $ b"]

    def test_escaped_character_at_start(self) -> None:
        assert list(_normparse("$$ hello")) == ["$ hello"]

    def test_escaped_character_at_end(self) -> None:
        assert list(_normparse("hello $$")) == ["hello $"]

    def test_escaped_function_delim(self) -> None:
        assert list(_normparse("a $% b")) == ["a % b"]

    def test_escaped_sep(self) -> None:
        assert list(_normparse("a $, b")) == ["a , b"]

    def test_escaped_close_brace(self) -> None:
        assert list(_normparse("a $} b")) == ["a } b"]

    def test_bare_value_delim_kept_intact(self) -> None:
        assert list(_normparse("a $ b")) == ["a $ b"]

    def test_bare_function_delim_kept_intact(self) -> None:
        assert list(_normparse("a % b")) == ["a % b"]

    def test_bare_opener_kept_intact(self) -> None:
        assert list(_normparse("a { b")) == ["a { b"]

    def test_bare_closer_kept_intact(self) -> None:
        assert list(_normparse("a } b")) == ["a } b"]

    def test_bare_sep_kept_intact(self) -> None:
        assert list(_normparse("a , b")) == ["a , b"]

    def test_symbol_alone(self) -> None:
        parts = list(_normparse("$foo"))
        assert len(parts) == 1
        self._assert_symbol(parts[0], "foo")

    def test_symbol_in_text(self) -> None:
        parts = list(_normparse("hello $foo world"))
        assert len(parts) == 3
        assert parts[0] == "hello "
        self._assert_symbol(parts[1], "foo")
        assert parts[2] == " world"

    def test_symbol_with_braces(self) -> None:
        parts = list(_normparse("hello${foo}world"))
        assert len(parts) == 3
        assert parts[0] == "hello"
        self._assert_symbol(parts[1], "foo")
        assert parts[2] == "world"

    def test_unclosed_braces_symbol(self) -> None:
        assert list(_normparse("a ${ b")) == ["a ${ b"]

    def test_empty_braces_symbol(self) -> None:
        assert list(_normparse("a ${} b")) == ["a ${} b"]

    def test_call_without_args_at_end(self) -> None:
        assert list(_normparse("foo %bar")) == ["foo %bar"]

    def test_call_without_args(self) -> None:
        assert list(_normparse("foo %bar baz")) == ["foo %bar baz"]

    def test_call_with_unclosed_args(self) -> None:
        assert list(_normparse("foo %bar{ baz")) == ["foo %bar{ baz"]

    def test_call_with_unclosed_multiple_args(self) -> None:
        assert list(_normparse("foo %bar{bar,bar baz")) == ["foo %bar{bar,bar baz"]

    def test_call_empty_arg(self) -> None:
        parts = list(_normparse("%foo{}"))
        assert len(parts) == 1
        self._assert_call(parts[0], "foo", 1)
        assert isinstance(parts[0], Call)
        assert list(_normexpr(parts[0].args[0])) == []

    def test_call_single_arg(self) -> None:
        parts = list(_normparse("%foo{bar}"))
        assert len(parts) == 1
        self._assert_call(parts[0], "foo", 1)
        assert isinstance(parts[0], Call)
        assert list(_normexpr(parts[0].args[0])) == ["bar"]

    def test_call_two_args(self) -> None:
        parts = list(_normparse("%foo{bar,baz}"))
        assert len(parts) == 1
        self._assert_call(parts[0], "foo", 2)
        assert isinstance(parts[0], Call)
        assert list(_normexpr(parts[0].args[0])) == ["bar"]
        assert list(_normexpr(parts[0].args[1])) == ["baz"]

    def test_call_with_escaped_sep(self) -> None:
        parts = list(_normparse("%foo{bar$,baz}"))
        assert len(parts) == 1
        self._assert_call(parts[0], "foo", 1)
        assert isinstance(parts[0], Call)
        assert list(_normexpr(parts[0].args[0])) == ["bar,baz"]

    def test_call_with_escaped_close(self) -> None:
        parts = list(_normparse("%foo{bar$}baz}"))
        assert len(parts) == 1
        self._assert_call(parts[0], "foo", 1)
        assert isinstance(parts[0], Call)
        assert list(_normexpr(parts[0].args[0])) == ["bar}baz"]

    def test_call_with_symbol_argument(self) -> None:
        parts = list(_normparse("%foo{$bar,baz}"))
        assert len(parts) == 1
        self._assert_call(parts[0], "foo", 2)
        assert isinstance(parts[0], Call)
        arg_parts = list(_normexpr(parts[0].args[0]))
        assert len(arg_parts) == 1
        self._assert_symbol(arg_parts[0], "bar")
        assert list(_normexpr(parts[0].args[1])) == ["baz"]

    def test_call_with_nested_call_argument(self) -> None:
        parts = list(_normparse("%foo{%bar{},baz}"))
        assert len(parts) == 1
        self._assert_call(parts[0], "foo", 2)
        assert isinstance(parts[0], Call)
        arg_parts = list(_normexpr(parts[0].args[0]))
        assert len(arg_parts) == 1
        self._assert_call(arg_parts[0], "bar", 1)
        assert list(_normexpr(parts[0].args[1])) == ["baz"]

    def test_nested_call_with_argument(self) -> None:
        parts = list(_normparse("%foo{%bar{baz}}"))
        assert len(parts) == 1
        self._assert_call(parts[0], "foo", 1)
        assert isinstance(parts[0], Call)
        arg_parts = list(_normexpr(parts[0].args[0]))
        assert len(arg_parts) == 1
        self._assert_call(arg_parts[0], "bar", 1)
        assert isinstance(arg_parts[0], Call)
        assert list(_normexpr(arg_parts[0].args[0])) == ["baz"]

    def test_sep_before_call_two_args(self) -> None:
        parts = list(_normparse("hello, %foo{bar,baz}"))
        assert len(parts) == 2
        assert parts[0] == "hello, "
        self._assert_call(parts[1], "foo", 2)
        assert isinstance(parts[1], Call)
        assert list(_normexpr(parts[1].args[0])) == ["bar"]
        assert list(_normexpr(parts[1].args[1])) == ["baz"]

    def test_sep_with_symbols(self) -> None:
        parts = list(_normparse("hello,$foo,$bar"))
        assert len(parts) == 4
        assert parts[0] == "hello,"
        self._assert_symbol(parts[1], "foo")
        assert parts[2] == ","
        self._assert_symbol(parts[3], "bar")

    def test_newline_at_end(self) -> None:
        parts = list(_normparse("foo\n"))
        assert len(parts) == 1
        assert parts[0] == "foo\n"


class TestEval:
    def _eval(self, template: str):
        values = {
            "foo": "bar",
            "baz": "BaR",
        }
        functions: FunctionCollection = {
            "lower": str.lower,
            "len": len,
        }
        return functemplate.Template(template).substitute(values, functions)

    def test_plain_text(self) -> None:
        assert self._eval("foo") == "foo"

    def test_subtitute_value(self) -> None:
        assert self._eval("$foo") == "bar"

    def test_subtitute_value_in_text(self) -> None:
        assert self._eval("hello $foo world") == "hello bar world"

    def test_not_subtitute_undefined_value(self) -> None:
        assert self._eval("$bar") == "$bar"

    def test_function_call(self) -> None:
        assert self._eval("%lower{FOO}") == "foo"

    def test_function_call_with_text(self) -> None:
        assert self._eval("A %lower{FOO} B") == "A foo B"

    def test_nested_function_call(self) -> None:
        assert self._eval("%lower{%lower{FOO}}") == "foo"

    def test_symbol_in_argument(self) -> None:
        assert self._eval("%lower{$baz}") == "bar"

    def test_function_call_exception(self) -> None:
        res = self._eval("%lower{a,b,c,d,e}")
        assert isinstance(res, str)

    def test_function_returning_integer(self) -> None:
        assert self._eval("%len{foo}") == "3"

    def test_not_subtitute_undefined_func(self) -> None:
        assert self._eval("%bar{}") == "%bar{}"

    def test_not_subtitute_func_with_no_args(self) -> None:
        assert self._eval("%lower") == "%lower"

    def test_function_call_with_empty_arg(self) -> None:
        assert self._eval("%len{}") == "0"
