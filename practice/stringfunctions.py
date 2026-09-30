full_name = input("Enter your first and last name: ").title()

first_name, last_name = full_name.split(" ")

print("Hello, ", end="")
print(first_name)

print(first_name, last_name, first_name, last_name, first_name, last_name, first_name, last_name, first_name, last_name, sep="-")