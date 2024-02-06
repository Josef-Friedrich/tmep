Functions
=========

:: 

    - **alpha**: ``%alpha{text}``  This function first ASCIIfies the given text,
      then all non alphabet characters are replaced with whitespaces. Example:
      None
    - **alphanum**: ``%alphanum{text}``  This function first ASCIIfies the given
      text, then all non alpanumeric characters are replaced with whitespaces.
      Example: None
    - **asciify**: ``%asciify{text}``  Translate non-ASCII characters to their
      ASCII equivalents. For example, “café” becomes “cafe”. Uses the mapping
      provided by the unidecode module. Example: None
    - **delchars**: ``%delchars{text,chars}``  Delete every single character of
      “chars“ in “text”. Example: None
    - **deldupchars**: ``%deldupchars{text,chars}``  Search for duplicate
      characters and replace with only one occurrance of this characters. Example:
      None
    - **first**: ``%first{text}`` or ``%first{text,count,skip}`` or
      ``%first{text,count,skip,sep,join}``  Returns the first item, separated by ;
      . You can use %first{text,count,skip}, where count is the number of items
      (default 1) and skip is number to skip (default 0). You can also use
      %first{text,count,skip,sep,join} where sep is the separator, like ; or / and
      join is the text to concatenate the items. Example: None
    - **if**: ``%if{condition,truetext}`` or ``%if{condition,truetext,falsetext}``
      If condition is nonempty (or nonzero, if it’s a number), then returns the
      second argument. Otherwise, returns the third argument if specified (or
      nothing if falsetext is left off). Example: None
    - **ifdef**: ``%ifdef{field}``, ``%ifdef{field,text}`` or
      ``%ifdef{field,text,falsetext}``  If field exists, then return truetext or
      field (default). Otherwise, returns falsetext. The field should be entered
      without $. Example: None
    - **ifdefempty**: ``%ifdefempty{field,text}`` or
      ``%ifdefempty{field,text,falsetext}``  If field exists and is empty, then
      return truetext. Otherwise, returns falsetext. The field should be entered
      without $. Example: None
    - **ifdefnotempty**: ``%ifdefnotempty{field,text}`` or
      ``%ifdefnotempty{field,text,falsetext}``  If field is not empty, then return
      truetext. Otherwise, returns falsetext. The field should be entered without
      $. Example: None
    - **initial**: ``%initial{text}``  Get the first character of a text in
      lowercase. The text is converted to ASCII. All non word characters are
      erased. Example: None
    - **left**: ``%left{text,n}``  Return the first “n” characters of “text”.
      Example: None
    - **lower**: ``%lower{text}``  Convert “text” to lowercase. Example: None
    - **nowhitespace**: ``%nowhitespace{text,replace}``  Replace all whitespace
      characters with ``replace``. By default: a dash (-) Example:
      ``%nowhitespace{$track,_}``
    - **num**: ``%num{number,count}``  Pad decimal number with leading zeros.
      Example: ``%num{$track,3}``
    - **replchars**: ``%replchars{text,chars,replace}``  Replace the characters
      “chars” in “text” with “replace”. Example: ``%replchars{text,ex,-}`` > ``t--
      t``
    - **right**: ``%right{text,n}``  Return the last “n” characters of “text”.
      Example: None
    - **sanitize**: ``%sanitize{text}``   Delete in most file systems not allowed
      characters. Example: None
    - **shorten**: ``%shorten{text}`` or ``%shorten{text,max_size}``  Shorten
      “text” on word boundarys. Example: ``%shorten{$title,32}``
    - **time**: ``%time{date_time,format,curformat}``  Return the date and time in
      any format accepted by strftime. For example, to get the year some music was
      added to your library, use %time{$added,%Y}. Example: None
    - **title**: ``%title{text}``  Convert “text” to Title Case. Example: None
    - **upper**: ``%upper{text}``  Convert “text” to UPPERCASE. Example: None

