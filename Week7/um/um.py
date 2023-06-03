import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    umcount = 0
    x = s.split(" ")
    for i in x:
        if re.findall("^um\W*$", i, re.IGNORECASE):
            umcount += 1
    return umcount


if __name__ == "__main__":
    main()
