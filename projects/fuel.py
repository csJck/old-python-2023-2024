def main():

    fuel(input("Fraction: "))


def fuel(x):
    n, d = x.split("/")

    try:
        n = int(n)
        d = int(d)
    except ValueError:
        print("input must be a fraction of integers.")
        main()


    if n > d:
            print("The numerator can't be larger than the denominator.")
            main()

    try:
        t = (n / d) * 100
        t = int(t)
    except ZeroDivisionError:
        print("You can't divide with zero.")
        main()


    if t <= 1:
        print("E")
    elif t == 100:
        print("F")
    else:
        print(f"{t}%")






















main()
