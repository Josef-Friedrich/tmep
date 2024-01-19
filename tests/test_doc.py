from tmep import doc


class TestDoc:
    def setup_method(self):
        self.doc = doc.Doc()

    def test_attribute_functions(self):
        assert self.doc.functions
        assert isinstance(self.doc.functions, list)

    def test_attribute_synopsises(self):
        assert self.doc.synopsises
        assert isinstance(self.doc.synopsises, dict)

    def test_attribute_examples(self):
        assert self.doc.examples
        assert isinstance(self.doc.examples, dict)

    def test_attribute_descriptions(self):
        assert self.doc.descriptions
        assert isinstance(self.doc.descriptions, dict)

    def test_functions_sort(self):
        assert self.doc.functions == sorted(self.doc.functions)

    def test_extract_synopsis(self):
        value = self.doc.extract_value(
            "        * synopsis: ``%shorten(text, max_size)``", "synopsis"
        )
        assert value == "%shorten(text, max_size)"

    def test_extract_synopsis_multiple(self):
        value = self.doc.extract_value(
            "* synopsis: ``%shorten(text)`` or ``%shorten(text, max_size)``", "synopsis"
        )
        assert value == "%shorten(text) or %shorten(text, max_size)"

    def test_extract_example(self):
        value = self.doc.extract_value(
            "        * example: ``%shorten($title, 2)``",
            "example",
        )
        assert value == "%shorten($title, 2)"

    def test_extract_description(self):
        value = self.doc.extract_value(
            "        * description: Some description", "description", False
        )
        assert value == "Some description"

    def test_get(self):
        assert self.doc.get()

    def test_read_help_text_rst(self):
        assert isinstance(doc.read_help_text_rst(), str)
