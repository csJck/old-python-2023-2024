import random


def main():
    generate_integer(get_level())
    

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    score = 0
    for x in range(10):
        counter = 0
        if level == 1:
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            while True:
                try:
                    ans = int(input(f"{n1} + {n2} = "))            
                    if ans != n1 + n2:
                        print("EEE")
                        counter+=1
                    elif counter == 3:
                        print(f"{n1} + {n2} = {ans}") 
                    else:
                        if counter == 0:
                            score+=1
                        break
                except ValueError:
                    counter+=1
                    print("EEE")
        
        elif level == 2:
            n1 = random.randint(10,100)
            n2 = random.randint(10,100)
            while True:
                try:
                    ans = int(input(f"{n1} + {n2} = "))            
                    if ans != n1 + n2:
                        print("EEE")
                        score -=1
                    elif counter == 3:
                        print(f"{n1} + {n2} = {ans}") 
                    else:
                         score +=1
                         break
                except ValueError:
                    print("EEE")
        else:
            n1 = random.randint(100,1000)
            n2 = random.randint(100,1000)
            while True:
                try:
                    ans = int(input(f"{n1} + {n2} = "))            
                    if ans != n1 + n2:
                        print("EEE")
                        score -=1
                    elif counter == 3:
                        print(f"{n1} + {n2} = {ans}") 
                    else:
                        score +=1
                        break
                except ValueError:
                    print("EEE")
    print(f"Score: {score}")
            

if __name__ == "__main__":
    main()

