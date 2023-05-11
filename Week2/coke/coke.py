def main():
    price = 50

    while price > 0:
        add_coin = int(input("Insert Coin: "))
        if add_coin == 5 or add_coin == 10 or add_coin == 25:
            price -= add_coin
        if price > 0:
            print(f"Amount Due: {price}")
        if price <= 0:
            print(f"Change Owed: {abs(price)}")


main()
