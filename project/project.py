import random

password_pool = []
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

count = 0

uppercase = [x.upper() for x in letters]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

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


def main():
    length_of_password = get_length()
    while count == 0:
        alpha()
        upper()
        number()
        special()
        if count != 0:
            y = random.sample(population=password_pool, k=length_of_password)
            print("Password: ", *y, sep="")
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
        except ValueError:
            print("Please choose a number between 8 and 128")


def alpha():
    while True:
        global count
        choice = input("Do you want lowercase letters in your password? ").casefold()
        if choice == "yes" or choice == "y":
            password_pool.extend(letters)
            count += 1
            return password_pool, count
        elif choice == "no" or choice == "n":
            return password_pool
        else:
            print("Please answer yes or no")


def upper():
    while True:
        global count
        choice2 = input("Do you want uppercase letter in your password? ").casefold()
        if choice2 == "yes" or choice2 == "y":
            password_pool.extend(uppercase)
            count += 1
            return password_pool, count
        elif choice2 == "no" or choice2 == "n":
            return password_pool
        else:
            print("Please answer yes or no")


def number():
    while True:
        global count
        choice3 = input("Do you want numbers in your password? ").casefold()
        if choice3 == "yes" or choice3 == "y":
            password_pool.extend(numbers)
            count += 1
            return password_pool, count
        elif choice3 == "no" or choice3 == "n":
            return password_pool
        else:
            print("Please answer yes or no")


def special():
    while True:
        global count
        choice4 = input("Do you want special characters in your password? ").casefold()
        if choice4 == "yes" or choice4 == "y":
            password_pool.extend(special_characters)
            count += 1
            return password_pool, count
        elif choice4 == "no" or choice4 == "n":
            return password_pool
        else:
            print("Please answer yes or no")


if __name__ == "__main__":
    main()
