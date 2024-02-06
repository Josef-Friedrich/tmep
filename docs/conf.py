# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

import tmep

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]
templates_path = ["_templates"]
source_suffix = ".rst"

master_doc = "index"

project = "tmep"
copyright = "2016-2024, Josef Friedrich"
author = "Josef Friedrich"
version = tmep.__version__
release = tmep.__version__
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"
todo_include_todos = False
html_static_path = []
htmlhelp_basename = "tmepdoc"

autodoc_default_options = {
    # If set, autodoc will generate documention for the members of the target module, class or exception.
    "members": True,
    # This value selects if automatically documented members are sorted alphabetical (value 'alphabetical'), by member type (value 'groupwise') or by source order (value 'bysource'). The default is alphabetical.
    "member-order": "bysource",
    # If set, autodoc will also generate document for the members not having docstrings:
    "undoc-members": True,
    # If set, autodoc will also generate document for the private members (that is, those named like _private or __private)
    "private-members": False,
    # If set, autodoc will also generate document for the special members (that is, those named like __special__):
    "special-members": False,
    # For classes and exceptions, members inherited from base classes will be left out when documenting all members, unless you give the inherited-members option, in addition to members
    "inherited-members": False,
}
