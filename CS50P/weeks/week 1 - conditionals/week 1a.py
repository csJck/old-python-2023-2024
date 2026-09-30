score = int(input("What's your score 1-100: "))

if 90 <= score <=100:
# you can put a number first and ask if the number is less or greateer or equal to the variable rather than doing it the other way round, this way you can then add in a second condfition on the other side without having to write and   
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("You're ass.")
