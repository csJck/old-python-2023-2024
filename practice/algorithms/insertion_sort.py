arr = [1,9,2,8,3,7,4,6,5,0]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key


        
    

print(arr)   

