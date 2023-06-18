class Jar:
    def __init__(
        self,
        capacity=12,
    ):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n > self.capacity or n + self._size > self.capacity:
            raise ValueError
        self._size = self._size + n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(8)
    jar.deposit(2)
    # jar.withdraw(1)
    # print(jar.capacity)
    # print(f"{('🍪')*(jar.size)}")
    print(jar.size)
    print(jar.capacity)



if __name__ == "__main__":
    main()
