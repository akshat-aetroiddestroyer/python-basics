# a=[1,2,3,4,5,6,7,8]
# opetaions=0
# while len(a)>1:
#     new=[]
#     opetaions+=1
#     for i in range(len(a)//2):
#         c=2*i
#         b=2*i+1
#         if len(new)%2==0:
#             new.append(min(a[c],a[b]))
#         else:
#             new.append(max(a[c],a[b]))
#     a=new
# print(new , opetaions)
# n=[1,2,3,4,5,6,7,8]
# while len(n)>1:
#     new=[]
#     for i in range(len(n)//2):
#         a=2*i
#         b=2*i+1
#         if len(new)%2==0:
#             new.append(min(n[a],n[b]))
#         else:
#             new.append(max(n[a],n[b]))
#     n=new
# print(new)

# a=[1,5,0,3,5]
# b=[]
# n=len(a)
# for i in range(n):
#     count=0
#     unique=0
#     for j in range(n):
#         if a[i]!=a[j]:
#             unique+=1
#         if a[i]==a[j]:
#             count+=1
#     if count==1:
#         b.append(a[i])
# print(unique)
# a=[1,5,0,3,5]
# b=[]
# for i in a:
#     if  i not in b and i!=0:
#         b.append(i)
# print(len(b))
    

# nums = [1, 5, 0, 3, 5]
# unique = []

# for i in nums:
#     if i not in unique and i != 0:
#         unique.append(i)

# print(len(unique))