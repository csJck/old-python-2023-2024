ae = input("Arithmetic expression: ")

x, y, z = ae.split(" ")

x = float(x)
z = float(z)

if y == "/" and z == 0:
    print("Error")

elif y == "+":
    result = x + z

elif y == "-":
    result = x - z

elif y == "*":
    result = x * z

elif y == "/":
    result = x / z

print(f"{result:.1f}")
