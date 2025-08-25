#code1
print("code1")
datalst=["Seed","Infotech","Pune"]
for ch in datalst:
    print("length of {} is {}".format(ch,len(ch)))



#code2
print('\n')
print("code2")
tup=(1,2,3,4)
for temp in tup:
    sqr=temp**2 #aqr=temp*temp
    print("square of {} is {} ".format(temp,sqr))



#code3
print('\n')
print("code3")
lst=(1,2,3,4)
for ls in lst:
    cube=ls**3 #aqr=ls*ls*ls
    print("cube of {} is {} ".format(ls,cube))

#code4
print('\n')
print("code4")
str1="Dnyaneshwari varal"
for i in str1:
   #print(i,end='\t')
   print(i)

#Assignment1
print('\n')
print("Assignment1: ")
for i in range(40,19,-1):
    if(i%2==0):
        sqr=i*i
        print("Square of ",i ,"is ",sqr)



#Assignment2
print('\n')
print("Assignment1: ")
tupl=(10,20,30,40,50)
count=0
for i in tupl:
   print("Element in tuple: ",i)
   count=count+1

print("Element present in tuple: ",count)


#Assignment3
print('\n')
print("Assignment3: ")
list=["sakshi","sam","Ram"]
num=1
for i in list:
    print(num,i)
    num+=1

#Assignment4
print('\n')
print("Assignment4: ")
table=int(input("Enter which table you want to print: "))

for i in range(1,11):
          print(table,"*",i,"=",table*i)


#Assignment5
print('\n')
print("Assignment5: ")
for i in range(1,6):
  num=int(input("Enter Number: "))
  if(num%2==0):
      sqr=num*num
      print(num, " is even so square of", num ,"is: ",sqr)
  else:
      cube1=num*num*num
      print(num, " is odd so cube of", num," is: ",sqr)






          
