from bank import value


def test_default():
    assert value("Hello") == 0

def test_partial():
    assert value("Hi") == 20

def test_full():
    assert value("What's up") == 100