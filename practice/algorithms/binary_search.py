list = [1,2,3,4,5,6,7,8,9,10]
target = 0

def binary_search(list, target):

    left = 0
    right = len(list)- 1

    while left <= right:
        mid = (left + right) // 2 # the double // means that result wont be a floating point number

        
        if list[mid] < target:
            left = mid + 1 # this changes the area being searched from (0 - 10) to (6 - 10)
        
        elif list[mid] > target:
            right = mid - 1 # this changes the area being searched from (0 - 10) to (0 - 4)
        
        else:
            return True
    
    return False


print(binary_search(list, target))