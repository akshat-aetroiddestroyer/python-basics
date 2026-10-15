#write a python programe to simulate an atm machine

'''rules:
1. pin verification:
       - default pin is 1234
       - user gets a maximum of 3 attempts to enter correct pin
       - if pin entered incorrectly for 3 times print card blocked please contact your bank
2. main menu (runs continuesly until user exists):
    option 1: display the current balance
    option 2: ask for deposit amount and add to the balance and and display upated balance
    option 3: ask for withdraw amount and check if amount<=balance then deduct amount from balance and print withrawl succesful
       otherwise print (insufficient balance!)
    option 4: print thanku for using oue atm have a nice day and exit the loop
#          --any other option print invalid choice! please choose 1-4    '''

# atempts=3                                                                #logic for pin attempt and main menu access
# has_access_mainmenu=False
# while atempts>0:
#     entered_pin=int(input("enter pin: "))
#     if entered_pin==1234:
#         has_access_mainmenu=True
#         break
#     else:
#         atempts-=1
#         if atempts>0:
#             print(f"incorrect pin! you have {atempts} remaining")
#         else:
#             print("card block contact to your bank :)")
# balance=50000                                                           #logic for main menu operations
# if has_access_mainmenu==True:
#     while True:
#         print("ATM MENU")
#         print("1 -> check balance")
#         print("2 -> deposit cash")
#         print("3 -> withdraw cash")
#         print("4 -> exit")

#         choice=int(input("enter the choice"))
#         if choice==1:                                                                       #logic for 1
#             print(f"your balance is {balance}")
#         elif choice==2:                                                                      #logic for 2
#             deposit_amount=int(input("enter the amount to deposite"))
#             if deposit_amount>0:
#                 balance+=deposit_amount
#                 print(f"deposite succesful!! your current balance is: {balance}")
#             else:
#                 print("entered amount is not valid")
#         elif choice==3:                                                                          #logic for 3
#             withdraw_amount=int(input("enter the amount to withdraw: "))
#             if withdraw_amount>0:
#                 balance-=withdraw_amount
#                 print(f"withdrawl succesful!! your current balance is: {balance}")
#             else:
#                 print("INSUFFICIENT BALANCE :( ")
#         elif choice==4:                                                                             #logic for 4
#             print("thank you for visting our ATM! please visit again :)")
#             break
#         else:
#             print("invalid choice! please choose between 1-4")


# #reverse a list using two pointer approach

# arr=[10,20,30,40,50]
# n=len(arr)
# mid=n//2
# for i in range(mid):
#     arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
# print(arr)


# a=[10,20,30,40,50,60]
# n=len(a)
# mid=n//2
# for i in range(mid):
#     a[i],a[n-i-1]=a[n-i-1],a[i]
# print(a)    

# a=[10,20,30,40,50,60]
# n=len(a)
# mid=n//2
# for i in range(mid):
#     a[i],a[n-i-1]=a[n-i-1],a[i]
# print(a)

# a=[1,2,3,5,6,7,9,0,23]
# n=len(a)
# mid=n//2
# for i in range(mid):
#     a[i],a[n-i-1]=a[n-i-1],a[i]
# print(a)

#print positive and negative element seperately

# a=[1,2,-2,-3,-4,-5,4,5,3,2,5]
# print("positive")

# for i in a:
    
#     if i>0:
#         print(i)
# print("negative")
# for i in a:
#     if i<0:
#         print(i)

# a=[1,2,3,4,5,-1,-2,-3,-4,-5]
# print('postive' , end=" ")
# for i in a:
#     if i>0:
#         print(i , end=" ")
# print()
# print("negative" , end=" ")
# for i in a:
#     if i<0:
#         print(i , end=" ")

#find a mising number in a list
# a=[1,2,3,5,6]
# n=len(a)+1
# expexted=n*(n+1)//2

# sum=0
# for i in a:
#     sum+=i
# missing=expexted-sum
# print(missing)

# #pattern printing n=5
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# n=5
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

 