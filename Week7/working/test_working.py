from working import convert
import pytest


def test_default():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_more_minutes():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_many_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_middle():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
