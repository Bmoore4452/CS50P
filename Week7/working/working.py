import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if x := re.search(
        r"(?:([0-9]|[1][0-9]):?([0-9][0-9])?) ([AM]{2}|[PM]{2}) (to) (?:([0-9]|[1][0-9]):?([0-9][0-9])?) ([AM]{2}|[PM]{2})",
        s,
    ):
        hour1, minute1, end1, to, hour2, minute2, end2 = (
            x.group(1),
            x.group(2),
            x.group(3),
            x.group(4),
            x.group(5),
            x.group(6),
            x.group(7),
        )

        # print(x.groups())

        if minute1 != None and minute2 != None:
            if int(minute1) >= 60 or int(minute2) >= 60:
                raise ValueError()
            if int(hour1) > 12 or int(hour2) > 12:
                raise ValueError()
            if to != "to":
                raise ValueError()
        else:
            minute1 = "00"
            minute2 = "00"

        first = hour1 + " " + end1
        second = hour2 + " " + end2

        if x:
            if "AM" in first:
                if hour1 == "12":
                    hour1 = "0"
                    return f"{int(hour1):02}:{minute1} to {int(hour2):02}:{minute2}"
            if "PM" in first:
                new = 12 + int(hour1)
                return f"{int(new):02}:{minute1} to {int(hour2):02}:{minute2}"
            elif "PM" in second:
                new2 = 12 + int(hour2)
                return f"{int(hour1):02}:{minute1} to {new2:02}:{minute2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
