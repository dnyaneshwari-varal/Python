
import os
'''fnn="abc.txt"
try:
    if os.path.exists(fnn):
        os.remove(fnn)
        print("File deleted")
except FileNotFoundError as e:
    print(e)

#rename
try:
    os.rename("abc.txt","new_file,txt")
    print("rename succesfully!!")
except FileNotFoundError as e:
    print(e)



#que1

#creat python_Assignment folder

#create main folder
os.mkdir(r"G:\SeedIfotech\Python_module2\Python_Assignment")

# go inside that folder
os.chdir(r"G:\SeedIfotech\Python_module2\Python_Assignment")

os.mkdir("Data")
os.mkdir("Backup")
print("Current working directory:", os.getcwd())
print("Folders created successfully!")
'''
#que2

#creat 5 empty files data1.txt to data2.txt

#file_path = r"G:\SeedIfotech\Python_module2\Python_Assignment\data1.txt"
print(os.getcwd())
os.chdir(r"G:\SeedIfotech\Python_module2\Python_Assignment")

f1=open("data1.txt", "w")
f1.close()
f2=open("data2.txt", "w")
f2.close()
f3=open("data3.txt", "w")
f3.close()
f4=open("data4.txt", "w")
f4.close()
f5=open("data5.txt", "w")
f5.close()

for file in os.listdir(r"G:\SeedIfotech\Python_module2\Python_Assignment"):
    if file.endswith(".txt"):
        print(file)






























    
