def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_length(s):
        if check_order(s):
            return True


def check_length(s):
    if len(s) <= 6 and len(s) >= 2:
        if s.isalnum():
            return True


def check_order(s):
    for i in range(len(s)):
        if s[0].isdigit():
            if int(s[i]) == 0:
                return False
        elif not (s[i + 1 : :].isalpha()) == False:
            return False
        else:
            return True


main()
