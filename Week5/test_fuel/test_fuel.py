import pytest
from fuel import convert, gauge


def test_default():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("0/100") == 0 and gauge(0) == "E"
    assert convert("4/4") == 100 and gauge(100) == "F"
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_string():
    with pytest.raises(ValueError):
        convert("boy/girl")
