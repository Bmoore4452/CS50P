from pyfiglet import Figlet
import sys
import random

fonts = [
    "banner",
    "avatar",
    "bell",
    "basic",
    "computer",
    "epic",
    "rectangles",
    "slant",
    "alphabet",
]

randfont = random.choice(fonts)


def main():
    if len(sys.argv) == 1:
        text = input("Input: ")
        f = Figlet(font=randfont)
        print(f.renderText(text))
    elif len(sys.argv) > 2 and len(sys.argv) < 4:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in fonts:
                text = input("Input: ")
                f = Figlet(font=sys.argv[2])
                print(f.renderText(text))
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
