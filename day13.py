#sliding window
# it is a technique which we use when we need to work with substrings of fixed variable size efficiently
# instead of  recall waiting values for very subarray  to slide window or over the array

#approach:
# 1. start with a window(subset of arrray)
# 2. expand the window move right pointer
# 3. shrink the window move left pointer
# 4. maintain required condition (sum, count,etc)

#COUNTING SUBARRAYS OF K PROBLEM
# COUNTING HOW AMNY SUBARRY OF SIZE K EXISTS
# EG:ARR=[1,2,3,4,5]
# K=3
# [1,2,3],[2,3,4],[3,4,5]

# def count_subarrays(arr, k):
#     count = 0
    
#     for i in range(len(arr)):
#         if i >= k - 1:
#             count += 1
#     return count
# def main():
#     arr = [1, 2, 3, 4, 5]
#     k = 3
#     print(count_subarrays(arr, k))
# main()

# def max_sum(arr, k):
#     window_sum = 0
#     max_sum = 0
#     for i in range(len(arr)):
#         window_sum += arr[i]
#         if i >= k - 1:
#             max_sum = max(max_sum, window_sum)
#             window_sum -= arr[i - (k - 1)]
#     return max_sum
# def main():
#     arr = [1, 2, 3, 4, 5]
#     k = 3
#     print(max_sum(arr, k))