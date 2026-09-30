import random as rd
import time as t


def main():
    coin_flip()


def coin_flip():
    print("---coin flip---")
    z = ".."
    for x in range(5):
        t.sleep(0.5)
        print(z)
        z += ".."
        
    print("outcome:", rd.choice(["heads","tails"]))



main()