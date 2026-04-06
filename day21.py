def find_peak(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]<arr[mid+1]:
            low =mid+1
        else:
            high = mid
    return arr[low]
arr=[1,2,4,5,9,10]
print(find_peak(arr))

de