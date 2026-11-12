# <<<<<<< HEAD
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
# =======
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
#         v<<<<<<< Updated upstream
# >>>>>>> a4ab258 (Add exception handling examples and explanations)
# =======
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
# a=[1,1,1,2,2,2,3,3,3,4,4,4,4]
# freq={}
# for num in a:
#     freq[num]=freq.get(num,0)+1
# print(freq)
# a=[1,1,1,2,2,2,3,3,3,4,4,4,4]
# freq={}
# for i in a:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq) 



# l=int(input('enter'))                        1
# r=int(input('enter'))
# for i in range(l,r+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# l=int(input('e'))
# r=int(input('enter'))                           2
# for i in range(l,r+1):
#     coumt=0
#     for j in range(1,i+1):
#         if i%j==0:
#             coumt+=1
#     if coumt==2:
#         print(i)

# l=1342                                         3
# r=34544
# for i in range(l,r+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         print(i)

# l=4
# r=5
# for i in range(l,r+1):                         4
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# a=9                                           5
# b=20
# for i in range(a,b+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# a=10
# for i in range(1,a+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)

# a=30
# for i in range(1,a+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)

# a=100
# for i in range(1,a+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==3:
#         print(i)

# l=2
# r=5
# for i in range(l,r+1):
#     print(i,end=': ')
#     for j in range(1,i+1):
#         if i%j==0:
#             print(j,end=' ')
#     print()
# l=2
# r=5
# for i in range(l , r+1):
#           print(i,end=': ')
#           for j in range(1 , i+1):
#                if i%j==0:
#                     print(i,end=' ')
#           print()

# n=7
# sum=0
# copy=n
# for i in range(1, n):
#     if n % i == 0:
#         sum=sum+i
# if copy==sum:
#     print('strong')
# else:
#     print('not strong')
# n=int(input('input'))
# i=0
# largest=None
# smallest=None
# for i in range(n): 
#     a=int(input('enter'))
#     if i>largest:
#         largest=i
# smallest=largest
# for i in n:
#     if i<smallest:
#         smallest=i
# diffrence=largest-smallest
# print(f'{largest}-{smallest}={diffrence}')
# n=int(input("input"))
# largest=float("-inf")
# smallest=float("inf")
# for i in range(n):
#     a=int(input("enter"))
#     if a>largest:
#         largest=a
#     if a<smallest:
#         smallest=a
# diffrence=largest-smallest
# print(f'{largest}-{smallest}={diffrence}')
# n = int(input("How many numbers? "))
# largest = float("-inf")
# smallest = float("inf")
# for i in range(n):
#     a = int(input("Enter your number: "))
#     if a > largest:
#         largest = a
#     elif a < smallest:
#         smallest = a
# difference = largest - smallest
# print("Largest:", largest)
# print("Smallest:", smallest)
# n=int(input(''))
# a=0
# b=1
# for i in range(n+1):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# l=10
# r=40
# for i in range(l,r+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)
# l=4
# r=34
# for i in range(l,r+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# l=4
# r=100
# for i in range(l,r+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# l=30
# for i in range(1,l+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)

# n=233
# for i in range(1,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)

# n=1000
# for i in range(1,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)
# l=1
# r=5
# for i in range(l,r+1):
#     print(i,end=': ')
#     for j in range(1,i+1):
#         if i%j==0:
#             print(j,end=' ')
#     print()

# l=1
# r=100
# max_count=0
# num=0
# for i in range(l,r+1):
#     print(i,end=': ')
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#             print(j,end=' ')
#     if count>max_count:
#         max_count=count
#         num=i
#     print()
# print(f'the num which has max factors is:- {num} and its number of factor are:- {max_count}')
# n=6
# copy=n
# sum=0
# for i in range(1,n):
#         if n%i==0:
#             sum=sum+i
# if sum==copy:
#     print('perfect')
# else:
#     print('not')
# n=7
# sum=0
# copy=n
# for i in range(1, n):
#     if n % i == 0:
#         sum=sum+i
# if copy==sum:
#     print('strong')
# else:
#     print('not strong')
# a=[-1,0,1,2,-1,-4]
# target=0
# ans=set()
# j=0
# for i in range(len(a)):
#         print(i)
#         j+=1
#         print(j)
#         for k in range(j+1,len(a)):
#             print(k)
#             if a[i]+a[j]+a[k]==target:
#                 ans.add(tuple(sorted([a[i],a[j],a[k]])))
# print(ans)
# print(list(ans))
# for i in ans:
#     l.append(list(i))
# print(l)
#                 # for l in ans:
                #     l=l.sorted()
            
# class Solution:
#     def threeSum(self, a: list[int]) -> list[list[int]]:
#             target=0
#             ans=set()
#             for i in range(len(a)):
#                 for j in range(i+1,len(a)):
#                     for k in range(j+1,len(a)):
#                         if a[i]+a[j]+a[k]==target:
#                             ans.add(tuple(sorted([a[i],a[j],a[k]])))
#             return [list(x) for x in ans]
# n=int(input('enter'))
# a=0
# b=1
# for i in range(n+1):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# n=6
# copy=n
# sum=0
# for i in range(1,n):
#         if n%i==0:
#             sum=sum+i
# if sum==copy:
#     print('')
# else:
#     print('not')

# n=145
# copy=n
# sum=0
# while n>0:
#     digit=n%10
#     factor=1
#     for i in range(1,digit+1):
#         factor=factor*i
#     sum=sum+factor
#     n//=10
# if sum==copy:
#     print('perfect')
# else:
#     print('not')

# a=[10,20,30,40,50]
# print(a[0])
# n=6
# a=n**2
# b=n
# while a>0:
#     last=a%10
#     if last==n:
#         print('yes it is automorphic number')
#         break
#     else:
#         print('no it is not a automorphic number')
#         break
#     a//=10
# if last==5:
#     print('yes')
# else:
#     print('no')

# a=12
# b=15
# while b!=0:
#     a,b=b,a%b
# print(a)
# a=145
# copy=a
# sum=0
# while a>0:
#     last=a%10
#     a//=10
# for i in range(a):
#     if a%i==0:
#         sum+=i
# print(sum)

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
# n=145
# sum=0
# copy=n
# fact=1
# while n>0:
#     last=n%10
#     fact*=n
#     n//10
# print(fact)
# # for i in range(1, last):
#     if last % i == 0:
#         sum=sum+i
# if copy==sum:
#     print('strong')
# else:
#     print('not strong')
# >>>>>>> Stashed changes


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
# >>>>>>> a4ab258 (Add exception handling examples and explanations)

# n=145
# sum=0
# while n>0:
#     fact=1
#     last=n%10
#     for i in range(1,last+1):
#         fact*=i
#     sum+=fact
#     n//=10
# print(sum)
# n=145
# sum=0
# while n>0:
#     fact=1
#     last=n%10
#     for i in range(1,last+1):
#         fact*=i
#     sum+=fact
#     n//=10
# print(sum)

# n=123
# sum=0
# while n>0:
#     fact=1
#     last=n%10
#     for i in range(1,last+1):
#         fact*=i
#     sum+=fact
#     n//=10
# print(sum)
# a=[1,2,3,4,5,6,7,8,9,10]
# target=20
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         for k in range(j+1,len(a)):
#             if a[i]+a[j]+a[k]==target:
#                 print(a[i],a[j],a[k])

# class Solution:
#     def threeSum(self, a: list[int]) -> list[list[int]]:
#             target=0
#             ans=set()
#             for i in range(len(a)):
#                 for j in range(i+1,len(a)):
#                     for k in range(j+1,len(a)):
#                         if a[i]+a[j]+a[k]==target:
#                             ans.add(tuple(sorted([a[i],a[j],a[k]])))
#             return [list(x) for x in ans]
# n=1234
# greatest=float('-inf')
# smallest=float('inf')
# while n>0:
#     last=n%10
#     if last>greatest:
#         greatest=last
#     elif last<smallest:
#          smallest=last
#     n//=10
# print(greatest , smallest)
# smallest=float('inf')
# while n>0:
#     last=n%10
#     if last<smallest:
#         smallest=last
#     n//=10
# print(smallest)

# n=23
# lis=[]
# while n!=1 and n not in lis:
#     lis.append(n)
#     sum=0
#     temp=n
#     while temp>0:
#         last=temp%10
#         a=last**2
#         sum+=a
#         temp//=10
#     n=sum
# if n==1:
#     print('happy')
# else:
#     print('not happy')
# print('not happy')
# print(sum)
# n=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]
# a=[]
# for i in n:
#     if i not in a:
#         count=0
#         for j in n:
#             if i==j:
#                 count+=1
#         print(i ,'-', count)
#         a.append(i)
# n=111122233444444
# a=[]
# while n>0:
#     last=n%10
#     n//=10
#     temp=n
# for i in temp:
#     if i not in a:
#         count=0
#         for j in n:
#             if i==j:
#                 count+=1
#         print(i ,'-', count)
#         a.append(i)
# color=[1,3,1,3,1,1,3]
# diff=0
# for i in range(len(color)):
#     for j in range(i+1 , len(color)):
#         if i<j:
#             diff=abs(j-i)
# print(diff)

# nums=[0,1,2]
# count=0
# smallest=float('inf')
# n=len(nums)
# for i in range(n):
#     if i%10==nums[i]:
#         count+=1
#         # print(nums[i])
#     if i<smallest:
#         smallest=i
# print(count , smallest)

# n=len(nums)
# for i in range(n):
#     if i%10==nums[i]:
#         print(i)
#     else:
#         print(-1)


# gain=[-5,1,5,0,-7]
# sum=0
# b=[]
# for i in gain:
#     sum+=i
#     b.append(sum)
# max=0
# for i in b:
#     if i>max:
#         max=i
# print(max)

# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         sum = 0  # Stores the current altitude, starting from 0
#         b = []  # Empty list to store the altitude after every movement
#         for i in gain:  # Loops through each value in the gain list
#             sum += i  # Adds the current gain to the previous altitude
#             b.append(sum)  # Stores the updated altitude in the list b
#         max = 0  # Assumes the highest altitude is initially 0
#         for i in b:  # Loops through all the calculated altitudes
#             if i > max:  # Checks if the current altitude is greater than the maximum
#                 max = i  # Updates max with the new highest altitude
#         return max  # Returns the highest altitude reached
# seats = [3,1,5]
# students = [2,7,4]
# seats.sort()
# students.sort()
# ans=0
# for i in range(len(seats)):
#     ans+=abs(seats[i]-students[i])
# print(ans)


# n=int(input('enter'))
# a=int(input('enter'))
# factor_1=[]
# factor_2=[]
# for i in range(1,n):
#     if n%i==0:
#         factor_1.append(i)
# for j in range(1,a):
#     if a%j==0:
#         factor_2.append(j)
# greatest=0
# for i in factor_2:
#     if i in factor_1:
#         if i>greatest:
#             greatest=i
# print(greatest)

# def gcd(a,b):
#     while a>0:
#         remainder = b%a
#         b = a
#         a = remainder
#     return b
# gcd(10,2)

# nums = [2,5,6,9,10]
# greatest=0
# for i in nums:
#     if i>greatest:
#         greatest=i
# smallest=greatest
# for i in nums:
#     if i<smallest:
#         smallest=i
# a=greatest
# b=smallest
# c=[]
# d=[]
# for i in range(1,a+1):
#     if a%i==0:
#         c.append(i)
# for j in range(1,b+1):
#     if b%j==0:
#         d.append(j)
# maximun=0
# for i in d:
#     if i in c:
#         if i>maximun:
#             maximun=i
# print(maximun)


# nums = [2,5,6,9,10]
# maxi=max(nums)
# mini=min(nums)
# a=[]
# b=[]
# for i in range(1,maxi+1):
#     if maxi%i==0:
#         a.append(i)
# for j in range(1,mini+1):
#     if mini%j==0:
#         b.append(j)
# maximum=0
# for i in a:
#     if i in b:
#         if i>maximum:
#             maximum=i
# print(maximum)
# s = "abaccb"
# count=0
# for i in range(s):
#     count=(i[0]-i[2])-1
# print(count)
# --