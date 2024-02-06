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


import tmep

values = {
    "prename": "Franz",
    "lastname": "Schubert",
    "lol": "lol",
    "troll": "troll",
    "genres": "Pop; Rock; Classical Crossover",
    "asciify": "gennemgår",
    "track": 7,
}


def assert_parsing(a: str, b: str) -> None:
    assert tmep.parse(a, values) == b


class TestAlpha:
    def test_literal(self) -> None:
        assert_parsing("%alpha{a1b23c}", "a b c")

    def test_symbol(self) -> None:
        assert_parsing("%alpha{$genres}", "Pop Rock Classical Crossover")


class TestAlphanum:
    def test_accent(self) -> None:
        assert_parsing("%alphanum{après-évêque1}", "apres eveque1")

    def test_genres(self) -> None:
        assert_parsing("%alphanum{$genres}", "Pop Rock Classical Crossover")

    def test_many(self) -> None:
        assert_parsing('%alphanum{a"&(&b}', "a b")


class TestAsciify:
    def test_literal(self) -> None:
        assert_parsing("%asciify{après évêque}", "apres eveque")

    def test_variable(self) -> None:
        assert_parsing("%asciify{$asciify}", "gennemgar")

    def test_foreign(self) -> None:
        assert_parsing("%asciify{Новыя старонкі}", "Novyia staronki")

    def test_german_umlaute(self) -> None:
        assert_parsing("%asciify{äÄöÖüÜ}", "aeAeoeOeueUe")

    def test_symbols_single(self) -> None:
        assert_parsing("%asciify{⚓}", "")

    def test_symbols_multiple(self) -> None:
        assert_parsing("%asciify{⚢⚣⚤⚥⚦⚧⚨⚩}", "")

    def test_symbols_mixed(self) -> None:
        assert_parsing("%asciify{a⚢b⚣⚤c}", "abc")


class TestDelchars:
    def test_single(self) -> None:
        assert_parsing("%delchars{x-x,-}", "xx")

    def test_multiple(self) -> None:
        assert_parsing("%delchars{x---x,-}", "xx")

    def test_no_match(self) -> None:
        assert_parsing("%delchars{x-x,_}", "x-x")

    def test_multiple_chars(self) -> None:
        assert_parsing("%delchars{x_-.x,_-.}", "xx")

    def test_unicode(self) -> None:
        assert_parsing("%delchars{öd,ö}", "d")

    def test_variable(self) -> None:
        assert_parsing("%delchars{$lastname, ue}", "Schbrt")


class TestDeldupchars:
    def test_default(self) -> None:
        assert_parsing("%deldupchars{a---b___c...d}", "a-b_c.d")

    def test_custom(self) -> None:
        assert_parsing("%deldupchars{a---b___c, -}", "a-b___c")

    def test_whitespace(self) -> None:
        assert_parsing("%deldupchars{a   a, }", "a a")


class TestFirst:
    def test_symbol(self):
        assert_parsing("%first{$genres}", "Pop")

    def test_first_skip(self):
        assert_parsing("%first{$genres,1,2}", "Classical Crossover")

    def test_first_different_sep(self):
        assert_parsing("%first{Alice / Bob / Eve,2,0, / , & }", "Alice & Bob")


class TestFunctions:
    def setup_method(self):
        self.values = {
            "prename": "Franz",
            "lastname": "Schubert",
            "lol": "lol",
            "troll": "troll",
            "genres": "Pop; Rock; Classical Crossover",
            "asciify": "gennemgår",
            "track": 7,
        }

    def assert_parsing(self, a: str, b: str):
        assert tmep.parse(a, self.values) == b

    # if
    def test_if_false(self):
        self.assert_parsing("x%if{,foo}", "x")

    def test_if_false_value(self):
        self.assert_parsing("x%if{false,foo}", "x")

    def test_if_true(self):
        self.assert_parsing("%if{bar,foo}", "foo")

    def test_if_else_false(self):
        self.assert_parsing("%if{,foo,baz}", "baz")

    def test_if_else_false_value(self):
        self.assert_parsing("%if{false,foo,baz}", "baz")

    def test_if_int_value(self):
        self.assert_parsing("%if{0,foo,baz}", "baz")

    # ifdef
    def test_if_def_field_return_self(self):
        self.assert_parsing("%ifdef{lastname}", "")

    def test_if_def_field_not_defined(self):
        self.assert_parsing("%ifdef{bar}", "")

    def test_if_def_true(self):
        self.assert_parsing("%ifdef{lastname,Its true}", "Its true")

    def test_if_def_true_complete(self):
        self.assert_parsing("%ifdef{lastname,lol,troll}", "lol")

    def test_if_def_false_complete(self):
        self.assert_parsing("%ifdef{trill,lol,troll}", "troll")

    # initial
    def test_initial_use_first_character(self):
        self.assert_parsing("%initial{abc}", "a")

    def test_initial_german_umlaut(self):
        self.assert_parsing("%initial{ä}", "a")

    def test_initial_special_characters(self):
        self.assert_parsing("%initial{-a-}", "a")

    def test_initial_nothing(self):
        self.assert_parsing("%initial{}", "_")

    def test_initial_number(self):
        self.assert_parsing("%initial{3}", "0")

    def test_initial_lower(self):
        self.assert_parsing("%initial{A}", "a")

    # left
    def test_left_literal(self):
        self.assert_parsing("%left{Schubert, 3}", "Sch")

    def test_left_variable(self):
        self.assert_parsing("%left{$lastname, 3}", "Sch")

    # lower
    def test_lower_literal(self):
        self.assert_parsing("%lower{SCHUBERT}", "schubert")

    def test_lower_variable(self):
        self.assert_parsing("%lower{$lastname}", "schubert")

    # nowhitespace
    def test_nowhitespace(self):
        self.assert_parsing("%nowhitespace{$genres}", "Pop;-Rock;-Classical-Crossover")

    def test_nowhitespace_inline(self):
        self.assert_parsing("%nowhitespace{a b}", "a-b")

    def test_nowhitespace_multiple(self):
        self.assert_parsing("%nowhitespace{a   b}", "a-b")

    def test_nowhitespace_newline_tab(self):
        self.assert_parsing("%nowhitespace{a\n\tb}", "a-b")

    def test_nowhitespace_replace_character(self):
        self.assert_parsing("%nowhitespace{a b,_}", "a_b")

    def test_nowhitespace_delete(self):
        self.assert_parsing("%nowhitespace{a b,}", "ab")

    # num
    def test_num_literal(self):
        self.assert_parsing("%num{7,3}", "007")

    def test_num_variable(self):
        self.assert_parsing("%num{$track,3}", "007")

    def test_num_default_count(self):
        self.assert_parsing("%num{7}", "07")

    def test_num_default_variable(self):
        self.assert_parsing("%num{$track}", "07")

    # replchars
    def test_replchars_literal(self):
        self.assert_parsing("%replchars{Schubert,-,ue}", "Sch-b-rt")

    def test_replchars_variable(self):
        self.assert_parsing("%replchars{$lastname,-,ue}", "Sch-b-rt")

    # right
    def test_right_literal(self):
        self.assert_parsing("%right{Schubert,3}", "ert")

    def test_right_variable(self):
        self.assert_parsing("%right{$lastname,3}", "ert")

    # sanitize
    def test_sanitize_literal(self):
        self.assert_parsing("%sanitize{x:*?<>|/~&x}", "xx")

    # shorten
    def test_shorten_literal(self):
        self.assert_parsing("%shorten{Lorem ipsum dolor sit, 10}", "Lorem")

    def test_shorten_default(self):
        self.assert_parsing(
            "%shorten{Lorem ipsum dolor sit amet consectetur adipisicing}",
            "Lorem ipsum dolor sit amet",
        )

    # title
    def test_title_literal(self):
        self.assert_parsing("%title{franz schubert}", "Franz Schubert")

    def test_title_variable(self):
        self.assert_parsing("%title{$lol $troll}", "Lol Troll")

    # upper
    def test_upper_literal(self):
        self.assert_parsing("%upper{foo}", "FOO")

    def test_upper_variable(self):
        self.assert_parsing("%upper{$prename}", "FRANZ")

    #
    def test_nonexistent_function(self):
        self.assert_parsing("%foo{bar}", "%foo{bar}")


class TestFunctionIfDefEmpty:
    def setup_method(self):
        self.values = {
            "empty_string": "",
            "false": False,
            "non_empty_string": "test",
            "none": None,
            "only_whitespaces": " \t\n",
        }

    def assert_parsing(self, a: str, b: str):
        assert tmep.parse(a, self.values) == b

    # empty_string
    def test_empty_string(self):
        self.assert_parsing("%ifdefempty{empty_string,trueval}", "trueval")

    # false
    def test_false(self):
        self.assert_parsing("%ifdefempty{false,trueval}", "trueval")

    # non_empty_string
    def test_non_empty_string(self):
        self.assert_parsing(
            "%ifdefempty{non_empty_string,trueval,falseval}", "falseval"
        )

    # nonexistent
    def test_nonexistent(self):
        self.assert_parsing("%ifdefempty{nonexistent,trueval,falseval}", "trueval")

    # none
    def test_none(self):
        self.assert_parsing("%ifdefempty{none,trueval}", "trueval")

    # nonexistent
    def test_only_whitespaces(self):
        self.assert_parsing("%ifdefempty{only_whitespaces,trueval,falseval}", "trueval")


class TestFunctionIfDefNotEmpty:
    def setup_method(self):
        self.values = {
            "empty_string": "",
            "false": False,
            "non_empty_string": "test",
            "none": None,
            "only_whitespaces": " \t\n",
        }

    def assert_parsing(self, a: str, b: str):
        assert tmep.parse(a, self.values) == b

    # empty_string
    def test_empty_string(self):
        self.assert_parsing("%ifdefnotempty{empty_string,trueval,falseval}", "falseval")

    # false
    def test_false(self):
        self.assert_parsing("%ifdefnotempty{false,trueval,falseval}", "falseval")

    # non_empty_string
    def test_non_empty_string(self):
        self.assert_parsing(
            "%ifdefnotempty{non_empty_string,trueval,falseval}", "trueval"
        )

    # nonexistent
    def test_nonexistent(self):
        self.assert_parsing("%ifdefnotempty{nonexistent,trueval,falseval}", "falseval")

    # none
    def test_none(self):
        self.assert_parsing("%ifdefnotempty{none,trueval,falseval}", "falseval")

    # nonexistent
    def test_only_whitespaces(self):
        self.assert_parsing(
            "%ifdefnotempty{only_whitespaces,trueval,falseval}", "falseval"
        )
