import random


def main():
    g = get_level()
    generate_integer(g)


def get_level():
    digits = ["1", "2", "3"]
    while True:
        level = input("Level: ")
        if level not in digits:
            continue
        return level


def generate_integer(level):
    score = 0
    for i in range(10):
        wrong = 0
        if level == "1":
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            z = x + y
        elif level == "2":
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            z = x + y
        elif level == "3":
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            z = x + y
        while True:
            print(f"{x} + {y} = ", end="")
            answer = input()
            if answer == str(x + y):
                score += 1
                break
            elif answer != str(x + y) and wrong != 3:
                wrong += 1
                print("EEE")
                if wrong == 3:
                    print(f"{x} + {y} = {z}", end="")
                    print()
                    break
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
