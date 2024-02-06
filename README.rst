.. image:: http://img.shields.io/pypi/v/tmep.svg
    :target: https://pypi.org/project/tmep
    :alt: This package on the Python Package Index

.. image:: https://github.com/Josef-Friedrich/tmep/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/Josef-Friedrich/tmep/actions/workflows/tests.yml
    :alt: Tests

.. image:: https://readthedocs.org/projects/tmep/badge/?version=latest
    :target: https://tmep.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

====
tmep
====

Template and Macros Expansion for Path names.

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
    >>> template = '$prename $lastname'
    >>> values = {'prename': 'Franz', 'lastname': 'Schubert'}
    >>> out = tmep.parse(template, values)
    >>> print(out)
    Franz Schubert

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

Introduction
============

Template Symbols or Variables
  In path templates, symbols or varialbes such as ``$title``
  (any name with the prefix ``$``) are replaced by the corresponding value.

  Because ``$`` is used to delineate a field reference, you can use ``$$`` to emit
  a dollars sign. As with `Python template strings`_, ``${title}`` is equivalent
  to ``$title``; you can use this if you need to separate a field name from the
  text that follows it.

.. _Python template strings: https://docs.python.org/library/string.html#template-strings

Template Functions
  Path templates also support *function calls*, which can be used to transform
  text and perform logical manipulations. The syntax for function calls is like
  this: ``%func{arg,arg}``. For example, the ``upper`` function makes its argument
  upper-case, so ``%upper{lorem ipsum}`` will be replaced with ``LOREM IPSUM``.
  You can, of course, nest function calls and place variable references in
  function arguments, so ``%upper{$title}`` becomes the upper-case version of the
  title.

Syntax Details
  The characters ``$``, ``%``, ``{``, ``}``, and ``,`` are “special” in the path
  template syntax. This means that, for example, if you want a ``%`` character to
  appear in your paths, you’ll need to be careful that you don’t accidentally
  write a function call. To escape any of these characters (except ``{``, and
  ``,`` outside a function argument), prefix it with a ``$``.  For example,
  ``$$`` becomes ``$``; ``$%`` becomes ``%``, etc. The only exceptions are:

  * ``${``, which is ambiguous with the variable reference syntax (like
    ``${title}``). To insert a ``{`` alone, it's always sufficient to just type
    ``{``.
  * commas are used as argument separators in function calls. Inside of a
    function’s argument, use ``$,`` to get a literal ``,`` character. Outside of
    any function argument, escaping is not necessary: ``,`` by itself will
    produce ``,`` in the output.

  If a value or function is undefined, the syntax is simply left unreplaced. For
  example, if you write ``$foo`` in a path template, this will yield ``$foo`` in
  the resulting paths because "foo" is not a valid field name. The same is true of
  syntax errors like unclosed ``{}`` pairs; if you ever see template syntax
  constructs leaking into your paths, check your template for errors.

  If an error occurs in the Python code that implements a function, the function
  call will be expanded to a string that describes the exception so you can debug
  your template. For example, the second parameter to ``%left`` must be an
  integer; if you write ``%left{foo,bar}``, this will be expanded to something
  like ``<ValueError: invalid literal for int()>``.

Functions
=========

reStructuredText format:

alpha
  ``%alpha{text}``:  This function first ASCIIfies the given text, then all
  non alphabet characters are replaced with whitespaces.
alphanum
  ``%alphanum{text}``:  This function first ASCIIfies the given text, then all
  non alpanumeric characters are replaced with whitespaces.
asciify
  ``%asciify{text}``:  Translate non-ASCII characters to their ASCII
  equivalents. For example, “café” becomes “cafe”. Uses the mapping provided
  by the unidecode module.
delchars
  ``%delchars{text,chars}``:  Delete every single character of “chars“ in
  “text”.
deldupchars
  ``%deldupchars{text,chars}``:  Search for duplicate characters and replace
  with only one occurrance of this characters.
first
  ``%first{text}`` or ``%first{text,count,skip}`` or
  ``%first{text,count,skip,sep,join}``:  Returns the first item, separated by
  ; . You can use %first{text,count,skip}, where count is the number of items
  (default 1) and skip is number to skip (default 0). You can also use
  %first{text,count,skip,sep,join} where sep is the separator, like ; or / and
  join is the text to concatenate the items.
if
  ``%if{condition,truetext}`` or ``%if{condition,truetext,falsetext}``:  If
  condition is nonempty (or nonzero, if it’s a number), then returns the
  second argument. Otherwise, returns the third argument if specified (or
  nothing if falsetext is left off).
ifdef
  ``%ifdef{field}``, ``%ifdef{field,text}`` or
  ``%ifdef{field,text,falsetext}``:  If field exists, then return truetext or
  field (default). Otherwise, returns falsetext. The field should be entered
  without $.
ifdefempty
  ``%ifdefempty{field,text}`` or ``%ifdefempty{field,text,falsetext}``:  If
  field exists and is empty, then return truetext. Otherwise, returns
  falsetext. The field should be entered without $.
ifdefnotempty
  ``%ifdefnotempty{field,text}`` or ``%ifdefnotempty{field,text,falsetext}``:
  If field is not empty, then return truetext. Otherwise, returns falsetext.
  The field should be entered without $.
initial
  ``%initial{text}``:  Get the first character of a text in lowercase. The
  text is converted to ASCII. All non word characters are erased.
left
  ``%left{text,n}``:  Return the first “n” characters of “text”.
lower
  ``%lower{text}``:  Convert “text” to lowercase.
nowhitespace
  ``%nowhitespace{text,replace}``:  Replace all whitespace characters with
  ``replace``. By default: a dash (-) **Example:** ``%nowhitespace{$track,_}``
num
  ``%num{number,count}``:  Pad decimal number with leading zeros. **Example:**
  ``%num{$track,3}``
replchars
  ``%replchars{text,chars,replace}``:  Replace the characters “chars” in
  “text” with “replace”. **Example:** ``%replchars{text,ex,-}`` > ``t--t``
right
  ``%right{text,n}``:  Return the last “n” characters of “text”.
sanitize
  ``%sanitize{text}``:   Delete in most file systems not allowed characters.
shorten
  ``%shorten{text}`` or ``%shorten{text,max_size}``:  Shorten “text” on word
  boundarys. **Example:** ``%shorten{$title,32}``
time
  ``%time{date_time,format,curformat}``:  Return the date and time in any
  format accepted by strftime. For example, to get the year some music was
  added to your library, use %time{$added,%Y}.
title
  ``%title{text}``:  Convert “text” to Title Case.
upper
  ``%upper{text}``:  Convert “text” to UPPERCASE.

Plain text format:

:: 

    alpha
        -----

        ``%alpha{text}``
            This function first ASCIIfies the given text, then all non alphabet
            characters are replaced with whitespaces.

        alphanum
        --------

        ``%alphanum{text}``
            This function first ASCIIfies the given text, then all non alpanumeric
            characters are replaced with whitespaces.

        asciify
        -------

        ``%asciify{text}``
            Translate non-ASCII characters to their ASCII equivalents. For
            example, “café” becomes “cafe”. Uses the mapping provided by the
            unidecode module.

        delchars
        --------

        ``%delchars{text,chars}``
            Delete every single character of “chars“ in “text”.

        deldupchars
        -----------

        ``%deldupchars{text,chars}``
            Search for duplicate characters and replace with only one occurrance
            of this characters.

        first
        -----

        ``%first{text}`` or ``%first{text,count,skip}`` or
        ``%first{text,count,skip,sep,join}``
            Returns the first item, separated by ; . You can use
            %first{text,count,skip}, where count is the number of items (default
            1) and skip is number to skip (default 0). You can also use
            %first{text,count,skip,sep,join} where sep is the separator, like ; or
            / and join is the text to concatenate the items.

        if
        --

        ``%if{condition,truetext}`` or ``%if{condition,truetext,falsetext}``
            If condition is nonempty (or nonzero, if it’s a number), then returns
            the second argument. Otherwise, returns the third argument if
            specified (or nothing if falsetext is left off).

        ifdef
        -----

        ``%ifdef{field}``, ``%ifdef{field,text}`` or
        ``%ifdef{field,text,falsetext}``
            If field exists, then return truetext or field (default). Otherwise,
            returns falsetext. The field should be entered without $.

        ifdefempty
        ----------

        ``%ifdefempty{field,text}`` or ``%ifdefempty{field,text,falsetext}``
            If field exists and is empty, then return truetext. Otherwise, returns
            falsetext. The field should be entered without $.

        ifdefnotempty
        -------------

        ``%ifdefnotempty{field,text}`` or ``%ifdefnotempty{field,text,falsetext}``
            If field is not empty, then return truetext. Otherwise, returns
            falsetext. The field should be entered without $.

        initial
        -------

        ``%initial{text}``
            Get the first character of a text in lowercase. The text is converted
            to ASCII. All non word characters are erased.

        left
        ----

        ``%left{text,n}``
            Return the first “n” characters of “text”.

        lower
        -----

        ``%lower{text}``
            Convert “text” to lowercase.

        nowhitespace
        ------------

        ``%nowhitespace{text,replace}``
            Replace all whitespace characters with ``replace``. By default: a dash
            (-)
            ``%nowhitespace{$track,_}``

        num
        ---

        ``%num{number,count}``
            Pad decimal number with leading zeros.
            ``%num{$track,3}``

        replchars
        ---------

        ``%replchars{text,chars,replace}``
            Replace the characters “chars” in “text” with “replace”.
            ``%replchars{text,ex,-}`` > ``t--t``

        right
        -----

        ``%right{text,n}``
            Return the last “n” characters of “text”.

        sanitize
        --------

        ``%sanitize{text}``
             Delete in most file systems not allowed characters.

        shorten
        -------

        ``%shorten{text}`` or ``%shorten{text,max_size}``
            Shorten “text” on word boundarys.
            ``%shorten{$title,32}``

        time
        ----

        ``%time{date_time,format,curformat}``
            Return the date and time in any format accepted by strftime. For
            example, to get the year some music was added to your library, use
            %time{$added,%Y}.

        title
        -----

        ``%title{text}``
            Convert “text” to Title Case.

        upper
        -----

        ``%upper{text}``
            Convert “text” to UPPERCASE.

