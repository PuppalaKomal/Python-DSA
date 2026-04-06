# quick sort
def quickselect(arr,k):
    return helper(arr, 0, len(arr) - 1, k-1)
def helper(arr,low,high,k):
    if low <= high:
        pivote_index = partition(arr,low,high)
    if pivote_index == k:
        return arr[pivote_index]
    elif pivote_index < k:
        return helper(arr,low,pivote_index - 1,k)
    else:
        return helper(arr,pivote_index + 1,high,k)
def partition(arr,low,high):
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i],arr[high] = arr[high] arr[i]
    return 1
arr=[7,10,4,3,20,15]
k=3
result= quickselect(arr,k)
print("array:"arr)
print(f"{k}th smallest element is: ",result)