# Time complexity
# Definition:
#     whenever the input increases the running time of code increases linearly.
# Eg:
#     if n=5 the code runs 5 times
#     if n=10 the code runs 10 times

# O(n)
# for i in range(arr):
#     print(i)

# O(n^2)
# for i in range (arr):
#     for j in range (arr):

# O(n^3)
# for i in range (arr):
#     for j in range (arr):
        # for k in range (arr):

# O(1)
# arr=[1,2,3,4,5]
# print(arr[0])

# Time complexities
# O(1): accessing elements
# O(n): linear search
# O(n^2): selection,bubble
# O(n^3): triplets
# O(log n): binary search
# O(n log n): merge,quick 
# O(n!): traveling salesman problem
# O(2^n): recursion
# fast to slow O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)


# two pointer
# very powerfull approach
# instead of using single index (pointer) we are using two index (pointers)
# instead of checking each and every pair we are using two pointer to check pairs
# we can optimize from O(n^2) to O(n)
# left pointer and right pointer
# left pointer at the start and right pointer at the end
# EG:
# arr=[1,2,3,4,6]
# target=6
# output=(2,6)

def two_pointer(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        curr_sum=arr[left]+arr[right]
        if curr_sum==target:
            return arr[left],arr[right]
        elif curr_sum<target:
            left+=1
        else:
            right-=1
    return None
arr=[1,2,3,4,6]
target=6
print("Output:",two_pointer(arr,target))

#Removing duplicates 

def remove_duplicates(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return  i+1
arr=[1,1,2,2,3,3]
k=remove_duplicates(arr)
print("new values: ",remove_duplicates(arr))
print("new array:", arr[:k])
print(arr)
