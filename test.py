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
		self.template = '${lastname}; ${prename}'

		self.values = {
			'prename': 'Wolfgang Amadeus',
			'lastname': 'Mozart'
		}
		self.parse = tmep.parse
		self.out = tmep.parse(self.template, self.values)

	def test_values(self):
		self.assertEqual(self.out, 'Mozart; Wolfgang Amadeus')

	def test_additional_functions(self):
		def lol(value):
			return 'lol' + value + 'lol'

		def troll(value):
			return 'troll' + value + 'troll'

		add_functs = {'lol': lol, 'troll': troll}
		template = '%lol{$prename}%troll{$lastname}'
		out = self.parse(template, self.values, additional_functions=add_functs)
		self.assertEqual(out, 'lolWolfgang AmadeusloltrollMozarttroll')
		out = self.parse(template, self.values)
		self.assertEqual(out, template)

if __name__ == '__main__':
	unittest.main()
