from __future__ import annotations

from importlib import metadata
from typing import Optional

from tmep import doc, functions, template
from tmep.types import FunctionCollection, Values

__version__: str = metadata.version("tmep")


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
    :param additional_functions: Additional functions to use
      in the template.
    :param functions: Use the given functions instead of the default functions.

    :return: The parsed template string with placeholders substituted.
    """
    if not functions:
        functions = Functions(values).get()

    if additional_functions:
        for k, v in additional_functions.items():
            functions[k] = v

    if not values:
        values = {}
    return Template(template).substitute(values, functions)


Template = template.Template
"""
:see: :class:`tmep.template.Template`
"""

Functions = functions.DefaultTemplateFunctions
"""
:see: :class:`tmep.functions.DefaultTemplateFunctions`
"""

get_doc = doc.get_doc
"""
:see: :func:`tmep.doc.get_doc`
"""
