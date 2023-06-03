import validators


def main():
    x = input("What's you email address? ")
    if validators.email(x):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
