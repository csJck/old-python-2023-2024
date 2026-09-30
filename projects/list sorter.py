items = [1,8,9,3,1]
swapped = True
n = len(items)
sorting = "sorting"

print("-----------------------------------------")
print(items, "sorting")
while n > 0 and swapped == True:
    swapped = False
    n -= 1
    for i in range(0,n):
        sorting = sorting + ".."
        temp = None
        if items[i] > items[i+1]:
            temp = items[i]
            items[i] = items[i+1]
            items[i+1] = temp
            print(items, sorting)
            swapped = True
        

print("-----------------------------------------")



