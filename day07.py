# Array:
#     collection of elements 
#     stored in contiguous memory locations
#     in python we use list
# arr=[1,2,3,4,5]
# for num in arr:
#     print(num)
# # to add a number 
# arr.append(6)
# # to update a number
# arr[0]=20

# FINDING SUM OF ARRAY
# def find_sum(arr):
#     total=0
#     for num in arr:
#         total+=num
#     return total
# def main():
#     arr=[1,2,3,4,5]
#     print("sum of array is: ",find_sum(arr))
# if __name__=="__main__":
#     main()
# # finding the maximum element in the array
# def find_max(arr):
#     max=arr[0]
#     for num in arr:
#         if num>max:
#             max=num
#     return max
# def main():
#     arr=[11,22,33,44,55,100]
#     print("maximum element is: ",find_max(arr))
# if __name__=="__main__":
#     main()

# finding the second largest element in the array
def finding_2nd_largest(arr):
    max1=max(arr)
    max2=arr[0]
    for num in arr:
        if num>max2 and num<max1:
            max2=num
    return max2
def main():
    arr=[11,22,33,44,55,100]
    print("second largest element is: ",finding_2nd_largest(arr))
if __name__=="__main__":
    main()

# counting even numbers in an array
def count_even(arr):
    count=0
    for num in arr:
        if num%2==0:
            count+=1
    return count
def main():
    arr=[11,22,33,44,55,100]
    print("count of even numbers is: ",count_even(arr))
if __name__=="__main__":
    main()
