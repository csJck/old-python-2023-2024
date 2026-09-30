DRINKS = [["1. Coke", "2. Pepsi", "3. Fanta", "4. Sprite", "5. Prime", "6. Powerade", "7. Redbull", "8. Dr pepper",
           "9. Oasis", "10. Water"],
          [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]


def drinks_machine():
    choice = None
    print("Drinks Machine")
    print("--------------")
    for x in range(len(DRINKS[0])):
        print(f"{DRINKS[0][x]} - stock: {DRINKS[1][x]}")
    print("--------------")

    while True:
        try:
            choice = int(input("choose a drink (1-10): "))
            if 1 <= choice <= 10:
                if DRINKS[1][choice - 1] > 0:
                    DRINKS[1][choice - 1] -= 1
                    print("Enjoy your " + DRINKS[0][choice - 1][3:] + ".")
                    print(DRINKS[0][choice - 1][3:], "Stock:", DRINKS[1][choice - 1])
                    print("--------------")
                    again()
                    break
                else:
                    print("There is no stock left for this drink.")
            else:
                print("That is not an option, choose an available drink.")
        except ValueError:
            print("That is not a correct value.")


def again():
    choice = None
    while choice != "y" or "n":
        choice = input("Would you like to buy another drink? (y|n): ").lower()
        if choice == "y":
            drinks_machine()
            break
        elif choice == "n":
            print("Enjoy your drink(s)")
            exit()
        else:
            continue


drinks_machine()
