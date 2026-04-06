# table_size = 7
# hash_table = [None] * table_size

# def hash_function(key):
#     return key % table_size

# def insert_linear(key):
#     index = hash_function(key)
#     i = 0
#     while hash_table[(index + i) % table_size] is not None:
#         i += 1
#     new_index = (index + i) % table_size
#     hash_table[new_index] = key

# keys = [8,15,22]

# for key in keys:
#     insert_linear(key)

# print("LINEAR PROBING:")
# print(hash_table)

# two pointers
# input:[2,7,13,11]
# output: 9
nums = [2,7,11,13]
target = 9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
