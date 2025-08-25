#Arithmatic Operator
# +, -,*,/,%,//,***

a=int(input("enter value of a "))
b=int(input("enter value of b "))

print("adition of a {} and b {} is".format(a,b),a+b)
print("substraction of  {} and  {} is".format(a,b),a-b)
print("multiplication of a {} and b {} is".format(a,b),a*b)
print("division of a {} and b {} is".format(a,b),a/b)
print("%.2f"%(a/b))
print("modulus of a {} and b {} is".format(a,b),a%b)
'''
Regular division: 7 / 3 = 2.3333…
Floor division: 7 // 3 = 2'''
print("floor division of a {} and b {} is".format(a,b),a//b)
print("Exponentiation of a {} and b {} is ".format(a,b), a**b)



#Assignment operator
a=10
#print(a =+ 10 ) #we cant write like this

a+=3 #a=a+3
print(a)

a-=4 #a=a-4
print(a)

a*=5 #a=a*5
print(a)

a/=3  #a=a/3
print(a)

a%=5 #a=a%5
print(a)

a//=5 #a=a//5
print(a)

a**=5 #a=a**5
print(a)




#comparison operators

x=10
y=20

print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x>=y)
print(x<=y)


#logical operator
x1=30
y=28
print(x1>5 and y<29)
print(x1>5 or y<30)
print(not(x>30 and y<10))



#Identity Operator
num1=10
num2=7
print(num1 is num2)
print(num1 is not num2)


str1="hello"
str2="hello"
print(str1 is str2)


z=[1,2,3]
z1=[1,2,3]
print(z is z1)

#membership operator
num3=["apple","banana"]
print("banana" in num3)

num4=["apple","banana"]
print("banana" not in num3)


####
m=25.73796211
print("%.3f"%m)
#output 25.737
print(True+False+1) #2




