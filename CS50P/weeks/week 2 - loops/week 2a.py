for i in [0,1,2,3,4,5,6,7,8,9]:
    print("he", end="",sep="")

# using the range function is sick because it means that you dont hve to write out each number of a list individually until you reach the desired number
for i in range(10):
    print("he", end="",sep="")

# the _ represents a valuable which has no value and isnt going to be used later so its a better alternative for use cases like this
for _ in range(10):
    print("he", end="",sep="")

# this is another cool way to print something multiple times just simply by using a multiplier on a string
print("he\n" * 10, end="")


# this break statement is efficient because it only breaks if the conditon is met so you dont hyave to tell the program what to do if the condition isnt met, you only tell it what to do when it is met. so while the condition isnt met it will just continue forever    
  
def main():
    x = get_number()
    meow(x)
    

def get_number():
    while True:
        n = int(input("How many meows? "))
        # this break statement is efficient because it only breaks if the conditon is met so you dont hyave to tell the program what to do if the condition isnt met, you only tell it what to do when it is met. so while the condition isnt met it will just continue forever    
        if n > 0:
            break
    return n
    # the return statement send this value back to where the function was called 


def meow(n):
  
    for _ in range(n):
        print("meow")

main()