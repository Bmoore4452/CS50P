import sys


def main():
    text = input("Input: ")

    print("Output:", shorten(text))


def shorten(word):
    x = []
    for i in word:
        x.append(i.strip("aeiou").strip("AEIOU"))
    y = "".join(x)
    return y


if __name__ == "__main__":
    main()
