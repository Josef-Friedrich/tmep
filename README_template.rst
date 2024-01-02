{{ badge.pypi }}

{{ badge.github_workflow() }}

{{ badge.readthedocs }}

====
tmep
====

Template and Macros Expansion for Path names.

Installation
============

From PyPI
----------

.. code:: Shell

    pip install tmep

Usage
=====

.. code:: Python

    >>> import tmep
    >>> template = '$prename $lastname'
    >>> values = {'prename': 'Franz', 'lastname': 'Schubert'}
    >>> out = tmep.parse(template, values)
    >>> print(out)
    Franz Schubert

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

Development
===========

Test
----

::

    poetry run tox

Publish a new version
---------------------

::

    git tag 1.1.1
    git push --tags
    poetry build
    poetry publish

Package documentation
---------------------

The package documentation is hosted on
`readthedocs <http://tmep.readthedocs.io>`_.

Generate the package documentation:

::

    python setup.py build_sphinx


Functions
=========

{{ func('tmep.doc.get_doc') | literal(False) }}
