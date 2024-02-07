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


def test_alpha() -> None:
    assert callable(alpha)


def test_alphanum() -> None:
    assert alphanum("a-b") == "a b"
    assert callable(alphanum)


def test_asciify() -> None:
    assert asciify("ä"), "ae"
    assert callable(asciify)


def test_delchars() -> None:
    assert delchars("a-b", "-") == "ab"
    assert callable(delchars)


def test_deldupchars() -> None:
    assert callable(deldupchars)


def test_first() -> None:
    assert callable(first)


def test_initial() -> None:
    assert callable(initial)


def test_left() -> None:
    assert callable(left)


def test_lower() -> None:
    assert callable(lower)


def test_num() -> None:
    assert callable(num)


def test_nowhitespace() -> None:
    assert callable(nowhitespace)


def test_replchars() -> None:
    assert callable(replchars)


def test_right() -> None:
    assert callable(right)


def test_sanitize() -> None:
    assert callable(sanitize)


def test_shorten() -> None:
    assert callable(shorten)


def test_time() -> None:
    assert callable(time)


def test_title() -> None:
    assert callable(title)


def test_upper() -> None:
    assert callable(upper)
