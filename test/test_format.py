# -*- coding: utf-8 -*-
import unittest
from tmep.format import alphanum, asciify, delchars


class TestFormatFunctions(unittest.TestCase):

    def test_alphanum(self):
        self.assertEqual(alphanum('a-b'), 'a b')

    def test_asciify(self):
        self.assertEqual(asciify('ä'), 'ae')

    def test_delchars(self):
        self.assertEqual(delchars('a-b', '-'), 'ab')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
