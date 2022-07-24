import unittest

from tmep import doc


class TestDoc(unittest.TestCase):
    def setUp(self):
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
            "        * synopsis: ``%shorten(text, max_size)``", "synopsis"
        )
        self.assertEqual(value, "%shorten(text, max_size)")

    def test_extract_synopsis_multiple(self):
        value = self.doc.extract_value(
            "* synopsis: ``%shorten(text)`` or ``%shorten(text, max_size)``", "synopsis"
        )
        self.assertEqual(value, "%shorten(text) or %shorten(text, max_size)")

    def test_extract_example(self):
        value = self.doc.extract_value(
            "        * example: ``%shorten($title, 2)``",
            "example",
        )
        self.assertEqual(value, "%shorten($title, 2)")

    def test_extract_description(self):
        value = self.doc.extract_value(
            "        * description: Some description", "description", False
        )
        self.assertEqual(value, "Some description")

    def test_get(self):
        self.assertTrue(self.doc.get())


if __name__ == "__main__":
    unittest.main()
