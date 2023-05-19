import random


def main():
    get_level()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            return print()


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
