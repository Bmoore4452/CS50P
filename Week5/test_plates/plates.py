def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if input length is more than two and less than six
    if not (len(s) <= 6 and len(s) >= 2):
        return False
    # Check if the input does not contain special characters
    if s.isalnum() == False:
        return False
    # Check if the first character is 0
    if s[0] != 0:
        if s[0].isdigit() == True or s[1].isdigit() == True:
            return False
    # If a number is found make sure the rest of the string is also a number
    for i in range(len(s)):
        if s[i] == "0":
            if s[i:] != "0":
                return False
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
    else:
        return True


if __name__ == "__main__":
    main()
