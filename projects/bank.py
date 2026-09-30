greeting = input("Greet me: ").strip().capitalize()

if greeting == "Hello":
    print("$0")
elif greeting[0] == "H":
    print("$20")
else:
    print("$100")


