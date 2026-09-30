import random as rand

def main():
    while True:
        try:
            team_gen(int(input("team size: ")))
        except ValueError:
            print("enter an integer")
        else:
            break

def team_gen(x):
    if x > 16:
        print("max team size is 16")
        main()
    
    # here im delcaring the team array as having a fixed value of 16 without having to manually insert 16 entries
    team = [None] * 16
    
    for i in range(x):
        team[i] = input("enter player: ")
    
    m = x / 2
    m = int(m)
    
    rand.shuffle(team[0:x])

    team_one = team[0:m]
    team_two = team[m:x]

           
    print(f"team one: {team_one}\nteam two: {team_two}")
    
   


    
main()