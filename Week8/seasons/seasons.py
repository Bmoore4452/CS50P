from datetime import date, timedelta, datetime
import inflect, sys

p = inflect.engine()


def main():
    birthday = input("Date of Birth: ")
    print(time_alive(birthday))


def time_alive(birthday):
    try:
        year, month, day = birthday.split("-")
        x = date(int(year), int(month), int(day))
        today = date.today()
        # Amount of days between date
        y = today - x
        # Convert days to years
        z = (y.days / 365) * 525600
        # Convert out rounded minutes into words
        minutes = p.number_to_words(round(z), andword="").capitalize()
    except:
        sys.exit("Invalid date")
    else:
        return f"{minutes} minutes"


if __name__ == "__main__":
    main()
