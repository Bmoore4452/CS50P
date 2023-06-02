from numb3rs import validate


def test_default():
    assert validate("127.0.0.1") == True


def test_letters():
    assert validate("cat") == False


def test_too_high():
    assert validate("277.0.0.1") == False


def test_too_high2():
    assert validate("1.2.3.1000") == False


def test_first():
    assert validate("500.1.1.1") == False
    assert validate("1.500.1.1") == False
