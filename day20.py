def first_occurence(arr,target):
    low = 0
    high = len(arr)-1
    result = -1
    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            result = mid
            high = mid-1  #moving left
        elif target < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    return result
arr = [10,30,20,20,30]
target = 20
print("Element found at index:",first_occurence(arr,target))

def search_rotated(arr, target):
    low = 0 
    high = len(arr)-1 
    while low <= high: 
        mid = (low + high) // 2
        if arr[mid]==target: 
            return mid 
        if arr[low] <= arr[mid]: 
            if arr[low] <= target < arr[mid]:
                high =  mid - 1
            else: 
                low = mid + 1
        else: 
            if arr[mid] <=  target <= arr[high]: 
                low = mid + 1
            else: 
                high =  mid - 1
    return - 1

arr = [4,5,6,7,0,1,2]
target =  6
print(search_rotated(arr, target))