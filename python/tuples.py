'''1. tuples are ordered
   2. annoated by parentheses
   3. tuples are immutable
   4. tuples can store duplicate value
   5. tuples are hetrogenous '''

# a=(1,2,3,4,5,6)
# print(type(a))

# a=(1,2,3,4,5,6)     #traversing tuples
# for i in a:
#     print(i)

# a=(1,2,3,4,5,6)           #traversing through index
# for i in range(len(a)):
#     print(i)
# help(tuple)
'''there are only 2 methods in tuples .index() and .count()'''
# a=(1,2,3,4,5,6)
# index=a.index(6)
# print(index)

# a=(1,2,3,4,5,6,6,6)
# count=a.count(6)
# print(count)

# a,b,c,d = (1,2,3,4)     #this is called unpacking we're packing this tuples in variables
# print(a)
'''OPERATIONS:

+ -> concatenation

a=(1,2)
b=(3,4)
print(a+b)

* -> repetition

print(a*5)'''

# a=(1,2,[3,4,5])
# a[2].append(100)
# print(a)

# a=(1,2,3,4,5)
# sum=0
# for i in a:
#     sum=i+sum
# print(sum)

# a=10,20,30,40,50
# print(tuple(a))

# a=(10,20,30,40,50)
# print(a[0] , a[4])


# a=[1,2,3,4,5,6]
# target=6
# n=len(a)

# for i in range(n):
    
#     for j in range(i+1 ,n):
        
#         if (a[i]+a[j])==target:
#           print(a[i] , a[j])
    
# a=(1,2,3,4,5,6,7,7,7,7)
# countt=a.count(7)
# print(countt)   
    

a=(10,20,30,40,50)
b=a.index(30)
print(b)
