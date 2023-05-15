def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    price = 0

    while True:
        try:
            item = input("Item: ").title()

            x = menu.keys()
            y = menu.values()

            if item in x:
                price += float(menu[item])
                print(f"Total: ${format(price, '.2f')}")
        except (EOFError, KeyError):
            return print()


main()
