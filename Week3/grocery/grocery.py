def main():
    grocery_list = {}
    count = 0

    while True:
        try:
            item = input()
            if item not in grocery_list:
                count = 0
                count += 1
                grocery_list[item] = count

            else:
                count = grocery_list[item]
                count = int(count) + 1
                grocery_list[item] = count

        except (EOFError, KeyError):
            print()
            for i, j in sorted(grocery_list.items()):
                print(j, i.upper())
            return print()


main()
