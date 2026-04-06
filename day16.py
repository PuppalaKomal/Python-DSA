# bubble sort
# 1. one of the simplest sorting algorithm
# 2. largest element 

# how it works:
#     1. compare the adjacent elements
#     2. swap them if they are in wrong order
#     3. repeat the process until no more swaps are needed

# time complexity
# best case: O(n)
# average case: O(n^2)

#space complexity: O(1)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr=[8,4,2,6]
print(bubble_sort(arr))

#COUNTING MINIMUM NUMBER OF SWAPS REQUIRED TO SORT AN ARRAY

