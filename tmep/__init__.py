from importlib import metadata
from typing import Optional

from tmep import doc, functions, template
from tmep.types import FunctionCollection, Values

__version__: str = metadata.version("tmep")

doc


def parse(
    template: str,
    values: Optional[Values] = None,
    additional_functions: Optional[FunctionCollection] = None,
    functions: Optional[FunctionCollection] = None,
) -> str:
    """
    Parse the given template string and substitute placeholders with values.

    :param template: The template string to parse, for example ``Hello $name!``.
    :param values: Optional dictionary of values to substitute in the template,
      for example ``{"name": "World"}``.
    :param additional_functions: Optional dictionary of additional functions to use
      in the template.
    :param functions: Optional dictionary of functions to use in the template.
    :return: The parsed template string with placeholders substituted.
    """
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


get_doc = doc.get_doc
"""
see  :func:`tmep.doc.get_doc`
"""

Template = template.Template
"""
see  :class:`tmep.template.Template`
"""

Functions = functions.Functions
"""
see  :class:`tmep.functions.Functions`
"""
