#! /usr/bin/env python

import unittest
import tmep

template = '${lastname}; ${prename}'

values = {
    'prename': 'Wolfgang Amadeus',
    'lastname': 'Mozart'
}

t = tmep.Template(template)
f = tmep.Functions(values)
out = t.substitute(values, f.functions)

class TestStringMethods(unittest.TestCase):

    def test_values(self):
        self.assertEqual(out, 'Mozart; Wolfgang Amadeus')

if __name__ == '__main__':
    unittest.main()
