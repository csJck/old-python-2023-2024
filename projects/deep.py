q = input("What's the meaning of life? ").lower()

match q:
    case "42" | "forty two" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")
