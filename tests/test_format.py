from tmep.format import (
    alpha,
    alphanum,
    asciify,
    delchars,
    deldupchars,
    first,
    initial,
    left,
    lower,
    nowhitespace,
    num,
    replchars,
    right,
    sanitize,
    shorten,
    time,
    title,
    upper,
)


class TestFormatFunctions:
    def test_alpha(self):
        assert callable(alpha)

    def test_alphanum(self):
        assert alphanum("a-b") == "a b"
        assert callable(alphanum)

    def test_asciify(self):
        assert asciify("ä"), "ae"
        assert callable(asciify)

    def test_delchars(self):
        assert delchars("a-b", "-") == "ab"
        assert callable(delchars)

    def test_deldupchars(self):
        assert callable(deldupchars)

    def test_first(self):
        assert callable(first)

    def test_initial(self):
        assert callable(initial)

    def test_left(self):
        assert callable(left)

    def test_lower(self):
        assert callable(lower)

    def test_num(self):
        assert callable(num)

    def test_nowhitespace(self):
        assert callable(nowhitespace)

    def test_replchars(self):
        assert callable(replchars)

    def test_right(self):
        assert callable(right)

    def test_sanitize(self):
        assert callable(sanitize)

    def test_shorten(self):
        assert callable(shorten)

    def test_time(self):
        assert callable(time)

    def test_title(self):
        assert callable(title)

    def test_upper(self):
        assert callable(upper)
