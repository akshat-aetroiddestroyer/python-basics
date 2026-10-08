# user define functions

#defining a function
# def hello():
#     print("hello")
#calling a function
# hello()

# def sum(a,b):   #positinal argument
#     print(a+b)

# sum(2,3)
# sum(45,45)

# def introduce(name, age , number):                                         #keyword argument
#     print(f"hello my name is {name} and my age is {age}")

# introduce(age=22,name="akshat",number=1234567780):
#   print(name,age,number)
#introduce(age , name , number)

# def sum(a,b=89):  #default argument
#     print(a+b)
# sum(12)

# def pallindrome(st):       #check multiple strings are pallinfrome or not
#     rev=""
#     for i in st:
#         rev=i+rev
#     if rev==st:
#         print("pallindrome")
#     else:
#         print("not pallindrome")
# pallindrome("madam")
# pallindrome("naman")
# pallindrome("akshat")


# def hello():      # use case of return statement is to return a value from the function to the caller
#     return "yo"
# a=hello() or print(hello())
# print(a)


# def sum(a,b):
#     print(a+b)
# sum(2,3)

# def sum(a,b):
#     return (a+b)
# print(sum(2,3))

# def sum(a,b):
#     print(a+b)
# sum(2,3)
# sum(2,7)
# sum(2,29)
# sum(2,34)
# sum(2,35)

# def sum(a,b):
#     return a+b
# print(sum(2,3))

# def sum(a,b):
#     print(a+b)
# sum(3,9)

# def check_even_odd(n):
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# check_even_odd(4)
# check_even_odd(5)


# def even_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(4)
# even_odd(6)

# def even_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(1)
# even_odd(6)
# even_odd(8)

# def even_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(23)
# even_odd(8)
# even_odd(235)

# def even_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(56)
# even_odd(97)
# even_odd(79)

# def even_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(4)
# even_odd(45)


# def even_odd(n):
#     if n%2==0:

# def square(n):
#     print(n**2)
# square(4)
   

# def square(n):
#     print(n**2)
# square(4)
# n=int(input("enter the number"))
# def square(n):
#     return (n**2)
# print(square(n))

# n=int(input())

# n=int(input("enter number"))
# a=int(input("enter number"))
# def max(n,a):
#     if n>a:
#         print("n is greater")
#     else:
#         print("b is greater ")
# max(n,a)

# n=int(input("enter number"))
# a=int(input("enter number"))
# def max(n,b):
#     if n>a:
#         print("n is greater")
#     else:
#         print('a is greater')
# max(a,n)      

# n=int(input("enter the input "))

# for i in range(n):
#     greatest=0
#     a=int(input("enter the number"))
# def max(a):
#     greatest=0
#     if  a>greatest:
#         greatest=a
# max(greatest)

# def max(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# max(15,25)

# def max(a,b):
#     if a<b:
#         print(a)
#     else:
#         print(b)
# max(2,4)

# def max(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b):
# max(2,6)

# def max(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# max(4,6)

# def max(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# max(5,6)

# def check_number(a):
#     if a==0:
#         print("number is 0")
#     elif a>0:
#         print("number is positive")
#     else:
#         print("number is negative")
# check_number(-8)

# n=int(input("enter number"))
# def check_number(n):
#     if n>=0:
#         print("number is positive")
#     else:
#         print("negative")
# check_number(n)

# n=int(input("enter number"))
# def check_number(n):
#     if n>=0:
#         print(f"{n} is positive")
#     else:
#         print(f"{n} is negative")
# check_number(n)

# n=int(input("enter the number"))
# def check_number(n):
#     if n>=0:
#         print("positive")
#     else:
#         print("negative")



# def simple_intrest(p,r,t):
#     print(p*r*t/100)
# simple_intrest(100,5,2)
# p=int(input("enter the number"))
# q=int(input("enter the number"))
# t=int(input("enter the number"))



# def simple_intreset(p,q,t):
#     print(p*q*t/100)
# simple_intreset(p,q,t)
# simple_intreset(p,q,t)
# simple_intreset(p,q,t)
# simple_intreset(p,q,t)
# n=int(input("enter number"))
# def cube(n):
#     print(n**3)
# cube(n)
# n=int(input("enter number"))
# def eligiblity(n):
#     if n>=18:
#         print("eligble")
#     else:
#         print("not eligible")
# eligiblity(n)




# def factorial(a):
#   fact=1
#   for i in range(1):
#     fact*=i
# factorial(5)



# n=int(input("number"))
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
        
#     print(fact)
# factorial(n)

# n=int(input("enter number"))
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# factorial(n)

# n=int(input("enter number"))
# def digit_count(n):
#     count=0
#     while n>0:
#         count+=1
#         n//=10
#     print(count)
# digit_count(n)


#print  1-30

# def  num(n):     #recursion - a function calling function itself
#     if n==999:
#         return
#     print(n)
#     num(n+1)
# num(1)

# def num(n):    printing the number in reverse
#     if n==31:
#         return
#     num(n+1)
#     print(n)
# num(1)

#fibonacci series(sum of previous two numbers)

# n=int(input("enter number"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# n=int(input("enter number"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# n= int(input("number"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c


# n = int(input("enter the number"))
# a=0
# b=1
# for i in range(n)
#     print(a)
#     c=a+b
#     a=b
#     b=c


# n=int(input("number"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c
    
# n=int(input("number"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c


# n=int(input('number'))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c


# n=int(input("number"))        #check how many number are divisible by 3 and 5 between 1 to n
# count=0
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         count+=1
    
# print(count)


# n=int(input("number"))
# def divisible(n):
#     count=0
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             count+=1
#     print(count)
# divisible(n=35)
# divisible(n=78)
# divisible(n=23)

# n=input("enter any text")        #calculate number of vowels in a string capital and small both
# count=0
# for ch in n:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)

# n=input()
# count=0
# for ch in n:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)


# n=input()
# count=0
# for ch in n:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)



# n=input()
# count=0
# for ch in n:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)


# n=input()
# count=0
# for ch in n:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)

# n=input()
# def vowels(n):
#     for ch in n:
#         if ch in "aeiouAEIOU":
#             count+=1
#     print(count)
# vowels(n)


# n=int(input("enter the umber of input"))    #check the greatest number by creating a function
# def largest(n):
#     greatest=0
#     for i in range(n):
#         a=int(input("enter number"))
#         if a>greatest:
#             greatest=a
#     print(greatest)
# largest(n)


# n=int(input("enter number of input "))
# def largest(n):
#     greatest=0
#     for i in range(n):
#         a=int(input("enter number"))
#         if a>greatest:
#             greatest=a
#     print(greatest)
# largest(n)

# n=int(input("input"))
# def largest(n):
#     count=0
#     for i in range(n):
#         a=int(input("number"))
#         if a>count:
#             count=a

#         print(count)

# largest(n)

# n=int(input("input"))
# def largest(n):
#     count=0
#     for i in range(n):
#         a=int(input("number"))
#         if a>count:
#             count=a
#         print(count)

# largest(n)

# n=int(input("number"))
# def prime(n):
#     i=2
#     count=True
#     while i<n:
#             if n%i==0:
#                 count=False
#                 break
#             i+=1
#     if count and n>1:
#             print("prime")
#     else:
#             print("not prime")
# prime(n)

# n=int(input("number"))
# while n>0:
#     if n%2==0:
        
#      print("not prime")   
# else:
#     print("prime")

# def sum(a,b):
#     print(a+b)
# sum(2,3)

# n=1234
# def reverse(n):
#     rev=0
#     while n>0:
#         last=n%10
#         rev=rev*10+last
#         n//=10
#     print(rev)
# reverse(n)

# n=int(input("number"))
# def palindrome(n):
#     copy=n
#     rev=0
#     while n>0:
#             last=n%10
#             rev=rev*10+last
#             n//=10
#     if copy==rev:
#             print("pallindrome")
#     else:
#             print("not pallindrome")
# palindrome(n)

# a=int(input("number"))
# b=int(input("number"))
# def gcd(a,b):

#     while b!=0:
#         remainder=a%b
#         a=b
#         b=remainder
#     print(a)
# gcd(a,b)

# n=int(input("input"))
# def largest(n):
#     count=0
#     for i in range(n):
#         a=int(input("number"))
#         if a>count:
#             count=a
#     print(count)
# largest(n)

# n=int(input("number"))
# def largest(n):
#     count=0
#     while n>0:
#         last=n%10
#         count=count>last
#         n//=10
#     print(count)
# largest(n)

# n=int(input("enter number"))       #check even or odd by ysing function
# def even_odd(n):
#     even=0
#     odd=0
#     while n>0:
#         last=n%10
#         if last%2==0:
#             even+=1
#         else:
#             odd+=1
#         n//=10
#     print(f"even digits {even}")
#     print(f"odd digits {odd}")
# even_odd(n)


# n=int(input("enter the number"))         #check weather number is armstrong or not by using function
# def armstrong(n):
#     sum=0
#     temp=n
#     length=len(str(n))
#     while n>0:
#         last=n%10
#         sum=sum+last**length
#         n=n//10

#     if sum==temp:
#         print("number is armstrong",sum)
#     else:
#         print("number is'nt armstrong",sum)
# armstrong(n)

# n=int(input("number"))

# for i in range(1,n+1):
#     if i%10==7:
#         print(i , end=" ")


    
