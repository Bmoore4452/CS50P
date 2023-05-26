from twttr import shorten
import pytest


def test_lower():
    assert shorten("twitter") == "twttr"


def test_upper():
    assert shorten("TWITTER") == "TWTTR"


def test_number():
    assert shorten("twitter9") == "twttr9"


def test_punc():
    assert shorten("twitter!") == "twttr!"
