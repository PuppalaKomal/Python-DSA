#returning indices of two strings
# def two_sum(num,target):
#     hashmap={}
#     for i,num in enumerate(num):
#         diff=target-num
#         if diff in hashmap:
#             return [hashmap[diff],i]
#         hashmap[num]=i
#     return None
# def main():
#     arr=[2,7,11,13]
#     target=9
#     print("Indexes: ",two_sum(arr,target))
# if __name__=="__main__":
#     main()


#counting duplicates in list
def count_duplicates(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
def main():
    arr=[1,1,2,3]
    print("Contains duplicates: ",count_duplicates(arr))
if __name__=="__main__":
    main()
