Functions
=========

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
  ``;``. You can use ``%first{text,count,skip}``, where count is the number of
  items (default 1) and skip is number to skip (default 0). You can also use
  ``%first{text,count,skip,sep,join}`` where ``sep`` is the separator, like
  ``;`` or ``/`` and join is the text to concatenate the items.

  **Example:** ``%first{Alice / Bob / Eve,2,0, / , & }`` → ``Alice & Bob``

if
  ``%if{condition,trueval}`` or ``%if{condition,trueval,falseval}``:  If
  condition is nonempty (or nonzero, if it’s a number), then returns the
  second argument. Otherwise, returns the third argument if specified (or
  nothing if ``falseval`` is left off).

  **Example:** ``x%if{false,foo}`` → ``x``

ifdef
  ``%ifdef{field}``, ``%ifdef{field,trueval}`` or
  ``%ifdef{field,trueval,falseval}``:  If field exists, then return
  ``trueval`` or field (default). Otherwise, returns ``falseval``. The field
  should be entered without ``$``.

  **Example:** ``%ifdef{compilation,Compilation}``

ifdefempty
  ``%ifdefempty{field,text}`` or ``%ifdefempty{field,text,falsetext}``:  If
  field exists and is empty, then return ``truetext``. Otherwise, returns
  ``falsetext``. The field should be entered without ``$``.

  **Example:** ``%ifdefempty{compilation,Album,Compilation}``

ifdefnotempty
  ``%ifdefnotempty{field,text}`` or ``%ifdefnotempty{field,text,falsetext}``:
  If field is not empty, then return ``truetext``. Otherwise, returns
  ``falsetext``. The field should be entered without ``$``.

  **Example:** ``%ifdefnotempty{compilation,Compilation,Album}``

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
