import os
import shutil

username=input("Please enter your username: ")
os.chdir("C:\\Users\\%s\Downloads\\" % (username,))
print(os.getcwd())
files = os.listdir()
for filename in files:
    name, ext = os.path.splitext(filename)
    if ext == ".jpg":
        img_dl = "C:\\Users\\%s\Downloads\\Images" %(username,)
        shutil.move(name + ext, img_dl)
    elif ext == ".zip":
        zip_dl = "C:\\Users\\%s\\Downloads\\Zips" %(username,)
        shutil.move(name + ext, zip_dl)
    elif ext == ".exe":
        os.listdir("C:\\Users\\%s\\Downloads\\Exes" %(username,))
        exe_dl = "C:\\Users\\%s\\Downloads\\Exes" %(username,)
        shutil.move(name + ext, exe_dl)
