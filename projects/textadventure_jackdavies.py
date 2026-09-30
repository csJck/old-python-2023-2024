import random
import time

#GLOBAL DECLARATIONS---------------------------------------------------------------------------------------------------

armoury = ["Katana", "Greatsword", "Broadsword","Falchion", "Longsword", "Scimitar"]
protective_gear = ["Leather armour", "Iron armour", "Steel armour","Obsidian armour", "Diamond armour"]


#INTRODUCTION----------------------------------------------------------------------------------------------------------


print("Text adventure.\n ")
time.sleep(2)
name = input("what would you like your name to be: ")
time.sleep(2)
print("\n""Welcome to your adventure", name+"!")
time.sleep(2)


#INTERSECTION ONE------------------------------------------------------------------------------------------------------

def d1func():
    decision1 = str(input("\n""You are the the beginning room, you see 2 doors labeled 'left' and 'right' in front of you, which one will you choose"+" "+name+"? \n")).lower()

    if decision1 == "left":
        time.sleep(3)
        print(name, "chose left.\n")
        time.sleep(3)
        left_door()

    elif decision1 == "right":
        time.sleep(3)
        print(name, "chose right.\n")
        time.sleep(3)
        right_door()

    else:
        print("please choose left or right", name, ".")
        d1func()

#RIGHT DOOR 1
def right_door():
    print("you enter a room which is encapsulated in darkness, you light a torch and rats scurry away from the light, you begin cautiously walking forward and then you encounter what seems to be some kind of crate.\n ")
    time.sleep(5)
    return1 = None
    while return1 != "yes" or "no":
        return1 = input("would you like to continue with this door or return and make a different decision?\n please type 'yes' to continue and 'no' to return.\n").lower()
        if return1 == "no":
            d1func()
            break
        elif return1 == "yes":
            print("\nOk", name, "lets continue.\n")
            print("you approach the crate and open it.\n")
            random.shuffle(armoury)
            time.sleep(3)
            print("you found a", armoury[0]+", this will be your weapon throughout the adventure.\n")
            time.sleep(3)
            print("you continue walking through the passage, only dimly lit by the torch you are holding.\nAfter what feels like hours, you feel a sense of relief as you notice two oddly shaped doors in the distance.\n")
            time.sleep(5)
            d2func()
            break
        else:
            continue

#LEFT DOOR 1

def left_door():
    print("you enter and all you can see is what seems to be an endless passage bordered with dense foliage and trees, you light a torch and bats fly back into hiding, you begin cautiously walking forward and then you encounter what seems to be some kind of crate.\n ")
    time.sleep(5)
    return1 = None
    while return1 != "yes" or "no":
        return1 = input("would you like to continue with this door or return and make a different decision?\n please type 'yes' to continue and 'no' to return.\n").lower()
        if return1 == "no":
            d1func()
            break
        elif return1 == "yes":
            print("\nOk", name, "lets continue.\n")
            print("you approach the crate and open it.\n")
            random.shuffle(armoury)
            time.sleep(3)
            print("you found a", armoury[0]+", this will be your weapon throughout the adventure.\n")
            time.sleep(3)
            print("You continue your walk, the trees seem to blend into eachother and the concept of time feels like its fading away.\n Just when you feel like your legs could give way, you see what appears to be two oddly shaped doors in the distance.\n")
            time.sleep(5)
            d2func()
            break
        else:
            continue


#INTERSECTION TWO------------------------------------------------------------------------------------------------------

def d2func():
    decision2 = str(input("You're at the end of the passage, two doors stand before you. Which will you choose "+ name+"?\nplease choose 'left' or 'right.\n")).lower()
   
    if decision2 == "left":
        time.sleep(3)
        print(name, "chose left.\n")
        time.sleep(3)
        left_door2()
    
    elif decision2 == "right":
        time.sleep(3)
        print(name, "chose right.\n")
        time.sleep(3)
        right_door2()
        
    else:
        print("\nplease choose left or right "+name+".")
        d2func()

#LEFT DOOR 2

def left_door2():
    print("You make your way through the door and you cant believe your eyes.\n A vast tropical paradise sits before you, but something doesnt feel right.\n ")
    time.sleep(5)
    return2 = None
    while return2 != "yes" or "no":
        return2 = input("would you like to continue with this door or return and make a different decision?\n please type 'yes' to continue and 'no' to return.\n").lower()
        if return2 == "no":
            time.sleep(3)
            print("You try to go back the way you came but the door slams shut.\n\n You try the handle but suddenly it glows red with heat and melts away\n\n"+name+" it seems like you cannot turn back, you have no option but to keep going forward.\n")
            time.sleep(3)
            break
        elif return2 == "yes":
            time.sleep(2)
            print("Ok", name, "lets continue\n")
            time.sleep(2)
            break
        else:
            print("Please choose 'yes' or 'no'!\n")
            continue


    print("You cautiously move forward, your shoes creating slight imprints into the sand as you walk.\nAs you walk through the fine powdery sand, you notice that some areas of the sand are behaving strangely.\n Its almost as if the surface of the sand is moving, like theres something moving beneath it.\n\n")
    print(name,"starts to become concerned.\n")
    time.sleep(5)

    equip = None
    while equip != "equip":
        equip = input("reply with 'equip' to ready your weapon, trouble may be on its way!\n").lower()
        if equip == "equip":
            print("You pull out your " + armoury[0] + " and prepare for the worst.")
            break
        else:
            print("Please equip your weapon!\n")
            continue
    time.sleep(3)
    print("Suddenly a large worm like creature shoots out of the ground and sand rains down onto you\n\nThe Sandworm barrels towards you at high speeds.\n")
    time.sleep(3)
    attack = None
    sandworm = [1, 2, 3, 4, 5]
    while attack != "attack":
        attack = input("Please type 'attack' to attack the sandworm with your " + armoury[0] + "! \n").lower()
        if attack == "attack":
            break
        else:
            continue
    counter = 1
    while sandworm[1] != 1:
        random.shuffle(sandworm)
        counter += 1
        input("You missed, please type 'attack' to try again!\n")
        if sandworm[1] == 1:
            print(
                "As the Sandworm comes towards you at high speeds, you hold your sword out and impale the Sandworm direcly in its head.\n")
            time.sleep(3)
            print("You stopped the Sandworm after", counter, "attempt(s), well done " + name + "!")
            break
        else:
            continue
    time.sleep(3)
    print("With your sword stil stuck in the sandworms head it stops moving and slumps flat onto the sand.\n\n Well done "+name+"!\n")
    time.sleep(3)
    print("following your victory against the sandworm you retrieve your weapon from its head and continue on your way\n")
    time.sleep(3)
    print("You made it the the end of the trail and you see a set of doors in the distance")


    time.sleep(3)
    final_door()

#RIGHT DOOR 2
def right_door2():
    print("You walk through the door and you're greeted with the sound of seagulls as they fly above your head, a series of rocky islands each interlinked by a series of wooden bridges sits before you.\n ")
    time.sleep(5)
    return2 = None
    while return2 != "yes" or "no":
        return2 = input("would you like to continue with this door or return and make a different decision?\n please type 'yes' to continue and 'no' to return\n").lower()
        if return2 == "no":
            time.sleep(3)
            print("You try to go back the way you came but the door slams shut.\n\n You try the handle but suddenly it glows red with heat and melts away.\n\n"+name+" it seems like you cannot turn back, you have no option but to keep going forward.\n")
            time.sleep(3)
            break
        elif return2 == "yes":
            time.sleep(2)
            print("Ok", name, "lets continue\n")
            time.sleep(2)
            break
        else:
            print("Please choose 'yes' or 'no'!")
            continue

    print("You cautiously move forward, making your way onto the first bridge which takes you to the initial rocky island.\n")
    time.sleep(3)
    print("You wince as the waves crash against the rocks, splashing you with water.\n\nAs you traverse along the bridges you start to notice spurts of water shooting up into the air, almost akin to a whale shooting air from its blowhole but on a much larger scale.\n")
    time.sleep(5)
    print(name, "starts to become concerned.\n")
    time.sleep(3)

    equip = None
    while equip != "equip":
        equip = input("reply with 'equip' to ready your weapon, trouble may be on its way!\n").lower()
        if equip == "equip":
            print("You pull out your "+armoury[0]+" and prepare for the worst.\n")
            time.sleep(3)
            break
        else:
            continue
    time.sleep(3)
    print("Suddenly a large serpent creature shoots ferociously out of the water and positions itself between yourself and the next bridge\n")
    time.sleep(3)
    attack = None
    serpent = [1, 2, 3, 4, 5]
    while attack != "attack":
        attack = input("Please type 'attack' to attack the serpent with your "+armoury[0]+"! \n").lower()
        if attack == "attack":
            break
        else:
            continue
    counter = 1
    while serpent[1] != 1:
        random.shuffle(serpent)
        counter += 1
        input("You missed, please type 'attack' to try again!\n")
        if serpent[1] == 1:
            print("You slice through the Serpents stomach, revealing its inner organs as they spill out onto the rocks in front of you.\n")
            time.sleep(3)
            print("You killed the Serpent after", counter, "attempt(s), well done "+name+"!")
            break
        else:
            continue
    time.sleep(3)
    print("\nfollowing your victory against the serpent you wipe down your sword against the railing of the wooden bridge and continue on your way\n")
    time.sleep(3)
    print("You made it the the end of the islands and you see a large set of doors in the distance\n")
    time.sleep(3)
    final_door()


#FINAL DOOR----------------------------------------------------------------------------------------------------

def final_door():
    print("You pass through the doors and you a long trail bordered with lava and flaming rocks leading to a large structure in the distance\n ")
    time.sleep(5)
    print("you start walking down the trail and you come across a suspicious looking crate positioned in the center of the path.\n")
    time.sleep(3)
    open = None
    while open != "yes" or "no":
        open = input("would you like to find out what is inside the suspicious crate or would you like to leave it?\nplease type 'yes' or 'no'\n").lower()
        if open == "no":
            time.sleep(2)
            print("Okay", name, "lets leave the crate and continue.\n")
            time.sleep(3)
            break
        elif open == "yes":
            time.sleep(2)
            print("Ok", name, "lets open it.\n")
            time.sleep(2)
            random.shuffle(protective_gear)
            print("You found", protective_gear[0], "this may come in handy very soon...\n")
            time.sleep(3)
            equip = None
            while equip != "equip":
                equip = input("Please type 'equip' to put on your new gear!\n").lower()
                if equip == "equip":
                    print("Great! you're now wearing your new", protective_gear[0]+".\n")
                    time.sleep(2)
                    break
                else:
                    continue
            break
        else:
            print("Please choose 'yes' or 'no'!\n")
            continue
    print("You continue walking down the trail.\n")
    time.sleep(2)
    print("You read a sign saying 'Turn back now or suffer the consequences!'\n")
    time.sleep(4)
    print("After", name+"'s success with the previous boss they choose to continue.\n")
    time.sleep(4)
    print("You continue with your walk, and the distant structure now doesnt seem so far.\n")
    time.sleep(4)
    print("You begin to feel dehydrated due to the heat and the distance of the walk.\n")
    time.sleep(4)
    drink = None
    while drink != "drink":
        drink = input("Type 'drink' to replenish your fluids!\n")
        if drink == "drink":
            print("Great, you are now refreshed!\n")
            break
        else:
            print("You wont survive without water!\n")
            continue
    time.sleep(3)
    print("After a long and painful walk, you finally reach the entrance of the large structure which you can now see is a castle of sorts.\n")
    time.sleep(3)
    print("**A LOAD ROAR ECHOES FROM INSIDE OF THE CASTLE**\n")
    time.sleep(3)
    print("Best to equip your weapon now, it seems like you may be fighting shortly!\n")
    equip2 = None
    while equip2 != "equip":
        equip2 = input("reply with 'equip' to ready your "+armoury[0]+"!\n").lower()
        if equip2 == "equip":
            print("You pull out your "+armoury[0]+" and prepare for a battle.\n")
            time.sleep(3)
            break
        else:
            continue
    print("You walk through the entrance and are greeted by an intense heat as well as a large dragon with his eyes locked on .\n")
    time.sleep(3)
    print("The dragon tries to attack you!\n")
    time.sleep(2)
    life = int(3)
    dodge = random.randint(1,2)
    while dodge != 1 or 2:
        input("Type 'dodge' to evade the dragons attack!\n")
        if dodge == 1:
            print("Great you dodged the dragons attack and you are still "+str(life)+ "/3 health.\n")
            break
        else:
            life = life - 1
            print("You have failed to dodge the dragons attack and you are now "+str(life)+"/3 health!\n")
            break
    time.sleep(3)
    print("You dart forward and slice along the wing of the dragon!\n")
    time.sleep(3)
    print("The dragon is angered and attempts to swing his tail at you!\n")
    time.sleep(3)
    dodge2 = random.randint(1, 2)
    while dodge2 != 1 or 2:
        input("Type 'dodge' to evade the dragons attack!\n")
        if dodge2 == 1:
            print("Great you dodged the dragons attack and you are still "+str(life)+"/3 health.\n")
            break
        else:
            life = life - 1
            print("You have failed to dodge the dragons attack and you are now "+str(life)+"/3 health!\n")
            break
    time.sleep(3)
    print("You attack the dragon while his back is turned and cut him along ridges of his spine!")
    time.sleep(3)
    print("The dragon exhales in anger and smoke is released form his nostrils!\n\nYou see an orange glow start to appear from his chest!\n")
    time.sleep(5)
    print("The dragon charges up a fire breathing attack, prepare to dodge "+name+"!")
    time.sleep(3)
    dodge3 = random.randint(1, 2)
    while dodge3 != 1 or 2:
        input("Type 'dodge' to evade the dragons breath!\n")
        if dodge3 == 1:
            print("Great you dodged the fire attack and you are still "+str(life) + "/3 health.\n")
            break
        else:
            life = life - 1
            print("You have failed to dodge the dragons attack and you are now "+str(life)+"/3 health!\n")
            break
    if life == 0:
        print("You have died, time to restart\n")
        d1func()
    time.sleep(3)
    print("As the dragons mouth is gaped open from his fire breathing attack, you launch your", armoury[0], "in the dragons mouth and he falls to the ground!\n")
    time.sleep(3)
    print("Well done", name, "you have slain the mighty beast!")
    time.sleep(3)
    print("You peak over the dragons corpse and notice a huge gold door behind him.\n\nYou walk through the door and are greated wiht a pile of riches as far as the eye can see.\n\nYou are now rich behond your wildest dreams, it seems like this adventure was worth it after all.\n")
    time.sleep(5)
    print("Your adventure has come to an end", name,".")

#KEEP BELOW ALL FUNCTION DECLARATIONS!
d1func()
exit()
    
        


    

    
    
