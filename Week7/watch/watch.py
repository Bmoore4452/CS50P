import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    x = re.search(r'.+src="https?://(?:www\.)?youtube\.com/embed/(\w+)"', s)
    if x:
        return "https://youtu.be/" + x.group(1)
    else:
        return


if __name__ == "__main__":
    main()
