camelCase = input("camelCase: ")
snake_case = ""

for x in range(len(camelCase)):
    if camelCase[x].isupper():
        snake_case += "_"
        snake_case += camelCase[x]
    else:
        snake_case += camelCase[x]

snake_case = snake_case.lower()

print(snake_case)
