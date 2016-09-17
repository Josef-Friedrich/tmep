#! /usr/bin/env python

import unittest
import tmep


class TestClasses(unittest.TestCase):
    def setUp(self):
        self.template = '${lastname}; ${prename}'
        self.values = {'prename': 'Franz', 'lastname': 'Schubert'}

        t = tmep.Template(self.template)
        f = tmep.Functions(self.values)
        self.out = t.substitute(self.values, f.functions)

    def test_values(self):
        self.assertEqual(self.out, 'Schubert; Franz')


class TestDefinitionParse(unittest.TestCase):
    def setUp(self):
        self.parse = tmep.parse
        self.template = '${lastname}; ${prename}'
        self.values = {'prename': 'Franz', 'lastname': 'Schubert'}

        def lol(value):
            return 'lol' + value + 'lol'

        def troll(value):
            return 'troll' + value + 'troll'

        self.functions = {'lol': lol, 'troll': troll}

    def test_values(self):
        out = self.parse(self.template, self.values)
        self.assertEqual(out, 'Schubert; Franz')

    def test_parameter_functions(self):
        template = '%lol{$prename}%troll{$lastname}'
        out = self.parse(template, self.values, functions=self.functions)
        self.assertEqual(out, 'lolFranzloltrollSchuberttroll')

    def test_parameter_additional_functions(self):
        template = '%lol{$prename}%troll{$lastname}'
        out = self.parse(
            template, self.values, additional_functions=self.functions)
        self.assertEqual(out, 'lolFranzloltrollSchuberttroll')
        out = self.parse(template, self.values)
        self.assertEqual(out, template)


if __name__ == '__main__':
    unittest.main()
