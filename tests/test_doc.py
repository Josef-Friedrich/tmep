from tmep import doc
from tmep.doc import FunctionDocumentation


class TestDoc:
    def setup_method(self) -> None:
        self.doc = doc.Doc()

    def test_attribute_functions(self) -> None:
        assert self.doc.functions
        assert isinstance(self.doc.functions, list)

    def test_attribute_synopsises(self) -> None:
        assert self.doc.synopsises
        assert isinstance(self.doc.synopsises, dict)

    def test_attribute_examples(self) -> None:
        assert self.doc.examples
        assert isinstance(self.doc.examples, dict)

    def test_attribute_descriptions(self) -> None:
        assert self.doc.descriptions
        assert isinstance(self.doc.descriptions, dict)

    def test_functions_sort(self) -> None:
        assert self.doc.functions == sorted(self.doc.functions)

    def test_extract_synopsis(self) -> None:
        value = self.doc.extract_value(
            "        * synopsis: ``%shorten(text, max_size)``", "synopsis"
        )
        assert value == "%shorten(text, max_size)"

    def test_extract_synopsis_multiple(self) -> None:
        value = self.doc.extract_value(
            "* synopsis: ``%shorten(text)`` or ``%shorten(text, max_size)``", "synopsis"
        )
        assert value == "%shorten(text) or %shorten(text, max_size)"

    def test_extract_example(self) -> None:
        value = self.doc.extract_value(
            "        * example: ``%shorten($title, 2)``",
            "example",
        )
        assert value == "%shorten($title, 2)"

    def test_extract_description(self) -> None:
        value = self.doc.extract_value(
            "        * description: Some description", "description", False
        )
        assert value == "Some description"

    def test_get(self) -> None:
        assert self.doc.get()

    def test_read_help_text_rst(self) -> None:
        assert isinstance(doc.read_help_text_rst(), str)


class TestClassFunctionDocumentation:
    def setup_method(self) -> None:
        self.fun_doc = FunctionDocumentation("if")

    def test_name(self) -> None:
        assert self.fun_doc.name == "if"

    def test_synopsis(self) -> None:
        assert (
            self.fun_doc.synopsis
            == "``%if{condition,truetext}`` or ``%if{condition,truetext,falsetext}``"
        )

    def test_example(self) -> None:
        assert self.fun_doc.example is None

    def test_description(self) -> None:
        assert (
            self.fun_doc.description
            == "If condition is nonempty (or nonzero, if it’s a number), then returns the second argument. Otherwise, returns the third argument if specified (or nothing if falsetext is left off)."
        )
