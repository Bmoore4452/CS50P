def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    slash = "/"
    comma = ","

    while True:
        try:
            date = input("Date: ").strip()
            if slash in date:
                x, y, z = date.split("/")
                if int(x) < 12:
                    if int(y) < 30:
                        if int(x) < 10 and int(y) < 10:
                            return print(f"{z}-0{x}-0{y}")
                        elif int(y) < 10:
                            return print(f"{z}-{x}-0{y}")
                        elif int(x) < 10:
                            return print(f"{z}-0{x}-{y}")
                        else:
                            return print(f"{z}-{x}-{y}")
            elif comma in date:
                x, y, z = date.split(" ")
                if x in months:
                    x = months.index(x)
                    y = y.strip(",")
                    if int(x) < 12:
                        if int(y) < 30:
                            if int(x) < 10 and int(y) < 10:
                                return print(f"{z}-{x+1:02}-0{y}")
                            elif int(y) < 10:
                                return print(f"{z}-{x+1}-0{y}")
                            elif int(x) < 10:
                                return print(f"{z}-{x+1}-{y}")
                            else:
                                return print(f"{z}-{x+1}-{y}")
        except ValueError:
            pass


main()
