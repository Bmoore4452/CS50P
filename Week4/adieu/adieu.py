import inflect

p = inflect.engine()
name_list = []


def main():
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)

        except (EOFError, KeyError):
            print()
            t = p.join((name_list))
            print(f"Adieu, adieu, to {t}")
            return print()


if __name__ == "__main__":
    main()
