def main():
    text = input("Input: ")

    text_check(text)


def text_check(n):
    print("Output: ", end="")
    for i in n:
        print(i.strip("aeiou").strip("AEIOU"), end="")
    print()


main()
