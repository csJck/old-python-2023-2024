import random

print("Random team generator")

players4 = [1,2,3,4]
players6 = [1,2,3,4,5,6]
players8 = [1,2,3,4,5,6,7,8]
def team_gen():
    size = str(input("choose a lobby size of 4, 6 or 8: "))

    if size == "4":
        players4[0] = input("enter the first player: ")
        players4[1] = input("enter the second player: ")
        players4[2] = input("enter the third player: ")
        players4[3] = input("enter the fourth player: ")
        random.shuffle(players4)
        print("Team 1 =", players4[:2])
        print("Team 2 =", players4[2:])

    elif size == "6":
        players6[0] = input("enter the first player: ")
        players6[1] = input("enter the second player: ")
        players6[2] = input("enter the third player: ")
        players6[3] = input("enter the fourth player: ")
        players6[4] = input("enter the fifth player: ")
        players6[5] = input("enter the sixth player: ")
        random.shuffle(players6)
        print("Team 1 =", players6[:3])
        print("Team 2 =", players6[3:])

    elif size == "8":
            players8[0] = input("enter the first player: ")
            players8[1] = input("enter the second player: ")
            players8[2] = input("enter the third player: ")
            players8[3] = input("enter the fourth player: ")
            players8[4] = input("enter the fifth player: ")
            players8[5] = input("enter the sixth player: ")
            players8[6] = input("enter the seventh player: ")
            players8[7] = input("enter the eighth player: ")
            random.shuffle(players8)
            print("Team 1 =", players8[:4])
            print("Team 2 =", players8[4:])

    else:
        if size != "4" or "6" or "8":
            print("That is not an option, please try again.")
            team_gen()


team_gen()

print("enjoy your game")



