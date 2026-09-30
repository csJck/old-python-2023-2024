

def main():
    square(int(input("Height: ")), int(input("Width: ")))



def square(w,h):
    # the range is just the amount of times that the string will be printed
    # remember that a range is a collection of individual numbers and isnt a single value
    # so a range of 3 is actually 1, 2 and 3 - so the below statement essentially means: for each value(_) in range(h) print this
    # this means that the amount of prints is decides by the size of the range
    # a range of 5 is essentially a list of [1,2,3,4,5]
    for _ in range(h):
        print("[]" * w)
        




main()