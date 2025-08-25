print("hello")
a="Dnyaneshwari"
b="Varal"
c="Java"
print(a,b,c,end='/t',sep="*")
print(a,b,c,end="\t")
print()

#integer
num1=10
num2=20
sum=num1+num2
res="Addition of %d and %d=%d"%(num1,num2,sum)
print(res)
#print("Addition of %d and %d is",(num1,num2,sum))



#String
str1="Guido"
design="introduce python"
year=1990

res1="%s was  %s  in %s"%(str1,design,year)
print(res1)


num3=40
num4=30

res="value for 1st variable is %d and second variable is %d"%(num3,num4)
print(res)
#using concatination
print("using concatination")
print("value of 1st variable is: "+str(num3)+"value of 1st variable is: "+str(num4))

#using positional parameters
print("using positional parameters")
print("value of 1st variable is: {} value of 2nd variable is: {}".format(num3,num4))


#using Index Parameter
print("using Index Parameter")
print("value of 1st variable is: {0} value of 2nd variable is: {1} again value of 1st variable is: {0}".format(num3,num4))


'''Assignment on print
student id
student name
cource
cource fees
start date
'''
studId=120
studName="Dnyaneshwari"
cource="java fullstack"
start_date=1
res="student id is %d student name is %s student cource is %s Start date is %d"%(studId,studName,cource,start_date)
print(res)

print("student id is "+str(studId)+ "Student name is "+studName +"cource name is "+cource +"Start date is "+str(start_date))

print("student id is {} Student name is {} cource name is {} Start date is {}".format(studId,studName,cource,start_date))

print("student id is {0} Student name is {1} cource name is {2} Start date is {3} again Student name is {0} ".format(studId,studName,cource,start_date))

print()

#take input from user
a=input("Enter Name ")
print(a)

b=int(input("enter num1 "))
c=int(input("enter num2 "))
res=b+c
print(res)

#Assignment 2

a=input("enter your name ")
b=int(input("enter your age "))
c=float(input("enter balance in ur acc "))
d=bool(input("information is: "))

print(a)
print(b)
print(c)
print(d)


#Assignment 3

'''Assignment on input take input from user
student id
student name
cource
cource fees
start date
'''

StudId=int(input("Enter student Id "))
StudName=input("Enter student Name ")
courceName=input("Enter student cource name ")
Fees=int(input("Enter student cource fees "))
StartDate=int(input("Enter start date "))
print("Student id is {} Name of student is {} Cource name is {} Fees of cource is {} Start date is{} ".format(StudId,StudName,courceName,Fees,StartDate))


