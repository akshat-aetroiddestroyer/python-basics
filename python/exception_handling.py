'''exception handling 
    1.deal with errors except
       .syntax error
       .indentation error
       . tab error 
    2. there are some error which is called exception 
        like:
              . ZeroDivisionError
              . Traceback
              . name error
              . value error
              '''
'''exception handling
      keyword                   purpose
        - try               - wrap the block of code that might cause an exception
        - except            - handle the exception if it occurs
        - else              - run code only if no exception occurs
        - finally           - run code no matter what whether ther's an exception or not
        - raise             - manually trow an exception'''        

 
# a=int(input('enter'))
# try:
#     print(10/a)
# except ZeroDivisionError:
#     print('sorry u can not divide zero')

# print('ok i have done the division')

# a=int(input('enter'))
# try:
#     print(10/a)
# except Exception as err:
#     print(f'sorry u can not divide zero because there is a array called {err}')
# else:
#     print('good no exception found')
# finally:
#     print('i will run no matter what')

# age = int(input('number'))

   
# if age<10 or age>18:
#         raise ValueError('your age must be between 10 to 18')
# else:
#     print('welcome to the club')
# except Exception as err:

# print('the club will start soon')

# a=[1,2,2,2,3,3,3,1,1]
# d = {}
# for i in a:
#    if i in d.keys():
#         d[i] +=1
#    else:
#        d[i]=1
# print(d)
        
# a=[1,2,2,2,3,3,3,1,1]
# b={}
# for i in a:
#     if i not in b.keys():
#         b[i]=1
#     else:
#         b[i]+=1
# print(b)

# nums = [1, 2, 2, 3, 2, 4, 1]

# for i in set(nums):
#     count = nums.count(i)
#     print(i, "=", count)

# find the nearest element of a given number
# a = [10, 20, 15, 25, 26]
# num = 22

# nearest = a[0]
# for i in range(1, len(a)):
#     current = a[i]

#     if current == num:
#         nearest = current
#         break

#     if current > num:
#         current_diff = current - num
#     else:
#         current_diff = num - current

#     if nearest > num:
#         nearest_diff = nearest - num
#     else:
#         nearest_diff = num - nearest

#     if current_diff < nearest_diff:
#         nearest = currentjdd

# print(f"Nearest element to {num} is {nearest}")

# a = [10, 4, 8, 3, 9]  
# result = []
# for i in range(len(a)-1):
#     result.append(abs(a[i+1] - a[i]))
# print(result)

#group identical elements in pair and represent it by its element once output[1,2,3,1]
# a = [1, 1, 2, 2, 2, 3, 1, 1]
# result = []
# for i in range(len(a)):
#     if i==0 or a[i]!= a[i - 1]:
#         result.append(a[i])
# print(result)
# a = [6, 6, 5, 5, 4, 1]
# hill=0
# valley=0
# i=0
# while i<len(a):
#     if a[i] == a[i - 1]:
#         a.pop(i)
#     else:
#         i += 1
# for i in range(len(a)):
#     if a[i-1]<a[i]>a[i+1]:
#         valley+=1
#     else:
#         hill+=1
# print(valley , hill)

# a = [6, 6, 5, 5, 4, 1]
# hill = 0
# valley = 0
# i = 1
# while i < len(a):
#     if a[i] == a[i - 1]:
#         a.pop(i)
#     else:
#         i += 1
# for i in range(1,len(a) - 1):
#     if a[i - 1] < a[i] > a[i + 1]:
#         hill += 1
#     elif a[i - 1] > a[i] < a[i + 1]:
#         valley += 1
# print(valley + hill)
# a = [6, 6, 5, 5, 4, 1]

# hill = 0
# valley = 0

# i = 1
# while i < len(a):
#     if a[i] == a[i - 1]:
#         a.pop(i)
#     else:
#         i += 1

# for i in range(1, len(a) - 1):
#     if a[i - 1] < a[i] > a[i + 1]:
#         hill += 1
#     elif a[i - 1] > a[i] < a[i + 1]:
#         valley += 1

# print(valley + hill)

# nums = [2, 4, 1, 1, 6, 5]

# i = 1
# while i < len(nums):
#     if nums[i] == nums[i - 1]:
#         nums.pop(i)
#     else:
#         i += 1
# hill = 0
# valley = 0
# for i in range(1, len(nums) - 1):
#     if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
#         hill += 1
#     elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
#         valley += 1
# print(hill, valley)
# print(hill + valley)
# a=0
# b=0
# for i in range(7):
#     n=input("p for present a for absent:")
#     if n=="p":
#         a=a+1
#     else:
#         b=b+1
# print("present",a)
# print("absent",b)
# pas=0
# fail=0
# for i in range(10):
#     n=int(input('enter'))
#     if n==1:
#         pas+=1
#     else:
#         fail+=1
# print(f'pass products- {pas} and fail products- {fail}')


# n=int(input('enter'))
# for i in range(2,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)

# n='hello'
# sum=''
# for i in n:
#     sum=i+sum
# print(sum)
        
# n=int(input('enter '))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==3:
#     print('yes')
# else:
#     print('no')
        

# n=int(input('enter'))
# a=len(str(n))
# copy=n
# sum=0
# while n>0:
#     last=n%10
#     sum+=last**a
#     n//=10
# if sum==copy:
#     print('strong')
# else:
#     print('not')

# n=int(input("enter the number"))
# sum=0
# temp=n
# length=len(str(n))
# while n>0:
#     last=n%10
#     sum=sum+last**length
#     n=n//10
# l=int(input())
# r=int(input())
# for n in range(l , r+1):
#           print(n,end=': ')
#           for i in range(1 , n+1):
#                if n%i==0:
#                     print(i,end=' ')
#           print()
# n=int(input("enter the number"))
# sum=0
# temp=n
# length=len(str(n))
# while n>0:
#     last=n%10
#     sum=sum+last**length
#     n=n//10
# if sum==temp:
#     print('armstrong')
# else:
#     print('not')

# n = "abcdef"
# a = "bcadfe"
# if len(n) == len(a):
#     for i in n:
#         if n.count(i) != a.count(i):
#             print("Not Anagram")
#             break
#     else:
#         print("Anagram")
# else:
#     print("Not Anagram")