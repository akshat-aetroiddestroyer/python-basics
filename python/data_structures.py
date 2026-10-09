# list = [12,23,45,67,True,print()]   #list can store any datatype

# print(list[1])   #list indexing
# print(list[0:5])  #list slicing


# #transversing a list with loop

# a=[12,34,56,12.3]

# for i in range(len(a)):  #using index
#     print(a[i])

# for i in a:              #directly on values
#     print(i)


# print(dir(list))   #directory of mehtods in list


# help(list)         print this you will get all use cases of methods


# a = [1,2,3,4,5]   #with this method append we can assign any datatype in the end

# a.append(6)
# a.append(7)
# a.append(8)

# print(a)


# a=[1,3,4,5,6]   #insert method will assign the datatype with the help of index

# a.insert(1,2)

# print(a)

# a=[1,2,3,4,5]        # by extend method you can insert multiple datatype at the end 

# a.extend([6,7,8])

# print(a)

# a=[1,2,3,4,5,2]     #remove method will remove the first ocurrence of the entred datatype

# a.remove(2)

# print(a)

 
# a=[1,2,3,4,5,6]        #by pop method you can remove datatype from the list and can store it to another variable

# popped_item=a.pop(3)

# print(a)
# print(popped_item)

# a=[1,2,3,4,5]        #index method will find you the index of the data

# index = a.index(4)

# print(index)

# a=[1,2,3,4,5,5,5,6,7]        #count method will tell you the occurence of the entred data

# count=a.count(5)

# print(count)

# a=[6,5,4,3,2,1]        #it will sort the given list in ascending order

# a.sort()

# print(a)

# a=[1,2,3,4,5,6,7]          #reverse method will the reverse the list

# a.reverse()

# print(a)


# a=[1,2,3,4,5,6]     #creates a copy of list in a new variable

# new=a.copy()

# print(new)

# a=[1,2,3,4,5]      # removes all elements in a list

# a.clear()

# print(a)

# a=[1,2,-1,-3,2,-4,7,-5]                  #printing positive and negative numbers
# print("positive elements are ")
# for i in a:
#     if i>=0:
#         print(i)
# print("negative numbers are ") 
# for i in a:
#     if i<0:
#         print(i)


# a=[1,2,3,4,5,6]    #find avg of a list
# sum=0
# for i in a:  
#     sum=sum+i
# print(sum/len(a))


# a=[1,2,3,4,5,6,7]                 # printing the greatest element in a list and it's index
# graetest=a[0]

# for i in range(len(a)):
#     if a[i]>graetest:
#         graetest=a[i]
# print(f"greates value in a list is: {graetest}")
# index=a.index(graetest)
# print(f"the index of a greatest value is: {index} ")
    
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

# a=[67,56,834,45689,7543,5,7678]
# a.sort()

















