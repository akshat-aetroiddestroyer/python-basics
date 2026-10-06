#while jab tak koi condition true hai tab tak loop chalta rahega:
#    tab tak yeh loop chlega


# a=10
# while a>=1:
#     print(a)
#     a=a-1


# a=input("enter the password")
# while a!="abhishek1234":
#     a=input("enter the password")
# print("access granted")

# n=int(input("enter the number")) #print the table of the number
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

#print even number from 2 to 20 and sum


# i=2
# sum=0
# while i<=20:
#     sum+=i
#     print(i)
#     i+=2
# print("sum of even number from 2 to 20 is",sum)

#print a number n in reverse order

# a=int(input("tell me your number")) 

# rev=0

# while a>0:
#     last=a%10
#     rev=rev*10+last
#     a=a//10

# print(rev)

#print the total number of digits in a number
# a=int(input("tell me your number"))
# count=0
# while a>0:
#     count+=1
#     a=a//10
# print("total number of digits in the number is",count)

# number is armstrong or not                  
# n=int(input("enter the number"))
# sum=0
# temp=n
# length=len(str(n))
# while n>0:
#     last=n%10
#     sum=sum+last**length
#     n=n//10

# if sum==temp:
#     print("number is armstrong",sum)
# else:
#     print("number is'nt armstrong",sum)



# a=256
# while a>0:
#      print(a%10)
#      a=a//10

# a=int(input("tell me your number")) #print the number in revere
# rev=0

# while a>0:
#     rev=rev*10+a%10
#     a=a//10

# print(rev)

# a=int(input("tell me your number"))  #seperate the number

# while a>0:
#     print(a%10)
#     a//=10

# a=int(input("tell me your number"))  #verify pallindromic number reverse==original
# copy=a
# rev=0

# while a>0:
#     rev=rev*10+a%10
#     a//=10
# if copy==rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic")

# import random       #guess the number game

# num=random.randint(1,10)
# tries=0
# while True:
#     guess=int(input("guess number between 1 and 10"))
#     if num==guess:
#         tries+=1
#         print(f"you're right you guessed a number in {tries} tries")
#         break

#     elif num<guess:
#         print("go a little lower")
#         tries+=1
#     elif num>guess:
#         print("go a little higher")
#         tries+=1
#     else:
#         tries+=1
#         print("you're wrong")


# a=int(input("tell me your number"))  
# copy=a
# rev=0

# while a>0:
#     rev=rev*10+a%10
#     a//=10
# if copy==rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic")

# n=int(input("enter number"))
# copy=n
# reverse=0
# while n>0:
#     last=n%10
#     reverse=reverse*10+last
#     
# if copy==reverse:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")

# n=int(input("enter number"))
# copy=n
# rev=0
# while n>0:
#     last=n%10
#     rev=rev*10+last
#     n//=10
# if copy==rev:
#     print("pallindromic")
# else:
#     print("not a pallindromic")

# n=int(input("enter number"))
# copy=n
# rev=0
# while n>0:
#     last=n%10
#     rev=rev*10+last
#     n//=10
# if copy==rev:
#     print("pallindromic")
# else:
#     print("not pallindromic")

# n=int(input("enter number"))
# rev=0
# while n>0:
#     last=n%10
#     rev=rev*10+last
#     n//=10
# print("reverse number is",rev)


#how many digits are greater than 5
# n=int(input("enter number"))
# count=0

# while n>0:
#     last=n%10
#     if last>=5:
#         count+=1
#     n//=10
# print("number of digits greater than 5 is",count)

# n=int(input("enter number"))
# count=0
# while n>0:
#     last=n%10
#     if last>5:
#         count+=1
#     n//=10
# print(count) 

# n=int(input("enter number"))
# product=1
# while n>0:
#     last=n%10
#     product=product*last
#     n//=10
# print(product)

# n=int(input("enter the number"))
# count=0
# while n>0:
#     last=n%10
#     if last==7:
#         count+=1       
#     n//=10
# if count>0:
#     print("present")
# else:
#     print("not present")

    



# n=int(input("enter number"))
# count=0
# while n>0:
#     last=n%10
#     if last%3==0:
#         count+=1
#     n//=10
# print(count)

# n=int(input("enter the number"))
# new=0
# while n>0:
#     new=new*10+9
#     n//=10
# print(new)

# n=int(input("enter number"))
# largest=0
# second=0
# while n>0:
#     last=n%10
#     if last>

# n=int(input("enter the number"))
# even=n
# while n>0:
#     last=n%10
#     if last%2!=0:
#         print("odd number is present")
#         break
#     n//=10
# else:
#     print("even number is present")
    



# n=int(input("enter number"))

# while n>0:
#     n=n//10
#     break
# print(n)

# n=int(input("enter number"))
# largest=0
# second=0
# while n>0:
#     last=n%10

# n=int(input("enter nummber"))
# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("number is a perfect number",)
# else:
#     print("number is not a perfect number",)
# count=0
# n=int(input("enter number"))
# while n>0:
#     last=n%10
#     if last%3==0 and last%5==0:
#         count+=1
#     n//=10
# print(count)


# factorial=1
# n = int(input("enter number"))
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)


# n=int(input("enter number"))
# fact=1
# sum=0

# while fact<n:
#     if n%fact==0:
#         sum+=fact
#     fact+=1
# if sum==n:
#     print("perfect number")
# else:
#     print("not a perfect number")


