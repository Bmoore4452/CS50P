def main():
        b = input("Fraction: ")
        c = convert(b)
        print(gauge(c))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            z = round((int(x) / int(y)) * 100)
            return z
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
        if percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
        else:
            return f"{percentage}%"



if __name__ == "__main__":
    main()
