#SUM OF SUBARRAYS OF SIZE K
# def sumOfSubarrays(arr,k):
#     windows_sum = 0
#     result = []
#     for i in range(len(arr)):
#         windows_sum += arr[i]
#         if i >= k - 1:
#             result.append(windows_sum)
#             windows_sum -= arr[i - k + 1]
#     return result
# def main():
#     arr=[1,2,3,4,5]
#     k=3
#     print(sumOfSubarrays(arr,k))
# main()

# find average of all the sub arrarys of the sum k arr=[1,2,3,4,5]
def averageOfSubarrays(arr,k):
    windows_avg = 0
    result = []
    for i in range(len(arr)):
        windows_avg += arr[i]
        if i >= k - 1:
            result.append(windows_avg/k)
            windows_avg -= arr[i - k + 1]
    return result
def main():
    arr=[1,2,3,4,5]
    k=3
    print(averageOfSubarrays(arr,k))
main()
