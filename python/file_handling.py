'''Mkdr - create a folder
rmdir - remove the folder'''

'''FILES
x-> this mode will only create the file and if already exist we will get an error
w->agar file exist nhi kr rhi h so this mode will create one and insert the content inside the file
a
r'''

# mode 1: x- just to create file
# open('garba.txt','x')

# mode 2: w- if there is any content already so the it will rewrite it
# file=open('garba.txt','w')
# file.write('job hi job')

# mode 3: a-> add the task at the last
# file=open('garba.txt','a')
# file.write('/n lol')

# # mode 4: r-> read the content inside the file
# file=open('garba.txt','r')
# print(file.read)

# with open('sample.txt','w') as file:   #by this syntax file will automatically closed
#     file.write('this is new file')

# CRUD - create , read , update , delete
# import os
# os.remove('sample.txt')
from pathlib import Path
import os

def create_folder():
    name=input('tell your folder name:- ')
    p=Path(name)
    if p.exists():
        print('this folder name already exist please try again ')
        create_folder()
    else:
        p.mkdir()
        print('folder created successfully !')
def read_folder():
    p=Path('')
    names=list(p.rglob('*'))

    for i in range(len(names)):
        print(f'{i+1} : {names[i]}')
def update_folder():
    read_folder()
    name=input('which folder you want to update:- ')
    old_p=Path(name)

    if old_p.exists():
        new_name=input('tell folder name:- ')
        new_p=Path(new_name)
        old_p.rename(new_p)
        print('folder name changed successfully')
    else:
        print('no such folder exist please try again')
        update_folder()
def delete_folder():
    name=input('tell me folder name:- ')
    p = Path(name)

    if not p.exists():
        print('the folder name does not exist please try again:- ')
        delete_folder()
    else:
        p.rmdir()
        print('folder deleted school!')
def create_file():
    name=input('tell your file name with extension:- ')
    p=Path(name)
    if p.exists():
        print('file already exist!')
        create_file()
    else:
        with open(p,'w') as fs:
            data=input('enter what you want to write: ')
            fs.write(data)
            print('successfully created! ')
def read_file():
    name=input('tell your file name with extension:- ')
    p=Path(name)
    if p.exists() and p.is_file():
        with open(p,'r') as file:
            data=file.read()
            print('\n\n\nyour file data is\n\n\n')
            print(data)
def update_file():
    read_file()
    name=input('tell your file name with extension:- ')
    p=Path(name)
    if p.exists() and p.is_file():
        print('press 1 for changing the file name')
        print('press 2 for overwriting the data of your file')
        print('press 3 for appending some content in your file')
        res=int(input('tell me your response:- '))
        if res==1:
            name2=input('tell your new file name:- ')
            p2=Path(name2)
            p.rename(p2)
        print('file name updated succesfully')
        if res==2:
            with open(p,'w') as file:
                name2=('tell what you wanna rewrite:- ')
                file.write(data)
            print('file rewrite succesfully')
        if res==3:
            with open(p,'a') as file:
                data=input('enter what you want to append: ')
                file.write(' '+data)
            print('data appended succesfully')
    else:
        print('no such file exist!')
def delete_file():
    name=input('tell your file name with extension:- ')
    p=Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        print('file deleted succesfully')
    else:
        print('no such file exists ')
        delete_file()

print('press 1 for creating a new folder: ')
print('press 2 for reading any folder: ')
print('press 3 for updating any folder: ')
print('press 4 for deleting any folder: ')
print('press 5 for creating a new file: ')
print('press 6 for reading any file: ')
print('press 7 for updating any file: ')
print('press 8 for deleting any file: ')


res=int(input('tell your response:- '))
if res==1:
    create_folder()
if res==2:
    read_folder()
if res==3:
    update_folder()
if res==4:
    delete_folder()
if res==5:
    create_file()
if res==6:
    read_file()
if res==7:
    update_file()
if res==8:
    delete_file()
