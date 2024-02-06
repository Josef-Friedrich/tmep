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
