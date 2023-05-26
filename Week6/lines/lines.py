import sys
import os.path

count = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python File")
if not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exit")
else:
    with open(sys.argv[1]) as file:
        for line in file:
            if not line.lstrip().startswith("#") and line.lstrip():
                count += 1
        print(count)
