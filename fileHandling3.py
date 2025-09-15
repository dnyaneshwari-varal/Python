'''
#code1
#w+ mode to read and write file
#open a file in w+ mode

with open("example.txt","w+") as file:
    #write some data to the file
    file.write("Writing in file\n")
    file.write("Python is versatile language!\n")
    file.write("This is file opend in w+ mode.\n")
    file.write("writing done in file!!\n")

    #move the file pointer back to the beggining of file
    file.seek(0)

    #Read the contents of the file
    content=file.read()
    print("File content after writing.")
    print(content)

'''
#code2
name="Abtony\n"
address=["224 Baker Street\n","London\n"]
try:
    with open("example.txt","a")as f:
        f.write(name)
        f.writelines(address)
except FileNotFound as e:
    print(f"Error:{e}.File not found.")
except Exception as e:
    print("An unexpected error occured:{e}")


#code3
#handling binary files
f=open('numlist.bin',"wb")
num=[5,10,15,20,25]
x=bytearray(num)
f.write(x)
f.close()

#open a binary file
f=open("numlist.bin","rb")
#read lines
data=f.read()
#dislay data
print("binary data",data)
f.close()

#output of code3= binary data b'\x05\n\x0f\x14\x19'































