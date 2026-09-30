# 59:00 / 1:45:38

name = input("enter your first and last name? ").strip().title()
# the line above is prompting the user to input thier name

# name = name.strip()
# the .strip() function removes any white space from the input

# name = name.capitalize()
# this function will capitalize the first letter of the input

# name = name.title()
# this will change the first letter of multiple words in the input to upper case

# name = name.strip().title()
# here you can see that built in functions can be chained together

firstName, lastName = name.split(" ")
#the split funciton can create multiple variables form one variable (sub variables) first you must declare the names of the new sub variables like i did (firstName, lastName) then you must tell the computer which character to perform the split on, i used a space so i simply entered the parameter (" ").

print("hello ", end="")
# the end="" changes what the end of the line is. since it has no value the end doesnt happen this means that the next line of code could then be displayed on the same line as the above one

print(firstName, lastName, firstName, lastName, firstName, lastName, firstName, lastName, sep="+")
# the sep="" can change what the space is filled in with so rather than name name name it would become name+name+name

print("hello, \"friend\"")
# the forward slashes before the quotes ( \"random\" ) allows them to be displayed as normal with the rest of the string