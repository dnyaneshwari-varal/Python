product=("TV", "Phone", "machine")
num=1
for j in product:
    print("{} . {}".format(num,j))
    num +=1
    

student=(("Dnyaneshwari",201,"java fsd",60000),("Aditi",202,"java SPIC",85000),("Aditya",203,"java SPIC",85000),("Roshni",204,"Data Analyst",60000))
ser_no=1
for i in student:
    print("Student {}. {}".format(ser_no,i))
    ser_no +=1


#Tuple Packing
#unpacking
tup=12,"Varal"
print(type(tup))
print(tup)
roll_no,name =tup
print(roll_no)
print(name)
name ="dnyaneshwari"
print(tup)

#we have tuple size 4 then for unpacking we need to give 4 variable to unpacking it
#but you want only print 2 varialble then you can use * so other element store in that[] list

#example
tup=1,"Dnyana",34,789,"Varal"
a,b,*c=tup
print(tup)
print(a,b,c)
