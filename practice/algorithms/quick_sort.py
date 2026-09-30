list = [1,0,2,9,3,8,4,7,5,6]

def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0] # can be first or last element
        left = []
        right = []

        for x in list[1:]:
            if x > pivot:
                right.append(x)
            else:
                left.append(x)
        
        return quicksort(left) + [pivot] + quicksort(right)


print(quicksort(list))