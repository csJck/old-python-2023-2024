def main():
    name = input("Name: ")
    hello(name)
    goodbye(name)


def hello(name):
    print(f"Hello, {name}.")


def goodbye(name):
    print(f"Goodbye, {name}.")


if __name__ == "__main__": # this means that if you are to use this file as a library in another file then it wont run main when you call one of the other functions like hello or goodbye
    main()