import os
import shutil

path = input("enter the name of the directory to be sorted :- ")


list_of_files = os.listdir(path)


for file in list_of_files:
    name, ext = os.path.splitext(file)

    
    ext = ext[1:]

    
    if ext == '':
        continue

    #will move the file to the directory
   
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    #will create a new directory,
    
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)