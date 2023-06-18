from jar import Jar


def test_init():
    jar = Jar(8)
    assert jar.capacity == 8
    assert jar.size == 0
    fulljar = Jar()
    assert fulljar.capacity == 12
    assert fulljar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    jar.deposit(2)
    assert jar.size == 10


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    jar.withdraw(2)
    assert jar.size == 6
