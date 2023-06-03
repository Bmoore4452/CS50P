from um import count


def test_default():
    assert count("um") == 1


def test_spec():
    assert count("um?") == 1


def test_inside():
    assert count("Um, thanks for the album.") == 1


def test_extra_punc():
    assert count("Um, thanks, um...,") == 2


