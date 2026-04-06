# Hashing: its a technique used to store and retrieve data using a key.
# In python hashing is implemented using dictionary.
# Hashing allows fast lookup.
# O(1) time complexity.

# open hashing : whenever im getting the same index value colliding with the previous index, it is going to stored in a form of linked list.
# All the collisions are stored as chain.
#     advantages of open hashing:
#        --> easy to implement
#        --> no need to search for empty slots
#        --> table never becomes completely full
#        --> handles many collision.


# closed hashing: all the elements are stored inside the hash table itself.
# --> when a collision occurs we find another empty slot in the table.
# --> No linked list are used. 

# types of closed hashing:
# 1) linear probing: when collision occurs, the next slot should be filled subsequently.
# formula : ( index + i) % table_size.

# (8,15,22) = i   table_size = 7 
# 8%7 = 1

# 2) quadratic probing:
# insteadc of checking next index he jump using squares.
# formula : index + isquare.
# 3) linear probong: (h(key)+i) % table_size
# 4)