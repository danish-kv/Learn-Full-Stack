def binary_search(arr, target):
    l = 0
    r = len(arr)-1

    while l <= r :
        mid = (l + r) // 2
        if arr[mid] == target:  
            return mid
        
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return None

arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 2))
