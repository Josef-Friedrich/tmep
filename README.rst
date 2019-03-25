.. image:: http://img.shields.io/pypi/v/tmep.svg
    :target: https://pypi.python.org/pypi/tmep
    :alt: This package on the Python Package Index

.. image:: https://travis-ci.org/Josef-Friedrich/tmep.svg?branch=master
    :target: https://travis-ci.org/Josef-Friedrich/tmep
    :alt: Continuous integration

.. image:: https://readthedocs.org/projects/tmep/badge/?version=latest
    :target: https://tmep.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

====
tmep
====

Template and Macros Expansion for Path names.

Installation
============

From Github
------------

.. code:: Shell

    git clone https://github.com/Josef-Friedrich/tmep.git
    cd tmep
    python setup.py install

From PyPI
----------

.. code:: Shell

    pip install tmep
    easy_install tmep

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

    tox


Publish a new version
---------------------

::

    git tag 1.1.1
    git push --tags
    python setup.py sdist upload


Package documentation
---------------------

The package documentation is hosted on
`readthedocs <http://tmep.readthedocs.io>`_.

Generate the package documentation:

::

    python setup.py build_sphinx


Functions
=========

.. code ::

    alpha
    -----

    %alpha{text}
        This function first ASCIIfies the given text, then all non alphabet
        characters are replaced with whitespaces.

    alphanum
    --------

    %alphanum{text}
        This function first ASCIIfies the given text, then all non alpanumeric
        characters are replaced with whitespaces.

    asciify
    -------

    %asciify{text}
        Translate non-ASCII characters to their ASCII equivalents. For
        example, “café” becomes “cafe”. Uses the mapping provided by the
        unidecode module.

    delchars
    --------

    %delchars{text,chars}
        Delete every single character of “chars“ in “text”.

    deldupchars
    -----------

    %deldupchars{text,chars}
        Search for duplicate characters and replace with only one occurrance
        of this characters.

    first
    -----

    %first{text} or %first{text,count,skip} or
    %first{text,count,skip,sep,join}
        Returns the first item, separated by ; . You can use
        %first{text,count,skip}, where count is the number of items (default
        1) and skip is number to skip (default 0). You can also use
        %first{text,count,skip,sep,join} where sep is the separator, like ; or
        / and join is the text to concatenate the items.

    if
    --

    %if{condition,truetext} or %if{condition,truetext,falsetext}
        If condition is nonempty (or nonzero, if it’s a number), then returns
        the second argument. Otherwise, returns the third argument if
        specified (or nothing if falsetext is left off).

    ifdef
    -----

    %ifdef{field}, %ifdef{field,text} or %ifdef{field,text,falsetext}
        If field exists, then return truetext or field (default). Otherwise,
        returns falsetext. The field should be entered without $.

    ifdefempty
    ----------

    %ifdefempty{field,text} or %ifdefempty{field,text,falsetext}
        If field exists and is empty, then return truetext. Otherwise, returns
        falsetext. The field should be entered without $.

    ifdefnotempty
    -------------

    %ifdefnotempty{field,text} or %ifdefnotempty{field,text,falsetext}
        If field is not empty, then return truetext. Otherwise, returns
        falsetext. The field should be entered without $.

    initial
    -------

    %initial{text}
        Get the first character of a text in lowercase. The text is converted
        to ASCII. All non word characters are erased.

    left
    ----

    %left{text,n}
        Return the first “n” characters of “text”.

    lower
    -----

    %lower{text}
        Convert “text” to lowercase.

    nowhitespace
    ------------

    %nowhitespace{text,replace}
        Replace all whitespace characters with replace. By default: a dash (-)
        %nowhitespace{$track,_}

    num
    ---

    %num{number,count}
        Pad decimal number with leading zeros.
        %num{$track,3}

    replchars
    ---------

    %replchars{text,chars,replace}
        Replace the characters “chars” in “text” with “replace”.
        %replchars{text,ex,-} > t--t

    right
    -----

    %right{text,n}
        Return the last “n” characters of “text”.

    sanitize
    --------

    %sanitize{text}
        Delete in most file systems not allowed characters.

    shorten
    -------

    %shorten{text} or %shorten{text,max_size}
        Shorten “text” on word boundarys.
        %shorten{$title,32}

    time
    ----

    %time{date_time,format,curformat}
        Return the date and time in any format accepted by strftime. For
        example, to get the year some music was added to your library, use
        %time{$added,%Y}.

    title
    -----

    %title{text}
        Convert “text” to Title Case.

    upper
    -----

    %upper{text}
        Convert “text” to UPPERCASE.


