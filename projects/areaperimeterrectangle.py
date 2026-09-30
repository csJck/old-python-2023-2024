import math


question = input("would you like to solve the area or perimeter of a rectangle, both or none? ")


def area(length, width):
            print("area is", (float(length * width)))

def perimeter(length, width):
            print("perimeter is", (float(2*(length + width))))
        

while question != "none":
    length = float(input("enter the length: "))
    width = float(input("enter the width: "))
    
    if question == "area":
        area(length, width)
        question = input("would you like to solve the area or perimeter of a rectangle, both or none? ")


    elif question == "perimeter":
        perimeter(length, width)
        question = input("would you like to solve the area or perimeter of a rectangle, both or none? ")
        

    elif question == "both":
        area(length, width)
        perimeter(length,width)
        break
        

