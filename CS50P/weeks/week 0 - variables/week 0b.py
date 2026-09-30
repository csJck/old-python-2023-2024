

while 1 == 1:
    try:
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))

        z= round(x+y, 2)
        #THE ROUND() function rounds the float to a whole number, the 2 means its rounded to 2 digits (leave it blank to round to  a whole number)
        print(f"{z:,}")
        #the above thingy makes it so that there are commas in the number
    except:
            ValueError
            print("that is not a number, try again.")
            

