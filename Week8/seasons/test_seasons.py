from seasons import time_alive
import inflect, pytest, sys

p = inflect.engine()


def test_default():
    assert (
        time_alive("1999-01-01")
        == "Twelve million, eight hundred fifty-two thousand minutes"
    )


def test_word_date():
    with pytest.raises(SystemExit):
        assert time_alive("January 1, 1999")
    # assert time_alive("January 1, 1999") == SystemExit("Invalid date")
