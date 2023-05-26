# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))


# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's your name? ")

# # file = open("names.txt", "w") # w to write

# with open("names.txt", "a") as file: # "a" appends or adds to the file
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())


# Accumulate the names into a list, then sort them, then print them
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
