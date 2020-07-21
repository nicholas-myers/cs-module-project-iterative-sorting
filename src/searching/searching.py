def linear_search(arr, target):
    # Your code here
    # check every index value
    for i in range(len(arr)): 
  
        if arr[i] == target: 
            return i 

    return -1   # not found


# Returns either the index of the target in the arr 
# or, if the target isn't in the arr, return -1 
def binary_search(arr, target):
    # set the start and end points
    start = 0
    end = len(arr) - 1
    
    # if the start point is less than or equal to the endpoint keep checking
    while   start <= end:
        # get the middle index
        midindex = (end + start) // 2
        # if the middle index is the target return
        if target == arr[midindex]:
            return midindex
        # if the target is less than the mid go left
        if target < arr[midindex]:
            # reset the end index ti mid minus 1
            end = midindex - 1
        # if the target is greater than mid go right
        if target > arr[midindex]:
            # reset the start index to be the mid plus one
            start = midindex + 1
    return -1
    
arr = [3, 4, 6, 16, 26, 28, 52, 55]
# print(binary_search(arr, 58))
