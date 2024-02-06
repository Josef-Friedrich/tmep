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
TMEP
====

TMEP (Template Macro Expansion for Paths) is a small template engine that
has been specially developed for file paths.

The engine can replace or expand symbols (or variables) like ``$title`` and
apply functions (or macros) like ``%upper{}`` in path templates.

The code comes from the `Beets project <https://beets.io/>`_ and was “extracted”
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

Template Symbols (or Variables)
  In path templates, symbols or varialbes such as ``$title``
  (any name with the prefix ``$``) are replaced by the corresponding value.

  Because ``$`` is used to delineate a field reference, you can use ``$$`` to emit
  a dollars sign. As with `Python template strings`_, ``${title}`` is equivalent
  to ``$title``; you can use this if you need to separate a field name from the
  text that follows it.

.. _Python template strings: https://docs.python.org/library/string.html#template-strings

Template Functions (or Macros)
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

reStructuredText format (``tmep-doc --functions-rst``):

:: 

    alpha
      ``%alpha{text}``:  This function first ASCIIfies the given text, then all
      non alphabet characters are replaced with whitespaces.

      **Example:** ``%alpha{a1b23c}`` → ``a b c``

    alphanum
      ``%alphanum{text}``:  This function first ASCIIfies the given text, then all
      non alpanumeric characters are replaced with whitespaces.

      **Example:** ``%alphanum{après-évêque1}`` → ``apres eveque1``

    asciify
      ``%asciify{text}``:  Translate non-ASCII characters to their ASCII
      equivalents. For example, “café” becomes “cafe”. Uses the mapping provided
      by the unidecode module.

      **Example:** ``%asciify{äÄöÖüÜ}`` → ``aeAeoeOeueUe``

    delchars
      ``%delchars{text,chars}``:  Delete every single character of “chars“ in
      “text”.

      **Example:** ``%delchars{Schubert, ue}`` → ``Schbrt``

    deldupchars
      ``%deldupchars{text,chars}``:  Search for duplicate characters and replace
      with only one occurrance of this characters.

      **Example:** ``%deldupchars{a---b___c...d}`` → ``a-b_c.d``; ``%deldupchars{a
      ---b___c, -}`` → ``a-b___c``

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

      **Example:** ``%initial{Schubert}`` → ``s``

    left
      ``%left{text,n}``:  Return the first “n” characters of “text”.

      **Example:** ``%left{Schubert, 3}`` → ``Sch``

    lower
      ``%lower{text}``:  Convert “text” to lowercase.

      **Example:** ``%lower{SCHUBERT}`` → ``schubert``

    nowhitespace
      ``%nowhitespace{text,replace}``:  Replace all whitespace characters with
      ``replace``. By default: a dash (``-``)

      **Example:** ``%nowhitespace{a b}`` → ``a-b``; ``%nowhitespace{a b, _}`` →
      ``a_b``

    num
      ``%num{number,count}``:  Pad decimal number with leading zeros.

      **Example:** ``%num{7,3}`` → ``007``

    replchars
      ``%replchars{text,chars,replace}``:  Replace the characters “chars” in
      “text” with “replace”.

      **Example:** ``%replchars{Schubert,-,ue}`` → ``Sch-b-rt``

    right
      ``%right{text,n}``:  Return the last “n” characters of “text”.

      **Example:** ``%right{Schubert,3}`` → ``ert``

    sanitize
      ``%sanitize{text}``:  Delete characters that are not allowed in most file
      systems.

      **Example:** ``%sanitize{x:*?<>|/~&x}`` → ``xx``

    shorten
      ``%shorten{text}`` or ``%shorten{text,max_size}``:  Shorten “text” on word
      boundarys.

      **Example:** ``%shorten{Lorem ipsum dolor sit, 10}`` → ``Lorem``

    time
      ``%time{date_time,format,curformat}``:  Return the date and time in any
      format accepted by ``strftime``. For example, to get the year, use
      ``%time{$added,%Y}``.

      **Example:** ``%time{30 Nov 2024,%Y,%d %b %Y}`` → ``2024``

    title
      ``%title{text}``:  Convert “text” to Title Case.

      **Example:** ``%title{franz schubert}`` → ``Franz Schubert``

    upper
      ``%upper{text}``:  Convert “text” to UPPERCASE.

      **Example:** ``%upper{foo}`` → ``FOO``

alpha
  ``%alpha{text}``:  This function first ASCIIfies the given text, then all
  non alphabet characters are replaced with whitespaces.

  **Example:** ``%alpha{a1b23c}`` → ``a b c``

alphanum
  ``%alphanum{text}``:  This function first ASCIIfies the given text, then all
  non alpanumeric characters are replaced with whitespaces.

  **Example:** ``%alphanum{après-évêque1}`` → ``apres eveque1``

asciify
  ``%asciify{text}``:  Translate non-ASCII characters to their ASCII
  equivalents. For example, “café” becomes “cafe”. Uses the mapping provided
  by the unidecode module.

  **Example:** ``%asciify{äÄöÖüÜ}`` → ``aeAeoeOeueUe``

delchars
  ``%delchars{text,chars}``:  Delete every single character of “chars“ in
  “text”.

  **Example:** ``%delchars{Schubert, ue}`` → ``Schbrt``

deldupchars
  ``%deldupchars{text,chars}``:  Search for duplicate characters and replace
  with only one occurrance of this characters.

  **Example:** ``%deldupchars{a---b___c...d}`` → ``a-b_c.d``; ``%deldupchars{a
  ---b___c, -}`` → ``a-b___c``

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

  **Example:** ``%initial{Schubert}`` → ``s``

left
  ``%left{text,n}``:  Return the first “n” characters of “text”.

  **Example:** ``%left{Schubert, 3}`` → ``Sch``

lower
  ``%lower{text}``:  Convert “text” to lowercase.

  **Example:** ``%lower{SCHUBERT}`` → ``schubert``

nowhitespace
  ``%nowhitespace{text,replace}``:  Replace all whitespace characters with
  ``replace``. By default: a dash (``-``)

  **Example:** ``%nowhitespace{a b}`` → ``a-b``; ``%nowhitespace{a b, _}`` →
  ``a_b``

num
  ``%num{number,count}``:  Pad decimal number with leading zeros.

  **Example:** ``%num{7,3}`` → ``007``

replchars
  ``%replchars{text,chars,replace}``:  Replace the characters “chars” in
  “text” with “replace”.

  **Example:** ``%replchars{Schubert,-,ue}`` → ``Sch-b-rt``

right
  ``%right{text,n}``:  Return the last “n” characters of “text”.

  **Example:** ``%right{Schubert,3}`` → ``ert``

sanitize
  ``%sanitize{text}``:  Delete characters that are not allowed in most file
  systems.

  **Example:** ``%sanitize{x:*?<>|/~&x}`` → ``xx``

shorten
  ``%shorten{text}`` or ``%shorten{text,max_size}``:  Shorten “text” on word
  boundarys.

  **Example:** ``%shorten{Lorem ipsum dolor sit, 10}`` → ``Lorem``

time
  ``%time{date_time,format,curformat}``:  Return the date and time in any
  format accepted by ``strftime``. For example, to get the year, use
  ``%time{$added,%Y}``.

  **Example:** ``%time{30 Nov 2024,%Y,%d %b %Y}`` → ``2024``

title
  ``%title{text}``:  Convert “text” to Title Case.

  **Example:** ``%title{franz schubert}`` → ``Franz Schubert``

upper
  ``%upper{text}``:  Convert “text” to UPPERCASE.

  **Example:** ``%upper{foo}`` → ``FOO``

Plain text format (``tmep-doc --functions-txt``):

:: 

    alpha
        -----

        ``%alpha{text}``
            This function first ASCIIfies the given text, then all non alphabet
            characters are replaced with whitespaces.
            ``%alpha{a1b23c}`` → ``a b c``

        alphanum
        --------

        ``%alphanum{text}``
            This function first ASCIIfies the given text, then all non alpanumeric
            characters are replaced with whitespaces.
            ``%alphanum{après-évêque1}`` → ``apres eveque1``

        asciify
        -------

        ``%asciify{text}``
            Translate non-ASCII characters to their ASCII equivalents. For
            example, “café” becomes “cafe”. Uses the mapping provided by the
            unidecode module.
            ``%asciify{äÄöÖüÜ}`` → ``aeAeoeOeueUe``

        delchars
        --------

        ``%delchars{text,chars}``
            Delete every single character of “chars“ in “text”.
            ``%delchars{Schubert, ue}`` → ``Schbrt``

        deldupchars
        -----------

        ``%deldupchars{text,chars}``
            Search for duplicate characters and replace with only one occurrance
            of this characters.
            ``%deldupchars{a---b___c...d}`` → ``a-b_c.d``; ``%deldupchars{a---
            b___c, -}`` → ``a-b___c``

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
            ``%initial{Schubert}`` → ``s``

        left
        ----

        ``%left{text,n}``
            Return the first “n” characters of “text”.
            ``%left{Schubert, 3}`` → ``Sch``

        lower
        -----

        ``%lower{text}``
            Convert “text” to lowercase.
            ``%lower{SCHUBERT}`` → ``schubert``

        nowhitespace
        ------------

        ``%nowhitespace{text,replace}``
            Replace all whitespace characters with ``replace``. By default: a dash
            (``-``)
            ``%nowhitespace{a b}`` → ``a-b``; ``%nowhitespace{a b, _}`` → ``a_b``

        num
        ---

        ``%num{number,count}``
            Pad decimal number with leading zeros.
            ``%num{7,3}`` → ``007``

        replchars
        ---------

        ``%replchars{text,chars,replace}``
            Replace the characters “chars” in “text” with “replace”.
            ``%replchars{Schubert,-,ue}`` → ``Sch-b-rt``

        right
        -----

        ``%right{text,n}``
            Return the last “n” characters of “text”.
            ``%right{Schubert,3}`` → ``ert``

        sanitize
        --------

        ``%sanitize{text}``
            Delete characters that are not allowed in most file systems.
            ``%sanitize{x:*?<>|/~&x}`` → ``xx``

        shorten
        -------

        ``%shorten{text}`` or ``%shorten{text,max_size}``
            Shorten “text” on word boundarys.
            ``%shorten{Lorem ipsum dolor sit, 10}`` → ``Lorem``

        time
        ----

        ``%time{date_time,format,curformat}``
            Return the date and time in any format accepted by ``strftime``. For
            example, to get the year, use ``%time{$added,%Y}``.
            ``%time{30 Nov 2024,%Y,%d %b %Y}`` → ``2024``

        title
        -----

        ``%title{text}``
            Convert “text” to Title Case.
            ``%title{franz schubert}`` → ``Franz Schubert``

        upper
        -----

        ``%upper{text}``
            Convert “text” to UPPERCASE.
            ``%upper{foo}`` → ``FOO``

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
