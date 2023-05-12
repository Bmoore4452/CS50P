def main():
    get_fraction("Fraction: ")


def get_fraction(h):
    while True:
        try:
            fract = input(h)
            x, y = fract.split("/")
            z = round((int(x) / int(y)) * 100)
            if z == 100:
                return print("F")
            elif z == 0:
                return print("E")
            else:
                return print(f"{z}%")
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
