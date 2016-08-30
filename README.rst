.. image:: http://img.shields.io/pypi/v/tmep.svg
    :target: https://pypi.python.org/pypi/tmep

.. image:: https://travis-ci.org/Josef-Friedrich/tmep.svg?branch=master
    :target: https://travis-ci.org/Josef-Friedrich/tmep

====================================================
tmep - Template and Macros Expansion for Path names.
====================================================

This module implements a string formatter based on the standard PEP
292 string.Template class extended with function calls. Variables, as
with string.Template, are indicated with $ and functions are delimited
with %.

This module assumes that everything is Unicode: the template and the
substitution values. Bytestrings are not supported. Also, the templates
always behave like the ``safe_substitute`` method in the standard
library: unknown symbols are left intact.

This is sort of like a tiny, horrible degeneration of a real templating
engine like Jinja2 or Mustache.
