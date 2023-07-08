import random


def main():
    password_pool = []
    count = 0
    length = get_length()
    while count == 0:
        choice = alpha()
        if choice:
            password_pool.extend(choice)
            count += 1
        choice2 = upper()
        if choice2:
            count += 1
            password_pool.extend(choice2)
        choice3 = number()
        if choice3:
            count += 1
            password_pool.extend(choice3)
        choice4 = special()
        if choice4:
            count += 1
            password_pool.extend(choice4)
        if count != 0:
            y = "".join([random.choice(password_pool) for _ in range(length)])
            print("Password:", y)
        else:
            print("Please select at least one condition")


def get_length():
    while True:
        try:
            length = int(input("How many characters do you want in your password? "))
            if length < 8 or length > 128:
                print("Number must be between 8 and 128")
            else:
                return length
        except (ValueError, TypeError):
            print("Please choose a number between 8 and 128")


def alpha():
    while True:
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
        choice = input("Do you want lowercase letters in your password? ").casefold()
        if choice == "yes" or choice == "y":
            return letters
        elif choice == "no" or choice == "n":
            return
        else:
            print("Please answer yes or no")


def upper():
    while True:
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

        choice2 = input("Do you want uppercase letter in your password? ").casefold()

        if choice2 == "yes" or choice2 == "y":
            return uppercase
        elif choice2 == "no" or choice2 == "n":
            return
        else:
            print("Please answer yes or no")


def number():
    while True:
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        choice3 = input("Do you want numbers in your password? ").casefold()
        if choice3 == "yes" or choice3 == "y":
            return numbers
        elif choice3 == "no" or choice3 == "n":
            return
        else:
            print("Please answer yes or no")


def special():
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
    while True:
        choice4 = input("Do you want special characters in your password? ").casefold()
        if choice4 == "yes" or choice4 == "y":
            return special_characters
        elif choice4 == "no" or choice4 == "n":
            return
        else:
            print("Please answer yes or no")


if __name__ == "__main__":
    main()
