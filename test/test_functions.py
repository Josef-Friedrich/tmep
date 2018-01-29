# -*- coding: utf-8 -*-
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

import unittest
import tmep


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.values = {
            'prename': u'Franz',
            'lastname': u'Schubert',
            'lol': u'lol',
            'troll': u'troll',
            'genres': u'Pop; Rock; Classical Crossover',
            'asciify': u'gennemgår',
            'track': 7,
        }

    def parseEqual(self, a, b):
        self.assertEqual(tmep.parse(a, self.values), b)

    # asciify
    def test_asciify_literal(self):
        self.parseEqual(u'%asciify{après évêque}', u'apres eveque')

    def test_asciify_variable(self):
        self.parseEqual(u'%asciify{$asciify}', u'gennemgar')

    def test_asciify_foreign(self):
        self.parseEqual(u'%asciify{Новыя старонкі}', u'Novyia staronki')

    def test_asciify_german_umlaute(self):
        self.parseEqual(u'%asciify{äÄöÖüÜ}', u'aeAeoeOeueUe')

    def test_asciify_symbols_single(self):
        self.parseEqual(u'%asciify{⚓}', u'')

    def test_asciify_symbols_multiple(self):
        self.parseEqual(u'%asciify{⚢⚣⚤⚥⚦⚧⚨⚩}', u'')

    def test_asciify_symbols_mixed(self):
        self.parseEqual(u'%asciify{a⚢b⚣⚤c}', u'abc')

    # delchars
    def test_delchars_single(self):
        self.parseEqual(u'%delchars{x-x,-}', u'xx')

    def test_delchars_multiple(self):
        self.parseEqual(u'%delchars{x---x,-}', u'xx')

    def test_delchars_no_match(self):
        self.parseEqual(u'%delchars{x-x,_}', u'x-x')

    def test_delchars_multiple_chars(self):
        self.parseEqual(u'%delchars{x_-.x,_-.}', u'xx')

    def test_delchars_unicode(self):
        self.parseEqual(u'%delchars{öd,ö}', u'd')

    def test_delchars_variable(self):
        self.parseEqual(u'%delchars{$lastname,ue}', u'Schbrt')

    # deldupchars
    def test_deldupchars_default(self):
        self.parseEqual(u'%deldupchars{a---b___c...d}', u'a-b_c.d')

    def test_deldupchars_custom(self):
        self.parseEqual(u'%deldupchars{a---b___c,-}', u'a-b___c')

    def test_deldupchars_whitespace(self):
        self.parseEqual(u'%deldupchars{a   a, }', u'a a')

    # first
    def test_first(self):
        self.parseEqual(u'%first{$genres}', u'Pop')

    def test_first_skip(self):
        self.parseEqual(u'%first{$genres,1,2}', u'Classical Crossover')

    def test_first_different_sep(self):
        self.parseEqual(
            u'%first{Alice / Bob / Eve,2,0, / , & }',
            u'Alice & Bob'
        )

    # if
    def test_if_false(self):
        self.parseEqual(u'x%if{,foo}', u'x')

    def test_if_false_value(self):
        self.parseEqual(u'x%if{false,foo}', u'x')

    def test_if_true(self):
        self.parseEqual(u'%if{bar,foo}', u'foo')

    def test_if_else_false(self):
        self.parseEqual(u'%if{,foo,baz}', u'baz')

    def test_if_else_false_value(self):
        self.parseEqual(u'%if{false,foo,baz}', u'baz')

    def test_if_int_value(self):
        self.parseEqual(u'%if{0,foo,baz}', u'baz')

    # ifdef
    def test_if_def_field_return_self(self):
        self.parseEqual(u'%ifdef{lastname}', u'')

    def test_if_def_field_not_defined(self):
        self.parseEqual(u'%ifdef{bar}', u'')

    def test_if_def_true(self):
        self.parseEqual(u'%ifdef{lastname,Its true}', u'Its true')

    def test_if_def_true_complete(self):
        self.parseEqual(u'%ifdef{lastname,lol,troll}', u'lol')

    def test_if_def_false_complete(self):
        self.parseEqual(u'%ifdef{trill,lol,troll}', u'troll')

    # left
    def test_left_literal(self):
        self.parseEqual(u'%left{Schubert, 3}', u'Sch')

    def test_left_variable(self):
        self.parseEqual(u'%left{$lastname, 3}', u'Sch')

    # lower
    def test_lower_literal(self):
        self.parseEqual(u'%lower{SCHUBERT}', u'schubert')

    def test_lower_variable(self):
        self.parseEqual(u'%lower{$lastname}', u'schubert')

    # num
    def test_num_literal(self):
        self.parseEqual(u'%num{7,3}', u'007')

    def test_num_variable(self):
        self.parseEqual(u'%num{$track,3}', u'007')

    def test_num_default_count(self):
        self.parseEqual(u'%num{7}', u'07')

    def test_num_default_variable(self):
        self.parseEqual(u'%num{$track}', u'07')

    # replchars
    def test_replchars_literal(self):
        self.parseEqual(u'%replchars{Schubert,-,ue}', u'Sch-b-rt')

    def test_replchars_variable(self):
        self.parseEqual(u'%replchars{$lastname,-,ue}', u'Sch-b-rt')

    # right
    def test_right_literal(self):
        self.parseEqual(u'%right{Schubert,3}', u'ert')

    def test_right_variable(self):
        self.parseEqual(u'%right{$lastname,3}', u'ert')

    # sanitize
    def test_sanitize_literal(self):
        self.parseEqual(u'%sanitize{x:*?<>|\/~&x}', u'xx')

    # shorten
    def test_shorten_literal(self):
        self.parseEqual(u'%shorten{Lorem ipsum dolor sit,10}', u'Lorem')

    def test_shorten_default(self):
        self.parseEqual(
            u'%shorten{Lorem ipsum dolor sit amet consectetur adipisicing}',
            u'Lorem ipsum dolor sit amet')

    # title
    def test_title_literal(self):
        self.parseEqual(u'%title{franz schubert}', u'Franz Schubert')

    def test_title_variable(self):
        self.parseEqual(u'%title{$lol $troll}', u'Lol Troll')

    # upper
    def test_upper_literal(self):
        self.parseEqual(u'%upper{foo}', u'FOO')

    def test_upper_variable(self):
        self.parseEqual(u'%upper{$prename}', u'FRANZ')

    #
    def test_nonexistent_function(self):
        self.parseEqual(u'%foo{bar}', u'%foo{bar}')


class TestFunctionIfDefEmpty(unittest.TestCase):

    def setUp(self):
        self.values = {
            'empty_string': u'',
            'false': False,
            'non_empty_string': u'test',
            'none': None,
            'only_whitespaces': u' \t\n',
        }

    def parseEqual(self, a, b):
        self.assertEqual(tmep.parse(a, self.values), b)

    # empty_string
    def test_empty_string(self):
        self.parseEqual(u'%ifdefempty{empty_string,trueval}', u'trueval')

    # false
    def test_false(self):
        self.parseEqual(u'%ifdefempty{false,trueval}', u'trueval')

    # non_empty_string
    def test_non_empty_string(self):
        self.parseEqual(u'%ifdefempty{non_empty_string,trueval,falseval}',
                        u'falseval')

    # nonexistent
    def test_nonexistent(self):
        self.parseEqual(u'%ifdefempty{nonexistent,trueval,falseval}',
                        u'trueval')

    # none
    def test_none(self):
        self.parseEqual(u'%ifdefempty{none,trueval}', u'trueval')

    # nonexistent
    def test_only_whitespaces(self):
        self.parseEqual(u'%ifdefempty{only_whitespaces,trueval,falseval}',
                        u'trueval')


class TestFunctionIfDefNotEmpty(unittest.TestCase):

    def setUp(self):
        self.values = {
            'empty_string': u'',
            'false': False,
            'non_empty_string': u'test',
            'none': None,
            'only_whitespaces': u' \t\n',
        }

    def parseEqual(self, a, b):
        self.assertEqual(tmep.parse(a, self.values), b)

    # empty_string
    def test_empty_string(self):
        self.parseEqual(u'%ifdefnotempty{empty_string,trueval,falseval}',
                        u'falseval')

    # false
    def test_false(self):
        self.parseEqual(u'%ifdefnotempty{false,trueval,falseval}',
                        u'falseval')

    # non_empty_string
    def test_non_empty_string(self):
        self.parseEqual(u'%ifdefnotempty{non_empty_string,trueval,falseval}',
                        u'trueval')

    # nonexistent
    def test_nonexistent(self):
        self.parseEqual(u'%ifdefnotempty{nonexistent,trueval,falseval}',
                        u'falseval')

    # none
    def test_none(self):
        self.parseEqual(u'%ifdefnotempty{none,trueval,falseval}', u'falseval')

    # nonexistent
    def test_only_whitespaces(self):
        self.parseEqual(u'%ifdefnotempty{only_whitespaces,trueval,falseval}',
                        u'falseval')


if __name__ == '__main__':
    unittest.main()
