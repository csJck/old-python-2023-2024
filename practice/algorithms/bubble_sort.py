# bubble sort

list = [1,0,2,9,3,8,4,7,5,6]

n = len(list)
swapped = True

while n > 0 and swapped == True:
    n-=1
    swapped = False

    for x in range(0,n):
        if list[x] > list[x+1]:
            temp = list[x]
            list[x] = list[x+1]
            list[x+1] = temp
            swapped = True


print(list)