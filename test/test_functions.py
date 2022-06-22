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

import unittest
import tmep


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.values = {
            'prename': 'Franz',
            'lastname': 'Schubert',
            'lol': 'lol',
            'troll': 'troll',
            'genres': 'Pop; Rock; Classical Crossover',
            'asciify': 'gennemgår',
            'track': 7,
        }

    def parseEqual(self, a: str, b: str):
        self.assertEqual(tmep.parse(a, self.values), b)

    # alphanum
    def test_alpha(self):
        self.parseEqual('%alpha{abc123}', 'abc ')

    def test_alpha_genres(self):
        self.parseEqual('%alpha{$genres}', 'Pop Rock Classical Crossover')

    # alphanum
    def test_alphanum_accent(self):
        self.parseEqual('%alphanum{après-évêque}', 'apres eveque')

    def test_alphanum_genres(self):
        self.parseEqual('%alphanum{$genres}', 'Pop Rock Classical Crossover')

    def test_alphanum_many(self):
        self.parseEqual('%alphanum{a"&(&b}', 'a b')

    # asciify
    def test_asciify_literal(self):
        self.parseEqual('%asciify{après évêque}', 'apres eveque')

    def test_asciify_variable(self):
        self.parseEqual('%asciify{$asciify}', 'gennemgar')

    def test_asciify_foreign(self):
        self.parseEqual('%asciify{Новыя старонкі}', 'Novyia staronki')

    def test_asciify_german_umlaute(self):
        self.parseEqual('%asciify{äÄöÖüÜ}', 'aeAeoeOeueUe')

    def test_asciify_symbols_single(self):
        self.parseEqual('%asciify{⚓}', '')

    def test_asciify_symbols_multiple(self):
        self.parseEqual('%asciify{⚢⚣⚤⚥⚦⚧⚨⚩}', '')

    def test_asciify_symbols_mixed(self):
        self.parseEqual('%asciify{a⚢b⚣⚤c}', 'abc')

    # delchars
    def test_delchars_single(self):
        self.parseEqual('%delchars{x-x,-}', 'xx')

    def test_delchars_multiple(self):
        self.parseEqual('%delchars{x---x,-}', 'xx')

    def test_delchars_no_match(self):
        self.parseEqual('%delchars{x-x,_}', 'x-x')

    def test_delchars_multiple_chars(self):
        self.parseEqual('%delchars{x_-.x,_-.}', 'xx')

    def test_delchars_unicode(self):
        self.parseEqual('%delchars{öd,ö}', 'd')

    def test_delchars_variable(self):
        self.parseEqual('%delchars{$lastname,ue}', 'Schbrt')

    # deldupchars
    def test_deldupchars_default(self):
        self.parseEqual('%deldupchars{a---b___c...d}', 'a-b_c.d')

    def test_deldupchars_custom(self):
        self.parseEqual('%deldupchars{a---b___c,-}', 'a-b___c')

    def test_deldupchars_whitespace(self):
        self.parseEqual('%deldupchars{a   a, }', 'a a')

    # first
    def test_first(self):
        self.parseEqual('%first{$genres}', 'Pop')

    def test_first_skip(self):
        self.parseEqual('%first{$genres,1,2}', 'Classical Crossover')

    def test_first_different_sep(self):
        self.parseEqual(
            '%first{Alice / Bob / Eve,2,0, / , & }',
            'Alice & Bob'
        )

    # if
    def test_if_false(self):
        self.parseEqual('x%if{,foo}', 'x')

    def test_if_false_value(self):
        self.parseEqual('x%if{false,foo}', 'x')

    def test_if_true(self):
        self.parseEqual('%if{bar,foo}', 'foo')

    def test_if_else_false(self):
        self.parseEqual('%if{,foo,baz}', 'baz')

    def test_if_else_false_value(self):
        self.parseEqual('%if{false,foo,baz}', 'baz')

    def test_if_int_value(self):
        self.parseEqual('%if{0,foo,baz}', 'baz')

    # ifdef
    def test_if_def_field_return_self(self):
        self.parseEqual('%ifdef{lastname}', '')

    def test_if_def_field_not_defined(self):
        self.parseEqual('%ifdef{bar}', '')

    def test_if_def_true(self):
        self.parseEqual('%ifdef{lastname,Its true}', 'Its true')

    def test_if_def_true_complete(self):
        self.parseEqual('%ifdef{lastname,lol,troll}', 'lol')

    def test_if_def_false_complete(self):
        self.parseEqual('%ifdef{trill,lol,troll}', 'troll')

    # initial
    def test_initial_use_first_character(self):
        self.parseEqual('%initial{abc}', 'a')

    def test_initial_german_umlaut(self):
        self.parseEqual('%initial{ä}', 'a')

    def test_initial_special_characters(self):
        self.parseEqual('%initial{-a-}', 'a')

    def test_initial_nothing(self):
        self.parseEqual('%initial{}', '_')

    def test_initial_number(self):
        self.parseEqual('%initial{3}', '0')

    def test_initial_lower(self):
        self.parseEqual('%initial{A}', 'a')

    # left
    def test_left_literal(self):
        self.parseEqual('%left{Schubert, 3}', 'Sch')

    def test_left_variable(self):
        self.parseEqual('%left{$lastname, 3}', 'Sch')

    # lower
    def test_lower_literal(self):
        self.parseEqual('%lower{SCHUBERT}', 'schubert')

    def test_lower_variable(self):
        self.parseEqual('%lower{$lastname}', 'schubert')

    # nowhitespace
    def test_nowhitespace(self):
        self.parseEqual('%nowhitespace{$genres}',
                        'Pop;-Rock;-Classical-Crossover')

    def test_nowhitespace_inline(self):
        self.parseEqual('%nowhitespace{a b}', 'a-b')

    def test_nowhitespace_multiple(self):
        self.parseEqual('%nowhitespace{a   b}', 'a-b')

    def test_nowhitespace_newline_tab(self):
        self.parseEqual('%nowhitespace{a\n\tb}', 'a-b')

    def test_nowhitespace_replace_character(self):
        self.parseEqual('%nowhitespace{a b,_}', 'a_b')

    def test_nowhitespace_delete(self):
        self.parseEqual('%nowhitespace{a b,}', 'ab')

    # num
    def test_num_literal(self):
        self.parseEqual('%num{7,3}', '007')

    def test_num_variable(self):
        self.parseEqual('%num{$track,3}', '007')

    def test_num_default_count(self):
        self.parseEqual('%num{7}', '07')

    def test_num_default_variable(self):
        self.parseEqual('%num{$track}', '07')

    # replchars
    def test_replchars_literal(self):
        self.parseEqual('%replchars{Schubert,-,ue}', 'Sch-b-rt')

    def test_replchars_variable(self):
        self.parseEqual('%replchars{$lastname,-,ue}', 'Sch-b-rt')

    # right
    def test_right_literal(self):
        self.parseEqual('%right{Schubert,3}', 'ert')

    def test_right_variable(self):
        self.parseEqual('%right{$lastname,3}', 'ert')

    # sanitize
    def test_sanitize_literal(self):
        self.parseEqual('%sanitize{x:*?<>|\/~&x}', 'xx')  # noqa: W605

    # shorten
    def test_shorten_literal(self):
        self.parseEqual('%shorten{Lorem ipsum dolor sit,10}', 'Lorem')

    def test_shorten_default(self):
        self.parseEqual(
            '%shorten{Lorem ipsum dolor sit amet consectetur adipisicing}',
            'Lorem ipsum dolor sit amet')

    # title
    def test_title_literal(self):
        self.parseEqual('%title{franz schubert}', 'Franz Schubert')

    def test_title_variable(self):
        self.parseEqual('%title{$lol $troll}', 'Lol Troll')

    # upper
    def test_upper_literal(self):
        self.parseEqual('%upper{foo}', 'FOO')

    def test_upper_variable(self):
        self.parseEqual('%upper{$prename}', 'FRANZ')

    #
    def test_nonexistent_function(self):
        self.parseEqual('%foo{bar}', '%foo{bar}')


class TestFunctionIfDefEmpty(unittest.TestCase):

    def setUp(self):
        self.values = {
            'empty_string': '',
            'false': False,
            'non_empty_string': 'test',
            'none': None,
            'only_whitespaces': ' \t\n',
        }

    def parseEqual(self, a: str, b: str):
        self.assertEqual(tmep.parse(a, self.values), b)

    # empty_string
    def test_empty_string(self):
        self.parseEqual('%ifdefempty{empty_string,trueval}', 'trueval')

    # false
    def test_false(self):
        self.parseEqual('%ifdefempty{false,trueval}', 'trueval')

    # non_empty_string
    def test_non_empty_string(self):
        self.parseEqual('%ifdefempty{non_empty_string,trueval,falseval}',
                        'falseval')

    # nonexistent
    def test_nonexistent(self):
        self.parseEqual('%ifdefempty{nonexistent,trueval,falseval}',
                        'trueval')

    # none
    def test_none(self):
        self.parseEqual('%ifdefempty{none,trueval}', 'trueval')

    # nonexistent
    def test_only_whitespaces(self):
        self.parseEqual('%ifdefempty{only_whitespaces,trueval,falseval}',
                        'trueval')


class TestFunctionIfDefNotEmpty(unittest.TestCase):

    def setUp(self):
        self.values = {
            'empty_string': '',
            'false': False,
            'non_empty_string': 'test',
            'none': None,
            'only_whitespaces': ' \t\n',
        }

    def parseEqual(self, a: str, b: str):
        self.assertEqual(tmep.parse(a, self.values), b)

    # empty_string
    def test_empty_string(self):
        self.parseEqual('%ifdefnotempty{empty_string,trueval,falseval}',
                        'falseval')

    # false
    def test_false(self):
        self.parseEqual('%ifdefnotempty{false,trueval,falseval}',
                        'falseval')

    # non_empty_string
    def test_non_empty_string(self):
        self.parseEqual('%ifdefnotempty{non_empty_string,trueval,falseval}',
                        'trueval')

    # nonexistent
    def test_nonexistent(self):
        self.parseEqual('%ifdefnotempty{nonexistent,trueval,falseval}',
                        'falseval')

    # none
    def test_none(self):
        self.parseEqual('%ifdefnotempty{none,trueval,falseval}', 'falseval')

    # nonexistent
    def test_only_whitespaces(self):
        self.parseEqual('%ifdefnotempty{only_whitespaces,trueval,falseval}',
                        'falseval')


if __name__ == '__main__':
    unittest.main()
