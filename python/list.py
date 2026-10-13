# a=[7,2,3,1,4,5]
# smallest=a[0]
# for i in a:
#     if i<smallest:
#         smallest=i
# print(smallest)

# a=[1,2,3,4,5,6]

# smallest=a[0]
# while a>0:
#     if a>smallest:
#         smallest=a
# print(smallest)

# a=[1,2,3,4,5,6]
# smallest=a[0]
# for i in a:
#     if i<smallest:
#         smallest=i
# print(smallest)


# a=[1,2,3,4,5,5,678,2]
# small=a[0]
# for i in a:
#     if i<small:
#         small=i
# print(small)

# a=[54,35,76654,34]
# small=a[0]
# for i in a:
#     if i<small:
#         small=a
# print(small)


# a=[12,34,-12,34,-34,-56]
# pos=0
# neg=0

# for i in a:
#     if i>0:
#         pos+=1
#     else:
#         neg+=1
# print(f"number of positive numbers: {pos}")
# print(f"number of negative: {neg}")


# a=[12,34,-12,34,-34,-56]
# p=0
# q=0
# for  i in a:
#     if i>0:
#         p+=1
#     else:
#         q+=1
# print(p)
# print(q)

# a=[12,34,-12,34,-34,-56]
# p=0
# q=0
# for i in a:
#     if i>0:
#         p+=1
#     else:
#         q+=1
# print(p)
# print(q)


# a=[12,34,-12,34,-34,-56]
# p=0
# q=0
# for i in a:
#     if i>0:
#         p+=1
#     else:
#         q+=1
# print(p)
# print(q)

# a=[12,34,-12,34,-34,-56]
# p=0
# q=0
# for i in a:
#     if i>0:
#         p+=1
#     else:
#         q+=1
# print(p)
# print(q)

# a=[12,34,-12,34,-34,-56]
# p=0
# q=0
# for i in a:
#     if i>0:
#         p+=1
#     else:
#         q+=1
# print(p)
# print(q)

# a=[10,20,30,40]
# sum=0
# count=1

# count = 1
# total = 0

# while count <= 5:
#     n = int(input("Enter a number: "))
#     total += n
#     count += 1

# avg = total / count

# print("Average:", avg)

# sum=0
# count=int(input("number of input"))
# for i in range(count):
#     a=int(input("enter number"))
#     sum+=a
# if count>0:
#     avg=sum/count
#     print(avg)

    
# a=[1,2,2,2,4,5,6,7,8]
# count=0
# for i in range(len(a)):
#     if a[i]==2:
#         count+=1
# print(count)

# sum=0
# count=int(input("input"))
# for i in range(count):
#     a=int(input("enter number"))
#     sum+=a
# if count>0:
#     avg=sum/count
#     print(avg)

# # a=[10,20,30,40,50]
# # couunt=1
# # sum=0
# # while couunt<=5:
#     sum+=a
#     couunt+=1

# avg=sum/couunt
# print(avg)

# count = 1
# total = 0
# n=[10,20,30,40,50]
# while count>0:
#     total += n
#     count += 1

# avg = total / count
# print(avg)

#print list in element in reverse

# a=[10,20,30,40,50]
# n=len(a)
# mid=n//2
# for i in range(mid):
#     a[i],a[n-1-i]=a[n-1-i],a[i]

# print(a)

#print positive and negative elements separate
# a=[12,34,-12,34,-34,-56]

# print("postive")
# for elem in a:
#     if elem>0:
#         print(elem)
# print("negative")
# for elem in a:
#         if elem<0:
#              print(elem)


# a=[10,20,30,40,50]
# couunt=1
# sum=0
# while couunt<=5:
#     sum+=a
#     couunt+=1

# avg=sum/couunt
# print(avg)

# a=[10,20,30,40]
# # sum=0
# # count=1

# length = len(a)
# total = 0

# for elem in a:
    
#     total += elem
    

# avg = total / length

# print("Average:", avg)

# a=[2,96,69,77,145,20]

# greatest=a[0]

# for i in a:
#     if i>greatest:
#         greatest=i
# print(greatest)
# n=a.index(greatest)
# print(n)

# a=[7,2,3,1,4,5]
# smallest=a[0]
# index=0
# for i in a:
#     if i<smallest:
        
#         smallest=i
# print(smallest)
# a=[7,2,3,1,4,5]
# smallest=a[0]
# index=0
# for i in range(len(a)):
#     if i>greatest:
#         greatest=i
#         index=i
# print(greatest,index)
# n=a.index(greatest)n

# a=[1,2,3,4,5,45,6,7]         #find the second greatest number
# greatest=a[0]
# second=a[0]

# for i in a:
#     if i>greatest:
#         second=greatest
#         greatest=i
#     elif i>second:
#         second=i
# print(second , greatest)


# n=int(input("number"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# print(count)
# if count==2:
#     print("prime")
# else:
#     print("not prime")

# a=[1,2,2,2,4,5,6,7,8]
# count=0
# for i in range(len(a)):
#     if a[i]==2:
#         count+=1
# print(count)

# a=[2,4,2,6,2,8]
# count=0
# for i in range(len(a)):
#     if a[i]==2:
#         count+=1
# print(count)


# a=[1,2,3,4,4,5,6,6,6]
# count=0
# for i in range(len(a)):
#     if a[i]==2:
#         count+=1
# print(count)

# a=[1,2,3,4,5]
# greatest=a[0]
# second=a[0]

# for i in a:
#     if i>greatest:
#         second=greatest
#         greatest=i
#     elif i>second:
#         second=i
# print(second)

# a=[1,2,3,4,5,6,7,8,9,10]
# g=a[0]
# s=a[0]
# for i in a:
#     if i>g:
#         s=g
#         g=i
#     elif i>s:
#         s=i
# print(s)


# a=[1234567,123456,12345,123,1234]
# g=a[0]
# s=a[0]
# for i in a:
#     if i>g:
#         s=g
#         g=i
#     elif i>s:
#         s=i
# print(s)

# a=[123,1234,12345,123456]
# g=a[0]
# s=a[0]
# for i in a:
#     if i>g:
#         s=g
#         g=i
#     elif i>s:
#         s=i
# print(s)

# a=[12,32,134,544,345,63,36,789,58,5,78,9]
# g=a[0]
# s=a[0]
# for i in a:
#     if i>g:
#         s=g
#         g=i
#     elif i>s:
#         s=i
# print(s)



# a=[1,2,3,4,3,3,3,3,3,3,3,2,2,2,2,2]
# g=a[0]
# s=a[0]
# for i in a:
#     if i>g:
#         s=g
#         g=i
#     elif i>s:
#         s=i
# print(s)

# a=[1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,45,6,7,33,3,33,33,33,33]
# count=0
# for i in range(len(a)):
#     if a[i]==2:
#         count+=1
# print(count)

# n=int(input("number"))
# count=0
# # for i in range(1,n+1):
# a=[1,2,3,4,4,4,4,2,2,2]
# n=int(input("number"))
# count=0
# for i in range(len(a)):
#     if a[i]==n:
#         count+=1
# print(count)

# a=[10,20,30,40,50,60]


# for i in range(len(a)):
#     if i%2==0:
#          print(a[i])

# a=[10,20,30,40,50,60]
# even=a[0]
# for i in range(len(a)):
#     if a[i]%2==0:
#         print(a[i])        

# a=[10,20,30,40,50,60,70]
# for i in range(len(a)):
#     if i%2==0:
#         print(a[i])

# a=[10,-5,20,-8,7]

# for i in range(len(a)):
#     if a[i]<0:
#         a[i]=0
# print(a)

# a=[12,34,-3,4,-4,56,-4,5,-78,-89]
# for i in range(len(a)):
#     if a[i]<0:
#         a[i]=0
# print(a)

# a=[1,2,3,4,-5,-7,-5,-7]
# for i in range(len(a)):
#     if a[i]<0:
#         a[i]=0
# print(a)


# a=[1,2,3,4,-5,-7,-5,-7]
# for i in range(len(a)):
#     if a[i]<0:
#         a[i]=0
# print(a)


# a=[10,20,30,40]
# sum=0
# for i in a:
#     sum+=i
# print(sum)

# a=[10,20,30,40]
# n=len(a)
# mid=n//2
# for i in range(mid):
#     a[i],a[n-i-1]=a[n-i-1],a[i]
# print(a)

# a=[10,20,30,40,50]
# n=len(a)
# mid=n//2
# for i in range(mid):
# #     a[i],a[n-1-i]=a[n-1-i],a[i]
# # print(a)
# rev=""
# for i in :
#         rev=i+rev

# a=[1,2,3,4,5,6]
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# a=[1,2,3,4,5,6]
# even=[]
# odd=[]

# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


# a=[1,23,4,4,5,6,6,5,4,43,4,5,6]
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# n=[2,3,4,5]
# multiply=1
# for i in n:
#     multiply=multiply*i
# print(multiply)

# n=[10,25,15,40,30]
# count=0
# for i in n:
#     if i>20:
#         count+=1
# print(count)

# a=[10,25,15,40,30]
# n=int(input("number"))
# count=0
# for i in a:
#     if i<n:
#         count+=1
# print(count)

# n=[1,2,3] 
# m=[4,5,6]

# for i in m:
#     n.append(i)
# print(n)

# a=[15,5,20,8,12]
# smallest=a[0]
# second=a[0]
# for i in a:
#     if i<smallest:
#         second=smallest
#         smallest=i
#     elif i<second:
#         second=i
# print(second)

# a=[10,20,30,40,50]
# n=len(a)
# mid=n//2
# for i in range(mid-1):
#         a[i],a[n-1-i]=a[n-1-i],a[i]
# print(a)
    
# a=[10,20,30,40,50]
# index=a[0]
# for i in range(len(a)):
#     if a[i]==30:
#         index=i
# print(index)

# n=[1,2,3,2,4,1,5]

# n.remove(n[3])
# n.remove(n[5])
    
# print(n)


# a=[1,2,3,2,4,1,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


#average 

# n=[10,20,30,40,50]
# sum=0
# count=0
# for i in n:
#     sum+=1
# if sum>0:
    

# sum=0
# count=int(input("input"))
# for i in range(count):
#     a=int(input("enter number"))
#     sum+=a
# if count>0:
#     avg=sum/count
# # # #     print(avg)
# a=[10,23,45,35,67,78,78,46,36,78]
# def second_largest(a):
#     greatest=0
#     second=0
#     for i in a:
#         if i>greatest:
#             greatest=i
    
#     a.remove(greatest)
#     while greatest in a:
#          a.remove(greatest)
#     greatest=0
#     second=0
#     for i in a:
#             if i>greatest:
#                 greatest=i
#     print(greatest)

# second_largest(a)
    

# a=[1,2,2,2,3,3,4,4,4,5,5,5,5]
# def occurence(a):
#     count1=0
#     for i in a:
#         if i==1:
#             count1+=1
#     print(f"1 - {count1}")
#     a=[1,2,2,2,3,3,4,4,4,5,5,5,5]
#     count2=0
#     for i in a:
#         if i==2:
#             count2+=1
#     print(f"2 - {count2}")
#     a=[1,2,2,2,3,3,4,4,4,5,5,5,5]
#     count3=0
#     for i in a:
#         if i==3:
#             count3+=1
#     print(f"3 - {count3}")
#     a=[1,2,2,2,3,3,4,4,4,5,5,5,5]
#     count4=0
#     for i in a:
#         if i==4:
#             count4+=1
#     print(f"4 - {count4}")
#     a=[1,2,2,2,3,3,4,4,4,5,5,5,5]
#     count5=0
#     for i in a:
#         if i==5:
#             count5+=1
#     print(f"5 - {count5}")

# # occurence(a)
# n=int(input("enter your number:"))
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
# #     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()

