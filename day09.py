# Brute force Approch:
# solving a problem by using most straight forward method
# Disadvantages:       
# USing Nested Loop O(n square)
# Trying every combination
# Making every posibility
# Optimized Approch
# We are using it to reduce time complexity by # Using proper data structure
                                                # Sorting
                                                # Hashing
                                                # MAthematical methods
# def pair_sum(arr,sum):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==sum:
#                 return (arr[i],arr[j])
#     return None
# def main():
#     arr = [1,2,3,4,5,6,7,8,9,10]
#     sum = 10
#     print(pair_sum(arr,sum))
# if __name__=="__main__":
#     main()
    
def two_sum_optimised(arr,target):
    seen=set()
    for num in arr:
        diff=target-num
        if diff in seen:
            return (diff,num)
        seen.add(num)
    return None
def main():
    arr=[1,2,3,4,5,6,7,8,9,10]
    target=10
    print(two_sum_optimised(arr,target))
if __name__=="__main__":
    main()

def count_duplicate(arr):
    count= 0
    for i in range(len(arr)):
        if arr[i] in arr[:i]:
            count+=1
    return count
def main():
    arr=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
    print("count of duplicates is: ",count_duplicate(arr))
if __name__=="__main__":
    main()
