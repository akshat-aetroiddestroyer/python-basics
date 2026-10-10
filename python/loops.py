# for loop

# a = range(1,21,1)

# for i in a:
# #     print(i)

# for i in range(10,81,1):
#     print(i)
# for i in range(-52,40,1):
#     print(i)    

# n = int(input("tell your number"))
# for i in range(n,n*11,n):
#     print(i)   

# n = int(input("enter number"))
# for i in range(1,n+1,1):
#     print(i)

# n=int(input("enter number"))
# for i in range(n,0,-1):
#     print(i)

# n=int(input("enter number"))
# for i in range(n,0,-1):
#     print(i)

# n=int(input("enter number"))
# for i in range(1,n+1,2):
#     print(i)

# n = int(input("tell your number"))
# for i in range(n,n*11,n):
#     print(i)   

# n=int(input("enter number"))
# for i in range(1,n,1):      #to be aksed
#     print(i)

# n=int(input("enter"))
# for i in range(n,):
#     print(i)
# n = int(input("tell me the number"))
# sum=0  #sum of natural number till 10
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# n=int(input("tell the number"))
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print(factorial)

# n=int(input("tell me the number")) 
# for i in range(1,n+1,1):
#     if n%i==0:
#         print(i)

# n=int(input("yell me your number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# n=int(input("number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)    

# a=0
# b=0
# for i in range(10):
#     n=int(input("enter 1 for pass and 0 for fail"))

#     if n==1:
#         a+=1
#     else:
#         b+=1
# print("pass",a)
# print("fail",b)

# a=0
# b=0
# for i in range(7):
#     n= input("p for present a for absent:")
#     if n=="p":
#         a=a+1
#     else:
#         b=b+1
# print("present",a)
# print("absent",b)
    

# a=0
# b=0
# for i in range(7):
#     n=input("p for present a for absent")
#     if n=="p":
#         a=a+1
#     else:
#         b=b+1
# print("present",a)
# print("absent",b)

# a=0 

# b=0
# for i in range(7):
#     n=input("p for prensent a for absent")
#     if n=="p":
#         a=a+1
#     else:
#         b=b+1
# print("present",a)
# print("absent",b)


# a=0
# b=0
# for i in range(7):
#     n=input("p for present a for absent")
#     if n=="p":
#         a=a+1
#     else:
#         b=b+1
# print("present",a)
# print("absent",b)

# a=0
# b=0
# for i in range(7):
#     n=input("p for present a for absent")
#     if n=="p":
#         a=a+1
#     else:
#         b=b+1
# print("present",a)
# print("absent",a)
# sum=0
# count=0
# for i in range(1,8):
#     n=int(input("enter the saving amount"))
#     sum=sum+n
#     if n>500:
#          count=count+1
#          
# print("totalsaving",sum)
# print("no. of days saving was greater",count)

# sum=0
# count=0
# for i in range(1,8):
#     n=int(input("enter the electricity cosumption in units"))
#     sum=sum+n
#     if n>10:
#         count=count+1
# print("total units",sum)
# print("no. of day when unit is greater than 10",count)
    
# p=0
# e=0

# for i in range(10):
#     n=input("p for present and a for absent")
#     if n=="p":
#         p=p+1
#     else:
#         e=e+1
# percantage=(p/10)*100
# print("total no. of p",p)
# print("total no. of a",e)a

# print(percantage)
# if percantage>=75:
#     print("attendance is more than 75")
# else:
#     print("attendance is less than 75")


# pcount=0
# ecount=0

# for i in range(10):
#     n=input("p for present and a for present")
#     if n=="p":
#         pcount+=1
#     else:
#         ecount+=1
# percentage=(pcount/10)*100
# print("total no. of present",pcount)
# print("totoal no. of absent",ecount)
# print(percentage)
# if percentage>=75:
#     print("attedence is more than 75")
# else:
#     print("precentage is less than 75")

# n=int(input("enter number"))                   #check the number is prime or coposite(break)
# for i in range(2,n):
#     if n%i==0:
#         print("number is a composite number")
#         break
# else:
#     print("number is prime")

# n=int(input("enter number"))
# for i in range(2,n):
#     if n%i==0:
#         print("number is composite")
#         break
# else:
#     print("number is prime")   
# 
# name="abhISHEK"    #print the number of upper case and lower case letters in the string
# upper=0
# lower=0
# for i in name:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
# print(f"upper case letters: {upper}")
# print(f"lower case letters: {lower}")


# n=int(input("enter number"))
# count=0
# for i in range(1,n+1):
#     if i%3==0:
#         count+=1
# print(count)

# n=int(input("enter number"))

# count=0
# for i in range(1,n+1):
#     if i%3==0:
#         count+=1
# print(count)

# n=int(input("enter number"))
# count=0
# for i in range(1,n+1):
#     if i%3==0:
#         count+=1
# print(count)

# n=int(input("enter number"))

# count=0
# for i in range(1,n+1):
#     if i%3==0:
#         count+=1
# print(count)

# a=int(input("enter number of inputs"))
# count=0
# for i in range(a):
#     n=int(input("enter number"))
#     if n>count:
#         count=n
# print(count)

# a=int(input("enter the number of input"))
# count=0
# for i in range(a):
#     n=int(input("enter the number"))
#     if n>count:
#         count=n
# print(count)

   
# a=int(input("enter the inputs"))
# count=0
# for i in range(a):
#     n=int(input("enter the number"))
#     if n>count:
#         count=n
# print(count)

# a=int(input("enter the number of input"))
# average=0
# sum=0
# for i in range(a):
#     n=int(input("enter the number"))
#     sum+=n
#     average=sum/a
# print("average of the number is",average)

# n=int(input("enter number"))
# for i in range(1,n+1):
#     if i%10==0:
#         print(i)

# n=int(input("enter the umber of input"))
# greatest=0
# for i in range(n):
#     a=int(input("enter number"))
#     if a>greatest:
#         greatest=a
# print(greatest)




                                           

    



    