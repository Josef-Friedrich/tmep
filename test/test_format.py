# -*- coding: utf-8 -*-
import unittest
from tmep.format import \
    alpha, \
    alphanum, \
    asciify, \
    delchars, \
    deldupchars, \
    first, \
    initial, \
    left, \
    lower, \
    nowhitespace, \
    num, \
    replchars, \
    right, \
    sanitize, \
    shorten, \
    time, \
    title, \
    upper


class TestFormatFunctions(unittest.TestCase):

    def test_alpha(self):
        self.assertTrue(callable(alpha))

    def test_alphanum(self):
        self.assertEqual(alphanum('a-b'), 'a b')
        self.assertTrue(callable(alphanum))

    def test_asciify(self):
        self.assertEqual(asciify('ä'), 'ae')
        self.assertTrue(callable(asciify))

    def test_delchars(self):
        self.assertEqual(delchars('a-b', '-'), 'ab')
        self.assertTrue(callable(delchars))

    def test_deldupchars(self):
        self.assertTrue(callable(deldupchars))

    def test_first(self):
        self.assertTrue(callable(first))

    def test_initial(self):
        self.assertTrue(callable(initial))

    def test_left(self):
        self.assertTrue(callable(left))

    def test_lower(self):
        self.assertTrue(callable(lower))

    def test_num(self):
        self.assertTrue(callable(num))

    def test_nowhitespace(self):
        self.assertTrue(callable(nowhitespace))

    def test_replchars(self):
        self.assertTrue(callable(replchars))

    def test_right(self):
        self.assertTrue(callable(right))

    def test_sanitize(self):
        self.assertTrue(callable(sanitize))

    def test_shorten(self):
        self.assertTrue(callable(shorten))

    def test_time(self):
        self.assertTrue(callable(time))

    def test_title(self):
        self.assertTrue(callable(title))

    def test_upper(self):
        self.assertTrue(callable(upper))


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
