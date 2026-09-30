def main():
    print(gauge(convert(input("fraction: "))))



def convert(fraction):

    num, den = fraction.split("/")

    try:
        num = int(num)
        den = int(den)
    except ValueError:
        return ValueError
    if num > den:
            print("The numerator can't be larger than the denominator.")
            main()
    try:
        per = (num / den) * 100
        per = int(per)
        return per
    except ZeroDivisionError:
        return ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()







