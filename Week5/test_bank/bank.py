def main():
    greeting = input("Greeting: ").casefold().strip()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h") == True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
