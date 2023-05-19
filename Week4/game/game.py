import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 100:
                x = random.randint((level + 1) - level, level)
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if guess < x:
                            print("Too small!")
                        elif guess > x:
                            print("Too large!")
                        else:
                            return print("Just right!")
                    except ValueError:
                        print()

        except (EOFError, ValueError):
            print()


if __name__ == "__main__":
    main()
