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
            'prename': 'Franz',
            'lastname': 'Schubert',
            'lol': 'lol',
            'troll': 'troll',
            'track': 7,
        }

    def parseEqual(self, a, b):
        self.assertEqual(tmep.parse(a, self.values), b)

    # num
    def test_num_literal(self):
        self.parseEqual(u'%num{7,3}', u'007')

    def test_num_variable(self):
        self.parseEqual(u'%num{$track,3}', u'007')

    def test_num_default_count(self):
        self.parseEqual(u'%num{7}', u'07')

    def test_num_default_variable(self):
        self.parseEqual(u'%num{$track}', u'07')

    # upper
    def test_upper_literal(self):
        self.parseEqual(u'%upper{foo}', u'FOO')

    def test_upper_variable(self):
        self.parseEqual(u'%upper{$prename}', u'FRANZ')

    # title
    def test_title_literal(self):
        self.parseEqual(u'%title{franz schubert}', u'Franz Schubert')

    def test_title_variable(self):
        self.parseEqual(u'%title{$lol $troll}', u'Lol Troll')

    # left
    def test_left_literal(self):
        self.parseEqual(u'%left{Schubert, 3}', u'Sch')

    def test_left_variable(self):
        self.parseEqual(u'%left{$lastname, 3}', u'Sch')

    # right
    def test_right_literal(self):
        self.parseEqual(u'%right{Schubert,3}', u'ert')

    def test_right_variable(self):
        self.parseEqual(u'%right{$lastname,3}', u'ert')

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

    #
    # def test_nonexistent_function(self):
    #     self.parseEqual(, )
    #     self._setf(u'%foo{bar}')
    #     self._assert_dest(b'/base/%foo{bar}')
    #
    # def test_if_def_field_return_self(self):
    #     self.parseEqual(, )
    #     self.i.bar = 3
    #     self._setf(u'%ifdef{bar}')
    #     self._assert_dest(b'/base/3')
    #
    # def test_if_def_field_not_defined(self):
    #     self.parseEqual(, )
    #     self._setf(u' %ifdef{bar}/$artist')
    #     self._assert_dest(b'/base/the artist')
    #
    # def test_if_def_field_not_defined_2(self):
    #     self.parseEqual(, )
    #     self._setf(u'$artist/%ifdef{bar}')
    #     self._assert_dest(b'/base/the artist')
    #
    # def test_if_def_true(self):
    #     self.parseEqual(, )
    #     self._setf(u'%ifdef{artist,cool}')
    #     self._assert_dest(b'/base/cool')
    #
    # def test_if_def_true_complete(self):
    #     self.parseEqual(, )
    #     self.i.series = "Now"
    #     self._setf(u'%ifdef{series,$series Series,Albums}/$album')
    #     self._assert_dest(b'/base/Now Series/the album')
    #
    # def test_if_def_false_complete(self):
    #     self.parseEqual(, )
    #     self._setf(u'%ifdef{plays,$plays,not_played}')
    #     self._assert_dest(b'/base/not_played')
    #
    # def test_first(self):
    #     self.parseEqual(, )
    #     self.i.genres = "Pop; Rock; Classical Crossover"
    #     self._setf(u'%first{$genres}')
    #     self._assert_dest(b'/base/Pop')
    #
    # def test_first_skip(self):
    #     self.parseEqual(, )
    #     self.i.genres = "Pop; Rock; Classical Crossover"
    #     self._setf(u'%first{$genres,1,2}')
    #     self._assert_dest(b'/base/Classical Crossover')
    #
    # def test_first_different_sep(self):
    #     self.parseEqual(, )
    #     self._setf(u'%first{Alice / Bob / Eve,2,0, / , & }')
    #     self._assert_dest(b'/base/Alice & Bob')


if __name__ == '__main__':
    unittest.main()
