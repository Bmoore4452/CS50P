def main():
    b = input("Fraction: ")
    c = convert(b)
    return print(guage(c))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            z = round(((x) / (y)) * 100)
            return z
        except (ValueError, ZeroDivisionError):
            raise


def guage(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}"


if __name__ == "__main__":
    main()
