arr = [5, 55, 6, 67, 12, 9, 25, 43, 16]
# runtime: O(n * n) = O(n^2)
def selection_sort(arr):
    # iterate through the array (represents the sorted-unsorted start 
    # moving across the array)
    for i in range(len(arr)):  # O(n)
        # index of the start, as well as the index we're going to 
        # swap the smallest element with 
        start = i

        smallest_value = arr[start]
        smallest_index = start
        # finding the smallest element 
        # in the "unsorted" portion of the array 
        for unsorted_index in range(start, len(arr)):  # O(n)
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        # `smallest_index` is the index of the smallest element in the unsorted portion 

        # once that's found, swap it with the element on the right edge 
        # of the sorted-unsorted start 

        arr[start], arr[smallest_index] = arr[smallest_index], arr[start]

    return arr


arr = [5, 55, 6, 67, 12, 9, 25, 43, 16]
print(selection_sort(arr))

# def selection_sort(arr):
    # new_arr = []
    # # loop for as long as the arr has items
    # for i in range(len(arr)):
    #     # print(arr)
    #     lowest_value = arr[0]
    #     lowest_index = 0
    #     for index, num in enumerate(arr, 0):
    #         if num < lowest_value:
    #             lowest_value = arr[index]
    #             lowest_index = index
    #     new_arr.append(lowest_value)
    #     arr.pop(lowest_index)
    # return new_arr

# import random
# arr4 = random.sample(range(200), 50)
# print(selection_sort(arr4))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    values_swapped = True
    # checks if values were swapped if they were swapped keep running
    while values_swapped:
        # set the default to be not swapped
        values_swapped = False
        # check every index minus the last index
        for i in range(len(arr) - 1):
            # current value is greater than the next value swap them
            if arr[i] > arr[i+1]:
                # swap them
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # if they get swapped the while loop keeps happening until there are no more swaps
                values_swapped = True
    
    return arr

arr = [5,1,7,6,2,1,0]
# print(bubble_sort(arr))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
