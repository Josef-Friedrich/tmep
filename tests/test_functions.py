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

# https://github.com/beetbox/beets/blob/master/test/test_library.py

from __future__ import annotations

import tmep

values = {
    "prename": "Franz",
    "lastname": "Schubert",
    "var1": "var1",
    "var2": "var2",
    "genres": "Pop; Rock; Classical Crossover",
    "asciify": "gennemgår",
    "track": 7,
}


def check(a: str, b: str) -> None:
    assert tmep.parse(a, values) == b


class TestAlpha:
    def test_literal(self) -> None:
        check("%alpha{a1b23c}", "a b c")

    def test_symbol(self) -> None:
        check("%alpha{$genres}", "Pop Rock Classical Crossover")


class TestAlphanum:
    def test_accent(self) -> None:
        check("%alphanum{après-évêque1}", "apres eveque1")

    def test_genres(self) -> None:
        check("%alphanum{$genres}", "Pop Rock Classical Crossover")

    def test_many(self) -> None:
        check('%alphanum{a"&(&b}', "a b")


class TestAsciify:
    def test_literal(self) -> None:
        check("%asciify{après évêque}", "apres eveque")

    def test_variable(self) -> None:
        check("%asciify{$asciify}", "gennemgar")

    def test_foreign(self) -> None:
        check("%asciify{Новыя старонкі}", "Novyia staronki")

    def test_german_umlaute(self) -> None:
        check("%asciify{äÄöÖüÜ}", "aeAeoeOeueUe")

    def test_symbols_single(self) -> None:
        check("%asciify{⚓}", "")

    def test_symbols_multiple(self) -> None:
        check("%asciify{⚢⚣⚤⚥⚦⚧⚨⚩}", "")

    def test_symbols_mixed(self) -> None:
        check("%asciify{a⚢b⚣⚤c}", "abc")


class TestDelchars:
    def test_single(self) -> None:
        check("%delchars{x-x,-}", "xx")

    def test_multiple(self) -> None:
        check("%delchars{x---x,-}", "xx")

    def test_no_match(self) -> None:
        check("%delchars{x-x,_}", "x-x")

    def test_multiple_chars(self) -> None:
        check("%delchars{x_-.x,_-.}", "xx")

    def test_unicode(self) -> None:
        check("%delchars{öd,ö}", "d")

    def test_variable(self) -> None:
        check("%delchars{$lastname, ue}", "Schbrt")


class TestDeldupchars:
    def test_default(self) -> None:
        check("%deldupchars{a---b___c...d}", "a-b_c.d")

    def test_custom(self) -> None:
        check("%deldupchars{a---b___c, -}", "a-b___c")

    def test_whitespace(self) -> None:
        check("%deldupchars{a   a, }", "a a")


class TestFirst:
    def test_symbol(self) -> None:
        check("%first{$genres}", "Pop")

    def test_first_skip(self) -> None:
        check("%first{$genres,1,2}", "Classical Crossover")

    def test_first_different_sep(self) -> None:
        check("%first{Alice / Bob / Eve,2,0, / , & }", "Alice & Bob")


class TestIf:
    def test_false(self) -> None:
        check("x%if{,foo}", "x")

    def test_false_value(self) -> None:
        check("x%if{false,foo}", "x")

    def test_true(self) -> None:
        check("%if{bar,foo}", "foo")

    def test_else_false(self) -> None:
        check("%if{,foo,baz}", "baz")

    def test_else_false_value(self) -> None:
        check("%if{false,foo,baz}", "baz")

    def test_int_value(self) -> None:
        check("%if{0,foo,baz}", "baz")


class TestIfDef:
    def test_field_return_self(self) -> None:
        check("%ifdef{lastname}", "")

    def test_field_not_defined(self) -> None:
        check("%ifdef{bar}", "")

    def test_true(self) -> None:
        check("%ifdef{lastname,Its true}", "Its true")

    def test_true_complete(self) -> None:
        check("%ifdef{lastname,var1,var2}", "var1")

    def test_false_complete(self) -> None:
        check("%ifdef{trill,var1,var2}", "var2")


class TestBase:
    def setup_method(self) -> None:
        self.values = {
            "empty_string": "",
            "false": False,
            "non_empty_string": "test",
            "none": None,
            "only_whitespaces": " \t\n",
        }

    def check(self, a: str, b: str) -> None:
        assert tmep.parse(a, self.values) == b


class TestIfDefEmpty(TestBase):
    def test_empty_string(self) -> None:
        check("%ifdefempty{empty_string,trueval}", "trueval")

    def test_false(self) -> None:
        self.check("%ifdefempty{false,trueval}", "trueval")

    def test_non_empty_string(self) -> None:
        self.check("%ifdefempty{non_empty_string,trueval,falseval}", "falseval")

    def test_nonexistent(self) -> None:
        self.check("%ifdefempty{nonexistent,trueval,falseval}", "trueval")

    def test_none(self) -> None:
        self.check("%ifdefempty{none,trueval}", "trueval")

    def test_only_whitespaces(self) -> None:
        self.check("%ifdefempty{only_whitespaces,trueval,falseval}", "trueval")


class TestIfDefNotEmpty(TestBase):
    def test_empty_string(self) -> None:
        self.check("%ifdefnotempty{empty_string,trueval,falseval}", "falseval")

    def test_false(self) -> None:
        self.check("%ifdefnotempty{false,trueval,falseval}", "falseval")

    def test_non_empty_string(self) -> None:
        self.check("%ifdefnotempty{non_empty_string,trueval,falseval}", "trueval")

    def test_nonexistent(self) -> None:
        self.check("%ifdefnotempty{nonexistent,trueval,falseval}", "falseval")

    def test_none(self) -> None:
        self.check("%ifdefnotempty{none,trueval,falseval}", "falseval")

    def test_only_whitespaces(self) -> None:
        self.check("%ifdefnotempty{only_whitespaces,trueval,falseval}", "falseval")


class TestInitial:
    def test_example(self) -> None:
        check("%initial{Schubert}", "s")

    def test_use_first_character(self) -> None:
        check("%initial{abc}", "a")

    def test_german_umlaut(self) -> None:
        check("%initial{ä}", "a")

    def test_special_characters(self) -> None:
        check("%initial{-a-}", "a")

    def test_nothing(self) -> None:
        check("%initial{}", "_")

    def test_number(self) -> None:
        check("%initial{3}", "0")

    def test_lower(self) -> None:
        check("%initial{A}", "a")


class TestLeft:
    def test_literal(self) -> None:
        check("%left{Schubert, 3}", "Sch")

    def test_variable(self) -> None:
        check("%left{$lastname, 3}", "Sch")


class TestLower:
    def test_literal(self) -> None:
        check("%lower{SCHUBERT}", "schubert")

    def test_variable(self) -> None:
        check("%lower{$lastname}", "schubert")


class TestNowhitespace:
    def test_variable(self) -> None:
        check("%nowhitespace{$genres}", "Pop;-Rock;-Classical-Crossover")

    def test_inline(self) -> None:
        check("%nowhitespace{a b}", "a-b")

    def test_multiple(self) -> None:
        check("%nowhitespace{a   b}", "a-b")

    def test_newline_tab(self) -> None:
        check("%nowhitespace{a\n\tb}", "a-b")

    def test_replace_character(self) -> None:
        check("%nowhitespace{a b,_}", "a_b")

    def test_delete(self) -> None:
        check("%nowhitespace{a b,}", "ab")


class TestNum:
    def test_literal(self) -> None:
        check("%num{7,3}", "007")

    def test_variable(self) -> None:
        check("%num{$track,3}", "007")

    def test_default_count(self) -> None:
        check("%num{7}", "07")

    def test_default_variable(self) -> None:
        check("%num{$track}", "07")


class TestReplchars:
    def test_literal(self) -> None:
        check("%replchars{Schubert,-,ue}", "Sch-b-rt")

    def test_example(self) -> None:
        check("%replchars{text,-,xe}", "t--t")

    def test_variable(self) -> None:
        check("%replchars{$lastname,-,ue}", "Sch-b-rt")


class TestRight:
    def test_literal(self) -> None:
        check("%right{Schubert,3}", "ert")

    def test_variable(self) -> None:
        check("%right{$lastname,3}", "ert")


def test_sanitize() -> None:
    check("%sanitize{x:*?<>|/~&x}", "xx")


class TestShorten:
    def test_literal(self) -> None:
        check("%shorten{Lorem ipsum dolor sit, 10}", "Lorem")

    def test_default(self) -> None:
        check(
            "%shorten{Lorem ipsum dolor sit amet consectetur adipisicing}",
            "Lorem ipsum dolor sit amet",
        )


def test_time() -> None:
    check("%time{30 Nov 2024,%Y,%d %b %Y}", "2024")


class TestTitle:
    def test_literal(self) -> None:
        check("%title{franz schubert}", "Franz Schubert")

    def test_variable(self) -> None:
        check("%title{$var1 $var2}", "Var1 Var2")


class TestUpper:
    def test_literal(self) -> None:
        check("%upper{foo}", "FOO")

    def test_variable(self) -> None:
        check("%upper{$prename}", "FRANZ")


def test_nonexistent_function() -> None:
    check("%foo{bar}", "%foo{bar}")
