import random as rd

# from random import choice
# here you can see that you are able to import individual functions form a library rather than importing the while library

def main():
    coin_flip()
    print(rd.randint(1, 100))
    list1 = [1,2,3,4,5]
    rd.shuffle(list1)
    print(list1)


def coin_flip():
    print("---coin flip---")
    coin = rd.choice(["heads","tails"])
    print("outcome:", coin)
    print("---------------")
    if coin == "heads":
        return True
    else:
        return False



main()