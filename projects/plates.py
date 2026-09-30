import string

def main():
    plate = str(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    for c in range(len(s)):
        if s[c].isspace():
           return False
        elif not s[c].isalnum():
            return False

    if s[0] == 0:
        return False
    elif len(s) > 6:
        return False
    elif not s[0:2].isalpha():
        return False
    elif s[-2].isdigit() and s[-1].isalpha():
        return False
    elif s[-2].isalpha() and s[-1].isdigit():
        return False
    else:
        return True












main()

