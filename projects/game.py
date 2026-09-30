import random as rd

while True:
    try:
        level = int(input("level: "))
        break
    except ValueError:
         continue
    
number = rd.randrange(1,level)

while True:
    try:
        guess = int(input("guess: "))
    except ValueError:
         continue
    
    if guess > level:
         print("Too large!")
         continue
    elif guess > number:
        print("Too large!")
    elif guess < number:
            print("Too small!")
    else:
         print("Just right!")
         break
        