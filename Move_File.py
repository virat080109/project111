import os
import shutil

path=input("Enter Path: ")
files= os.listdir(path)
print(files)
for file in files:
    filename,extension=os.path.splittext(file)
    extension=extension[1:]

    if os.path.exists(path+'/'+extension+'/'+file)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)    