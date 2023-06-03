import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # initiates the umcount variable and sets it to zero
    umcount = 0
    # split the string into a list by any single space
    x = s.split(" ")
    # interate through the list
    for i in x:
        # check each string in the list for match
        if re.findall("^um\W*$", i, re.IGNORECASE):
            # increments umcount if the match is found
            umcount += 1
    return umcount


if __name__ == "__main__":
    main()
