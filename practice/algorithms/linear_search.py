arr = [2,1,3,6,4,5,7,8,9,0]

def linear_search(arr,target):
    for x in arr:
        if x == target:
            return True
        else:
            return False
        
print(linear_search(arr, 12))