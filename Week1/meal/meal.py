def main():
    time = input("What time is it? ").strip()
    hours, minutes = time.split(":")
    if (int(hours) == 7 and (int(minutes) >= 0 or int(minutes) <= 59)) or (
        int(hours) == 8 and int(minutes) == 0
    ):
        print("breakfast time")
    if (int(hours) == 12 and (int(minutes) >= 0 or int(minutes) <= 59)) or (
        int(hours) == 13 and int(minutes) == 0
    ):
        print("lunch time")
    if (int(hours) == 18 and (int(minutes) >= 0 or int(minutes) <= 59)) or (
        int(hours) == 19 and int(minutes) == 0
    ):
        print("dinner time")
    convert(time)

def convert(time):
    hour2, minute2 = time.split(":")

    converted = (float(minute2) / 60) + float(hour2)
    return print(round(converted, 2))


if __name__ == "__main__":
    main()
