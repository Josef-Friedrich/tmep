{{ badge.pypi }}

{{ badge.github_workflow() }}

{{ badge.readthedocs }}

====
TMEP
====

TMEP (Template Macro Expansion for Paths) is a small template engine that
has been specially developed for file paths.

The engine can replace or expand symbols (or variables) like ``$title`` and
apply functions (or macros) like ``%upper{}`` in path templates.

The code originates from the `Beets project <https://beets.io/>`_ and was “extracted”
from the code base together with the tests.

Installation
============

From PyPI
---------

.. code:: Shell

    pip install tmep

Usage
=====

.. code:: Python

    >>> import tmep
    >>> template = "%upper{$prename $lastname}"
    >>> values = {"prename": "Franz", "lastname": "Schubert"}
    >>> result = tmep.parse(template, values)
    >>> print(result)
    FRANZ SCHUBERT

This module implements a string formatter based on the standard
`PEP 292 <https://peps.python.org/pep-0292>`_
`string.Template <https://docs.python.org/3/library/string.html#template-strings>`_
class extended with function calls. Variables, as with
`string.Template <https://docs.python.org/3/library/string.html#template-strings>`_,
are indicated with ``$`` and functions are delimited
with ``%``.

This module assumes that everything is Unicode: the template and the
substitution values. Bytestrings are not supported. Also, the templates
always behave like the ``safe_substitute`` method in the standard
library: unknown symbols are left intact.

This is sort of like a tiny, horrible degeneration of a real templating
engine like Jinja2 or Mustache.

TMEP provides public Python functions and a small command line tool that outputs
documentation in various formats that can be used by projects based on TMEP.

Introduction
============

``tmep-doc --introduction-rst``

{{ cli('tmep-doc --introduction-rst') }}

Functions
=========

reStructuredText format (``tmep-doc --functions-rst``):

{{ cli('tmep-doc --functions-rst') }}

{{ cli('tmep-doc --functions-rst') | literal }}

Plain text format (``tmep-doc --functions-txt``):

{{ cli('tmep-doc --functions-txt') | literal(False) }}

Development
===========

Package documentation
---------------------

The package documentation is hosted on
`readthedocs <http://tmep.readthedocs.io>`_.
