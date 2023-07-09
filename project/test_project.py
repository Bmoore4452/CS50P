from password import get_length, alpha, upper, number, special


def test_length():
    assert get_length(9) == 9


def test_alpha():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    assert alpha("y") == letters


def test_upper():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    uppercase = [x.upper() for x in letters]

    assert upper("y") == uppercase


def test_numbers():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    assert number("y") == numbers


def test_special():
    special_characters = [
        "'",
        '"',
        "!",
        "#",
        "$",
        "%",
        "&",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        ":",
        ";",
        "<",
        ">",
        "?",
        "@",
        "[",
        "]",
        "^",
        "_",
        "`",
        "{",
        "}",
        "|",
        "~",
        "=",
        "\\",
    ]
    assert special("y") == special_characters
