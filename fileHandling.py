#code1   read data

'''
try:
    file1=open("G:\\SeedIfotech\\Python_module2\\Demo.txt","r")
    data=file1.read()
    print(type(file1))
    print(data)
    file1.close()
except:
    print("Some error in above code")

print("Hope u enjoy 1st Demo of file handling!!!")
print("Hope u enjoy 1st Demo of file handling!!!")
print("__***__")


#code 2  add data at end of file
data="Name: Dnyaneshwari, Address:Chinchvad, city:Pune"
try:
    file1=open("Demo.txt","a+")
    file1.write("\n")
    file1.write(data)
    file1.close()
except:
    print("Some error in above code")


#code3
try:
    file1=open("Demo.txt","r")
    data=file1.readline()
    print(type(data)) #  <class 'str'>
    while data !='':
        print(data,end='')
        data=file1.readline()
    file1.close()
except:
    print("Some erroe in above code!")


#code4
try:
    file1=open("Demo.txt","r")
    data=file1.readlines()
    print(type(data))  #<class 'list'>
    for line in data:
        print(line)
except:
    print("Some Erroe occure")
'''




    
