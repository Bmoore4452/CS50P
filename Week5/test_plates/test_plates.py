from plates import is_valid


def test_plates_default():
    assert is_valid("bm4452") == True


def test_num_after():
    assert is_valid("b445m2") == False


def test_num_first():
    assert is_valid("4bm") == False


def test_letters_first():
    assert is_valid("bm44") == True


def test_spec():
    assert is_valid("bm.445") == False


def test_zero_first():
    assert is_valid("2bfbc") == False


def test_zero_inside():
    assert is_valid("bm0445") == False


def test_length_short():
    assert is_valid("b") == False


def test_length_long():
    assert is_valid("bmoore4452") == False
