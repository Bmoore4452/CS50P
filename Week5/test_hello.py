from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["Brian", "LaToya", "Moore"]:
        assert hello(name) == f"hello, {name}"
