def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    number = d.strip("$")
    return float(number)


def percent_to_float(p):
    number = p.strip("%")
    return float(int(number) / 100)


main()
