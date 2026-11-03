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
    

<<<<<<< Updated upstream
a=(10,20,30,40,50)
b=a.index(30)
print(b)
=======
# a=(10,20,30,40,50)
# b=a.index(30)
# print(b)

# a=[3,2,3,2,2,2]
# n=len(a)
# mid=n//2
# list=[]
# for i in a:
#     if n%2!=0:
#         print('can not divide into 2 parts')
#         break
#     else:
#         for j in a:
#             if a[i]==a[j]:
#                 list.append(a[i])
# print(list)


# def numberOfPairs( nums: list[int]):
#         pairs=0
#         i=0
#         while i<len(nums):
#             j=i+1
#             while j<len(nums):
#                 if nums[i]==nums[j]:
#                     pairs+=1
#                     nums.pop(i)
#                     nums.pop(j)
#                     i=-1
#                     break
#                 j+=1
#             i+=1
#         return(pairs,len(nums))
# print(numberOfPairs([1,3,2,1,3,2,2]))

# nums=[1,5,0,3,5] #select minimum value x and subtract it from every number
# n=len(nums)
# for i in range(n):
#         count=0
#         for j in range(n):
#             if nums[i]==nums[j]:
#                 count+=1
#       if count==1:
#          print(nums[i])

a=(1234)
while a>0:
    last=a%10
    
>>>>>>> Stashed changes
