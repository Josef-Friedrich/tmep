"""Test the interface of the main package."""

from __future__ import annotations

import tmep
from tmep.types import FunctionCollection


class TestClasses:
    def setup_method(self):
        self.template = "${lastname}; ${prename}"
        self.values = {"prename": "Franz", "lastname": "Schubert"}

        template = tmep.Template(self.template)
        functions = tmep.Functions(self.values)
        self.out = template.substitute(self.values, functions.get())

    def test_values(self):
        assert self.out == "Schubert; Franz"


class TestDefinitionParse:
    def setup_method(self):
        self.parse = tmep.parse
        self.template = "${lastname}; ${prename}"
        self.values = {"prename": "Franz", "lastname": "Schubert"}

        def lol(value: str) -> str:
            return "lol" + value + "lol"

        def troll(value: str) -> str:
            return "troll" + value + "troll"

        self.functions: FunctionCollection = {"lol": lol, "troll": troll}

    def test_values(self):
        out = self.parse(self.template, self.values)
        assert out == "Schubert; Franz"

    def test_parameter_functions(self):
        template = "%lol{$prename}%troll{$lastname}"
        out = self.parse(template, self.values, functions=self.functions)
        assert out == "lolFranzloltrollSchuberttroll"

    def test_parameter_additional_functions(self):
        template = "%lol{$prename}%troll{$lastname}"
        out = self.parse(template, self.values, additional_functions=self.functions)
        assert out == "lolFranzloltrollSchuberttroll"
        out = self.parse(template, self.values)
        assert out == template


class TestDoc:
    def test_import(self):
        assert tmep.doc.FnDocCollection
