#! /usr/bin/env python

import unittest
import tmep

class TestClasses(unittest.TestCase):

    def setUp(self):
        template = '${lastname}; ${prename}'

        values = {
            'prename': 'Wolfgang Amadeus',
            'lastname': 'Mozart'
        }

        t = tmep.Template(template)
        f = tmep.Functions(values)
        self.out = t.substitute(values, f.functions)

    def test_values(self):
        self.assertEqual(self.out, 'Mozart; Wolfgang Amadeus')

class TestParseDef(unittest.TestCase):

    def setUp(self):
        template = '${lastname}; ${prename}'

        values = {
            'prename': 'Wolfgang Amadeus',
            'lastname': 'Mozart'
        }

        self.out = tmep.parse(template, values)

    def test_values(self):
        self.assertEqual(self.out, 'Mozart; Wolfgang Amadeus')


if __name__ == '__main__':
    unittest.main()
