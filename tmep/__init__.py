from importlib import metadata
from typing import Optional

from tmep import doc, functions, template
from tmep.types import FunctionCollection, Values

__version__: str = metadata.version("tmep")

doc


class Template(template.Template):
    def __init__(self, template: str) -> None:
        super(Template, self).__init__(template)


class Functions(functions.Functions):
    def __init__(self, values: Optional[Values] = None) -> None:
        super(Functions, self).__init__(values)


def parse(
    template: str,
    values: Optional[Values] = None,
    additional_functions: Optional[FunctionCollection] = None,
    functions: Optional[FunctionCollection] = None,
) -> str:
    template_ = Template(template)
    if not functions:
        functions_ = Functions(values)
        functions = functions_.functions()

    if additional_functions:
        for k, v in additional_functions.items():
            functions[k] = v

    if not values:
        values = {}
    return template_.substitute(values, functions)
