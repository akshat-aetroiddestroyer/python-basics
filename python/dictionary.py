'''1. dictionary is anoted by  {}
   2. dictionary are combination of multiple keys:values
   3. dictinary are mutable
   4. multiple data type(hetrogenous)
   5. keys will be unique
   6. dictionary are ordered'''


# d = {1:"hello"}
# print(type(d))

# d={10:100,20:200,30:300,40:400}
# d[50]=100  #creating a new key:value pair which never exist before
# d[10]=110  #update 
# del d[20]   #delete
# print(d)

# d={10:100,20:200,30:300,40:400}      #traversing the dictinary only keys(loop)

# for i in d:
#     print(i)

# d={10:100,20:200,30:300,40:400}       #traversing the dictinary only values(loop)
# for i in d:
#     print(d[i])

# d={10:100,20:200,30:300,40:400}       #traversing the dictinary only values(loop)
# for i in d.values():
#     print(i)

# help(dict)

# d.clear()
# d.copy()

# a=[1,2,3,4,5,6]          #this is known as deep copy (b ke andar change krne se a bhi change ho jata h)
# b=a
# b[0]=100
# print(a)

# a=[1,2,3,4,5,6]          #this is known as shallow copy (b k andar change krne se a change nhi hoga by using copy())
# b=a.copy()
# b[0]=100
# print(a)


# a={'name':'akshat','age':'21','city':'bhopal'}
# print(a['name'])

# a={'name':'akshat','age':'21','city':'bhopal'}
# print(a , a['name'])

# a={'name':'akshat','city':'bhopal','age':'22'}
# print(a,a['age'])

# a={'name':'akshat','age':22,'city':'bhopal'}
# print(a['name'] , a['city'] , a['age'])

# a={'name':'akshat','age':22,'city':'bhopal'}
# a['course']='python'
# print(a)

# a={'name':'akshat','age':'21'}
# a['age']=20
# print(a)

# a={'name':'akshat','age':22,'city':'bhopal'}
# del a['city']
# print(a)

# a={'name':'akshat','age':22,'city':'bhopal'}
# if 'age' in a:
#     print("key exist")
# else:
#     print("KEY not exist")

# a={'name':'akshat','age':21,'city':'bhopal'}
# for i in a:
#     print(i)


# a={'name':'akshat','age':22,'city':'bhopal'}
# for i in a:
#     print(a[i])

# a={'a':10,'b':20,'c':30}
# count=0
# for i in a:
#     count+=1
# print(count)
    
# a={1:10,2:20,3:30}
# sum=0
# for i in a:
#     sum+=a[i]
# print(sum)

# help(dict)     #methods of dictionary

# a={1:10,2:20,3:30}
# a.clear()
#a.keys()       #by this method we get only keys
#a.values       #by this method we get only values
# a.copy
# a=[1,2,3,4,5,6]          #this is known as deep copy (b ke andar change krne se a bhi change ho jata h)
# b=a
# b[0]=100
# print(a)

# a=[1,2,3,4,5,6]          #this is known as shallow copy (b k andar change krne se a change nhi hoga by using copy())
# b=a.copy()
# b[0]=100
# print(a)

# a={1:10,2:20,3:30}         #by get method we can store specific key:value in another variable

# b=a.get(3)
# print(a.get(1))       #can also print value and if the key not exist so it will print none

# print(b)

# a={1:10,2:20,3:30}         #items method print key:values in a pair
# print(a.items())

# a={1:10,2:20,3:30} 
# a.update(a[3:40])
# print(a)

# a={1:10,2:20,3:30}        #remove specified key and return the corresponding value
# a.pop(3)
# print(a)
# a={1:10,2:20,3:30}
# a.popitem(a)
# print(a) 
#a.upate(n)         #you can update a dictionary by adding another dictionary to it

# a={1:10,2:20,3:30} 
# b={4:40,5:50,6:60} 
# for i in b:
#     a[i]=b[i]
# print(a) 

# a={1:70,2:33,3:12}
# sum=0
# for i in a:
#     sum+=a[i]
# print(sum) 

# a=[1,2,3,4,5,6,6,6,6,6,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5]     #frequency of each element by using dictionaries

# d = {}
# for i in a:
#    if i in d.keys():
#         d[i] +=1
#    else:
#        d[i]=1
# print(d)


# a=[1,2,3,4,5,6,6,6,6,6,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5]
# d={}
# for i in a:
#    if a[i] in d.keys():
#         d[i]+=1
#    else:
#        d[i]=1
# print(d)

# a=[1,2,3,4,5,6,6,6,6,6,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5]
# d={}
# for i in a:
#    if a[i] in d.keys():
#       d[i]+=1
#    else:
#       d[i]=1
# print(d)



# a=[1,2,3,4,5,6,6,6,6,6,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5]
# d={}
# for i in a:
#    if a[i] in d.keys():
#       d[i]+=1
#    else:
#       d[i]=1
# print(d)   


# a=[1,2,3,4,5,6,6,6,6,6,1,1,1,2,2,2,2,3,3,3,4,4,5,5]
# d={}
# for i in a:
#     if a[i] in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# n=10
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c


# a={1:10,2:20,3:30} 
# b={4:40,5:50,6:60} 
# for i in b:
#     if i in a.keys():
#         a[i]+=1
#     else:
#         a[i]=b[i]

        
    
# print(a)

# d={1:1,2:1,3:1}
# for i in d:
#     print(i)

# a={1:70,2:88,3:12}
# for i in a:
#     if a[i]>50:
#         print(i)

# a={1:70,2:33,1:100}
# greatest=0
# for i in a:
#     if i>greatest:
#         greatest=i
# print(greatest)
    

# a={'abab':70,'vikas':33,'akshat':12}
# top=0
# highest=70
# for name, marks in a.items():
#     if marks>highest:
#         highest=marks
#         top=name
# print(top , highest)


# # a={1:70,2:33,3:12}
# # add=5
# # print(a[1]+5 , a[2]+5 , a[3]+5)
    
# # a={1:70,2:33,3:12}
# # for i in a:
# #     a[i]=a[i]+5
# # print(a)

# a={'n':70,'a':33,'ak':100}
# greatest=0
# greatest_key=""
# for i in a:
#     if a[i]>greatest:
#         greatest=a[i]
#         greatest_key=i
        
# print(greatest_key,greatest)

# a[i]-60 , a ,ak
#  60>greatest

# a={'n':70,'a':33,'ak':100}
# smallest=100

# for i in a:
#     if a[i]<smallest:
#         smallest=a[i]
# print(smallest)


# a={'n':70,'a':33,'ak':100}

# greatest=0

# for i in a:
    
#       if a[i]>greatest:
#         greatest=a[i] 

# smallest=greatest
# for i in a:
#     if a[i]<smallest:
#         smallest=a[i]
    
# print(smallest)

# a={'n':70,'a':33,'ak':100}
# greatest=0
# for i in a:
#     if a[i]>greatest:
#         greatest=a[i]
# smallest=greatest
# smallest_key=""
# for i in a:
#     if a[i]<smallest:
#         smallest=a[i]
#         smallest_key=i
# print(smallest_key , smallest)
      
# a={'n':70,'a':33,'ak':100}
# greatest=0
# for i in a:
#     if a[i]>greatest:
#         greatest=a[i]
# smallest=greatest
# smallest_key=''
# for i in a:
#     if a[i]<smallest:
#         smallest=a[i]
#         smallest_key=i
# print(f"the smallest key is {smallest_key} and the value is {smallest}")
        
# a={'n':70,'a':33,'ak':100}
# greatest=0
# for i in a:
#     if a[i]>greatest:
#         greatest=a[i]
# smallest=greatest
# for i in a:
#     if a[i]<smallest:
#      smallest=a[i]
# print(smallest)

# a={'n':10,'a':15,'ak':20,'aa':7}
# even=0
# odd=0
# for i in a:
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"even: {even}")
# print(f"odd: {odd}")

# a={'n':10,'a':15,'ak':20,'aa':7}
# even=0
# odd=0
# for i in a:
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even,odd)

# a={'n':10,'a':15,'ak':20,'aa':7}
# even=0
# odd=0
# for i in a:
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even,odd)
# a={'n':10,'a':15,'ak':20,'aa':7}
# even=0
# odd=0
# for i in a:
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even,odd)

# a={'n':10,'a':15,'ak':20,'aa':7}
# even=0
# odd=0
# for i in a:
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even,odd)

# a={'n':10,'a':15,'ak':20,'aa':7}
# even=0
# odd=0
# for i in a:
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even,odd)

# a={'n':10,'a':15,'ak':20,'aa':7}
# even=0
# odd=0
# for i in a:
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even,odd)


# a={'n':10,'a':15,'ak':20,'aa':7}
# even=0
# odd=0
# for i in a:
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd=+1
# print(even,odd)

# a={'n':10,'a':15,'ak':20,'aa':7}
# sum=0
# for i in a:
#     if a[i]%2==0:
#         sum+=a[i]
# print(sum)

# a={'n':10,'a':15,'ak':20,'aa':7}
# sum=0
# for i in a:
#     if a[i]%2==0:
#         sum+=a[i]
# print(sum)

# a={'n':10,'a':15,'ak':20,'aa':7}
# sum=0
# for i in a:
#     if a[i]%2==0:
#         sum+=a[i]
# print(sum)

# a={'n':10,'a':15,'ak':20,'aa':7}
# sum=0
# for i in a:
#     if a[i]%2==0:
#         sum+=a[i]
# print(sum)

# a={'n':10,'a':15,'ak':20,'aa':7}
# sum=0
# for i in a:
#     if a[i]%2==0:
#         sum+=a[i]
# print(sum)

# a={'n':10,'a':15,'ak':20,'aa':7}
# sum=0
# for i in a:
#     if a[i]%2==0:
#         sum+=a[i]
# print(sum)

# a={'n':10,'a':15,'ak':20,'aa':7}
# sum=0
# for i in a:
#     if a[i]%2==0:
#         sum+=a[i]
# print(sum)

# a={'a':10,'b':20,'c':30}
# value=20
# for i in a:
#     if a[i]==value:
#         print(i)

# a={'a':10,'b':20,'c':30}
# for i in a:
#     if a[i]==20:
#         print(i)

# a={'a':10,'b':20,'c':30}
# for i in a:
#     if a[i]==20:
#         print(i)

# a={'a':10,'b':20,'c':30}
# b={'a':15,'b':25,'c':35}
# a.update(b) 
# print(a)

# a={'a':10,'b':20,'c':30}
# for i in a:
#     a[i]=a[i]+5
# print(a)

# a={'a':10,'b':25,'c':15,'d':40}
# count=0
# for i in a:
#     if a[i]>20:
#         count+=1
# print(count)

# a={'a':10,'b':25,'c':15,'d':40}
# count=0
# n=int(input("number"))
# for i in a:
#     if a[i]>n:
#         count+=1
# print(count)

# a={'a':10,'b':25,'c':15,'d':40}
# count=0
# for i in a:
#     if a[i]>20:
#         count+=1
# print(count)

# a={'a':10,'b':25,'c':15,'d':40}
# count=0
# for i in a:
#     if a[i]>20:
#         count+=1
# print(count)

# keys= ['a','b','c']
# values= [10,20,30]

# d=dict(zip(keys, values))
# print(d)

# keys= ['a','b','c']
# values= [10,20,30]
# d={}
# for i in range(len(keys)):
#     d[keys[i]]=values[i]
# print(d)

# keys= ['a','b','c']
# values= [10,20,30]
# d={}
# for i in range(len(keys)):
#     d[keys[i]]=values[i]
# print(d)

# keys= ['a','b','c']
# values= [10,20,30]
# d={}
# for i in range(len(keys)):
#     d[keys[i]]=values[i]
# print(d)

# keys= ['a','b','c']
# values= [10,20,30]
# d={}
# for i in range(len(keys)):
#     d[keys[i]]=values[i]
# print(d)

# keys= ['a','b','c']
# values= [10,20,30]
# d={}
# d['a']=10
# d['b']=20
# d['c']=30
# print(d)

# a={'a':10,'b':20,'c':10,'d':40}
# count=0
# for i in a:
#     if a[i]==10:
#         count+=1
# print(count)

# a=[1,2,3,4,5,6,6,6,6,6,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5]
# d={}
# for i in a:
#    if a[i] in d.keys():
#         d[i]+=1
#    else:
#        d[i]=1
# print(d)

# a={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# positive=0
# print("positive")
# for i in a:
#     if a[i]>0:
#         positive+=1
# print(positive)
# negative=0
# print("negative")
# for i in a:
#     if a[i]<0:
#         negative+=1
# print(negative)

# a={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# postive=0
# print("positive")
# for i in a:
#     if a[i]>0:
#         postive+=1
# print(postive)
# negative=0
# print("negative")
# for i in a:
#     if a[i]<0:
#         negative+=1
# print(negative)


# a={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# postive=0
# print("positive")
# for i in a:
#     if a[i]>0:
#         postive+=1
# print(postive)
# negative=0
# print("negative")
# for i in a:
#     if a[i]<0:
#         negative+=1
# print(negative)

# a={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# positive=0
# print("positive")
# for i in a:
#     if a[i]>0:
#         positive+=1
# print(positive)
# negative=0
# print('negative')
# for i in a:
#     if a[i]<0:
#         negative+=1
# print(negative)

# a=[1,2,3,4,5]
# k=2
# k=k%len(a)
# for i in range(k):
#     last=a.pop()
#     a.insert(0 , last)
# print(a)

# a=[1,2,3,4,5]
# greatest=0
# for i in a:
#     if i>greatest:
#         greatest=i
# print(a.index(greatest), greatest)
# a={'a':10,'b':25,'c':15,'d':40}
# count=0
# for i in a:
#     if a[i]>20:
#         count+=1
# print(count)

# keys=['a','b','c']
# values=[10,20,30]
# d={}
# for i in range(len(keys)):
#     d[keys[i]]=values[i]
# print(d)

# a=[1,2,3,4,5]
# greatest=0
# second_greatest=0
# for i in a:
#     if i>greatest:
#         second_greatest=greatest
#         greatest=i
#     elif i>second_greatest:
#         second_greatest=i
# print(second_greatest)

# a=[1,2,3,4,5,6]
# def second(a):
#     greatest=0
#     for i in a:
#         if i>greatest:
#             greatest=i
#     a.remove(greatest)
#     second_greatest=0
#     for i in a:
#         if i>second_greatest:
#             second_greatest=i
#     print(second_greatest)
# second(a)

# a=[1,2,3,4,5,6,6,6,6,6,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5]                                                                          

# d={}
# for i in a:
#    if i in d.keys():
#         d[i] +=1
#    else:
#        d[i]=1
# print(d)