import json
import requests
import sys


def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        elif sys.argv[1].isalpha() == True:
            sys.exit("Commad-line argument is not a number")
        else:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            rate = o["bpi"]["USD"]["rate_float"]
            print(f"${rate * float(sys.argv[1]):,}")

    except requests.RequestException:
        return


if __name__ == "__main__":
    main()
