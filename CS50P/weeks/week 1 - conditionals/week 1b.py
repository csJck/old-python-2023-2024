
#the % (modulo operator) basically divides numbers and then outputs what the remainder is (it doesnt output the actual number only the remainder), so logically if you divide any number by 2 and there is a remainder then automatically the number isnt even. e.g 3 divided by 2 is 1 remainder 1 in the context of using modulo
# this statement basically means if the remainder of x divided by 2 isnt 0 then the number is odd

def main():
    x = int(input("What is x? "))
    if even_check(x):
        print("even")
    else:
        print("odd")

def even_check(number):
    if number % 2 == 0:
        return True
    else:
        return False
# another way to write this:
# return True if n % 2 == 0 else False
# another way to write this:
# return n % 2 ==0

main()

print(even_check(3))