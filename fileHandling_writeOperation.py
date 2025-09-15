'''
#code1
try:
    choice='y'
    file1=open("Demo2.txt","w")
    while choice == 'y':
        data=input("Enter data: ")
        data=data+"\n"
        #bdata=data.encode()
        file1.write(data)
        #file1.write("\n")
        choice=input("wish to add more data: ")
    file1.close()
except Exception as e:
    print("Some Error: ",e)

#code2
#writting Binary file
try:
    choice='y'
    file1=open("Demo2.txt","wb")
    while choice == 'y':
        data=input("Enter data: ")
        data=data+"\n"
        bdata=data.encode()
        print(bdata)
        file1.write(bdata)
        #file1.write("\n")
        choice=input("wish to add more data:(y/n) ")
    file1.close()
except Exception as e:
    print("Some Error: ",e)

'''
#code3
try:
    file1=open("Demo2.txt","r")
    file1.seek(4)
    data=file1.read()
    print(data)
    file1.close()
except Exception as e:
    print("Some Error: ",e)


