def main():
    x = int(input("input x: "))
    print(f"x squared is {square(x)}")

def square(num):
    return num + num


if __name__ == "__main__":
    main()
# doing this prevents main from being called if i was to import one of the above funcitons into another file