names = []
size = 0

while True:
    try:
        names.append(input("name: "))
        size+=1
    except EOFError:
        break


if len(names) != 1:
    print("Adieu, adieu, to ", end="")
    for x in range(size-1):
        if len(names) > 1:
            print(names[x], end="")
            print(", ",end="")

    print(f"and {names[-1]}")

elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")

else:
    print(f"Adieu, adieu, to {names[0]}")




    