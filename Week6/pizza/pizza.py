import sys, csv, os.path
from tabulate import tabulate


def main():
    menu = []

    # Make sure that there cannot be less than one argument passed into the program
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # Make sure that there cannot be more than one arguement passed into the program
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Make sure that the file is a CSV file
    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV File")
    # Make sure that the file exists in the give directory
    if not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exit")
    else:
        # Open, read, and iterate through the file
        with open(sys.argv[1], "r") as file:
            read = csv.DictReader(file)
            for row in read:
                # Access the keys of the headers in the dictionary
                x = row.keys()
                # Convert the keys into a list
                y = list(x)
                headers = [y[0], y[1], y[2]]
                # Adds the rows to the menu
                menu.append([row[y[0]], row[y[1]], row[y[2]]])
            # Prints the menu to as a grid
            print(tabulate(menu, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
