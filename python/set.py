'''SETS
1. SETS ARE ANNOTES BY {} OR set()
2. sets stores only unique element and remove duplicate value
3. sets are unorderd no indexing
4. sets are hetrogenous
5. sets are semi-mutable'''

# s={1,1,1,1,2,3,4,4,4,5}
# print(s)

#list to set
# l=[1,2,2,3,4,5]
# print(set(l))

'''methods for sets'''

# s={1,2,3,4,5}
# # # s.add(6)          #.add() add a element in set
# # # print(s)


# # s.remove(3)         #.remove() delete a element from set
# # print(s)


# s.discard(100)           #removes the element but will not show any error if the element is not present in set
# print(s)


'''OPERATIONS IN SETS'''

# s1={1,2,3,4}            #.union() or '|' will merge two sets
# s2={4,5,6,7,8}

# # print(f"union -> {s1.union(s2)}")
# print(s1|s2)

# # s1={1,2,3,4}            
# # s2={4,5,6,7,8}

# # print(f"union -> {s1.intersection(s2)}")   #.intersection() or '&' will print common elements only between two sets
# print(s1&s2)
# # s1={1,2,3,4}            
# # s2={4,5,6,7,8}

# # print(f"union -> {s1.difference(s2)}")
# print(s1-s2)                                     #.difference() or '-' will prints that are present in one set but not in another set

# # s1={1,2,3,4}           
# # s2={4,5,6,7,8}

# # print(f"union -> {s1.symmetric_difference(s2)}")          #.symmetric() or '^' will prints that number which are not common (duplicate elements are not printed)
# print(s1^s2)


# s1=frozenset([1,2,3,4,5])         #by using frozenset you cannot add or remove any element from a set
# s1.add(6)
# print(s1)



