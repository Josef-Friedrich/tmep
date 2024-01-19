Path Formats
============

The ``paths:`` section of the config file (see :doc:`config`) lets
you specify the directory and file naming scheme for your music library.
Templates substitute symbols like ``$title`` (any field value prefixed by ``$``)
with the appropriate value from the track's metadata. Beets adds the filename
extension automatically.

For example, consider this path format string:
``$albumartist/$album/$track $title``

Here are some paths this format will generate:

* ``Yeah Yeah Yeahs/It's Blitz!/01 Zero.mp3``

* ``Spank Rock/YoYoYoYoYo/11 Competition.mp3``

* ``The Magnetic Fields/Realism/01 You Must Be Out of Your Mind.mp3``

Because ``$`` is used to delineate a field reference, you can use ``$$`` to emit
a dollars sign. As with `Python template strings`_, ``${title}`` is equivalent
to ``$title``; you can use this if you need to separate a field name from the
text that follows it.

.. _Python template strings: https://docs.python.org/library/string.html#template-strings

.. _template-functions:

Template Functions
------------------

Beets path formats also support *function calls*, which can be used to transform
text and perform logical manipulations. The syntax for function calls is like
this: ``%func{arg,arg}``. For example, the ``upper`` function makes its argument
upper-case, so ``%upper{beets rocks}`` will be replaced with ``BEETS ROCKS``.
You can, of course, nest function calls and place variable references in
function arguments, so ``%upper{$artist}`` becomes the upper-case version of the
track's artists.

These functions are built in to beets:

* ``%lower{text}``: Convert ``text`` to lowercase.
* ``%upper{text}``: Convert ``text`` to UPPERCASE.
* ``%title{text}``: Convert ``text`` to Title Case.
* ``%left{text,n}``: Return the first ``n`` characters of ``text``.
* ``%right{text,n}``: Return the last ``n`` characters of  ``text``.
* ``%if{condition,text}`` or ``%if{condition,truetext,falsetext}``: If
  ``condition`` is nonempty (or nonzero, if it's a number), then returns
  the second argument. Otherwise, returns the third argument if specified (or
  nothing if ``falsetext`` is left off).
* ``%asciify{text}``: Convert non-ASCII characters to their ASCII equivalents.
  For example, "café" becomes "cafe". Uses the mapping provided by the
  `unidecode module`_. See the :ref:`asciify-paths` configuration
  option.
* ``%aunique{identifiers,disambiguators,brackets}``: Provides a unique string
  to disambiguate similar albums in the database. See :ref:`aunique`, below.
* ``%sunique{identifiers,disambiguators,brackets}``: Similarly, a unique string
  to disambiguate similar singletons in the database. See :ref:`sunique`, below.
* ``%time{date_time,format}``: Return the date and time in any format accepted
  by `strftime`_. For example, to get the year some music was added to your
  library, use ``%time{$added,%Y}``.
* ``%first{text}``: Returns the first item, separated by ``;`` (a semicolon
  followed by a space).
  You can use ``%first{text,count,skip}``, where ``count`` is the number of
  items (default 1) and ``skip`` is number to skip (default 0). You can also use
  ``%first{text,count,skip,sep,join}`` where ``sep`` is the separator, like
  ``;`` or ``/`` and join is the text to concatenate the items.
* ``%ifdef{field}``, ``%ifdef{field,truetext}`` or
  ``%ifdef{field,truetext,falsetext}``: Checks if an flexible attribute
  ``field`` is defined. If it exists, then return ``truetext`` or ``field``
  (default). Otherwise, returns ``falsetext``. The ``field`` should be entered
  without ``$``. Note that this doesn't work with built-in :ref:`itemfields`, as
  they are always defined.

.. _unidecode module: https://pypi.org/project/Unidecode
.. _strftime: https://docs.python.org/3/library/time.html#time.strftime



Syntax Details
--------------

The characters ``$``, ``%``, ``{``, ``}``, and ``,`` are "special" in the path
template syntax. This means that, for example, if you want a ``%`` character to
appear in your paths, you'll need to be careful that you don't accidentally
write a function call. To escape any of these characters (except ``{``, and
``,`` outside a function argument), prefix it with a ``$``.  For example,
``$$`` becomes ``$``; ``$%`` becomes ``%``, etc. The only exceptions are:

* ``${``, which is ambiguous with the variable reference syntax (like
  ``${title}``). To insert a ``{`` alone, it's always sufficient to just type
  ``{``.
* commas are used as argument separators in function calls. Inside of a
  function's argument, use ``$,`` to get a literal ``,`` character. Outside of
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


.. _itemfields:

Available Values
----------------

Here's a list of the different values available to path formats. The current
list can be found definitively by running the command ``beet fields``. Note that
plugins can add new (or replace existing) template values (see
:ref:`templ_plugins`).
