def main():
    word = camel(input("camelCase: "))


def camel(c):
    print("snake_case: ", end="")
    for i in c:
        if i.islower():
            print(i, end="")
        elif i.isupper():
            print("_", end="")
            print(i.casefold(), end="")
    print()


main()
