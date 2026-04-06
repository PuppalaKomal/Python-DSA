# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        return arr
arr=[9,4,2,7]
print(insertion_sort(arr))

# Quick Sort
# _pick a pivot element
# _place th pivot at its correct position
