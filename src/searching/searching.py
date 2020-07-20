def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = arr[0]
    high = arr[len(arr) - 1]
    mid = (high - low) / 2
    while low <= high:
        mid = (high - low) / 2
        if target == arr[mid]:
            return mid
        
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1


sorted_nums = [3, 4, 6, 26, 28, 52, 55]

binary_search(sorted_nums, 52)