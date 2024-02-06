from tmep import doc
from tmep.doc import FnDoc


class TestDoc:
    def setup_method(self) -> None:
        self.doc = doc.FnDocCollection()

    def test_functions_sort(self) -> None:
        assert self.doc.fn_names == sorted(self.doc.fn_names)

    def test_get(self) -> None:
        assert self.doc.format()

    def test_read_help_text_rst(self) -> None:
        assert isinstance(doc.read_help_text_rst(), str)


class TestClassFunctionDocumentation:
    def setup_method(self) -> None:
        self.fun_doc = FnDoc("if")

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

    def test_format(self) -> None:
        assert (
            self.fun_doc.format("txt")
            == "    if\n    --\n\n    ``%if{condition,truetext}`` or ``%if{condition,truetext,falsetext}``\n        If condition is nonempty (or nonzero, if it’s a number), then returns\n        the second argument. Otherwise, returns the third argument if\n        specified (or nothing if falsetext is left off).\n"
        )
