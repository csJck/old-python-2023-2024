

with open("names.txt", "w") as file: # "w" means write, "a" means append, "r" means read but read is the default so it isnt needed

    for _ in range(3):
        file.write(f"{input("name: ").title()}\n")

names = []

with open("names.txt") as file:
    # lines = file.readlines() thius function reads the lines inside the text file

    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")



    