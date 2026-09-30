name = input("What's your name? ").title()

match name:
    case "Mongraal" | "Mr Savage" | "Veno":
        print("Europe")
    case "Clix" | "Bugha" | "Peterbot":
        print("North America")
    case _:
        print("Who?")