#! /usr/bin/env python

import unittest
import path_macrotemplate as pmt

template = '${lastname}; ${prename}'

values = {
    'prename': 'Wolfgang Amadeus',
    'lastname': 'Mozart'
}

t = pmt.Template(template)
f = pmt.Functions(values)
out = t.substitute(values, f.functions)

class TestStringMethods(unittest.TestCase):

    def test_values(self):
        self.assertEqual(out, 'Mozart; Wolfgang Amadeus')

if __name__ == '__main__':
    unittest.main()
