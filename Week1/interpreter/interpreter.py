def main():
    txt = input("Expression: ")

    x, y, z = txt.split(" ")
    if y == "+":
        add = float(x) + float(z)
        print(round(add, 1))
    if y == "-":
        subtract = float(x) - float(z)
        print(round(subtract, 1))
    if y == "*":
        product = float(x) * float(z)
        print(round(product, 1))
    if y == "/":
        divide = float(x) / float(z)
        print(round(divide, 1))


main()
