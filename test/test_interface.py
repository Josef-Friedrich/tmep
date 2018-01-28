# -*- coding: utf-8 -*-

import unittest
import tmep


class TestClasses(unittest.TestCase):

    def setUp(self):
        self.template = '${lastname}; ${prename}'
        self.values = {'prename': 'Franz', 'lastname': 'Schubert'}

        template = tmep.Template(self.template)
        functions = tmep.Functions(self.values)
        self.out = template.substitute(self.values, functions.functions)

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


class TestDoc(unittest.TestCase):

    def setUp(self):
        from tmep import doc
        self.doc = doc.Doc()

    def test_attribute_functions(self):
        self.assertTrue(self.doc.functions)
        self.assertTrue(isinstance(self.doc.functions, list))

    def test_attribute_synopsises(self):
        self.assertTrue(self.doc.synopsises)
        self.assertTrue(isinstance(self.doc.synopsises, dict))

    def test_attribute_examples(self):
        self.assertTrue(self.doc.examples)
        self.assertTrue(isinstance(self.doc.examples, dict))

    def test_attribute_descriptions(self):
        self.assertTrue(self.doc.descriptions)
        self.assertTrue(isinstance(self.doc.descriptions, dict))

    def test_functions_sort(self):
        self.assertEqual(self.doc.functions, sorted(self.doc.functions))

    def test_extract_synopsis(self):
        value = self.doc.extract_value(
            '        * synopsis: ``%shorten(text, max_size)``',
            'synopsis'
        )
        self.assertEqual(value, '%shorten(text, max_size)')

    def test_extract_synopsis_multiple(self):
        value = self.doc.extract_value(
            '* synopsis: ``%shorten(text)`` or ``%shorten(text, max_size)``',
            'synopsis'
        )
        self.assertEqual(value, '%shorten(text) or %shorten(text, max_size)')

    def test_extract_example(self):
        value = self.doc.extract_value(
            '        * example: ``%shorten($title, 2)``',
            'example',
            True
        )
        self.assertEqual(value, '%shorten($title, 2)')

    def test_extract_description(self):
        value = self.doc.extract_value(
            '        * description: Some description',
            'description',
            False
        )
        self.assertEqual(value, 'Some description')

    def test_get(self):
        self.assertTrue(self.doc.get())


if __name__ == '__main__':
    unittest.main()
