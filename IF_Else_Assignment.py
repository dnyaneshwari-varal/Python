
#code 1
#1-Write a program to input two numbers and print their sum, difference, product, and division.

num1=int(input("Enter num1 "))
num2=int(input("Enter num2: "))
add=num1+num2
print("addition of {} and {} is {}".format(num1,num2,add))
sub=num1-num2
print("difference of {} and {} is {}".format(num1,num2,sub))
prod=num1*num2
print("product of {} and {} is {}".format(num1,num2,prod))
div=num1/num2
div=round(div,4)
print("division of {} and {} is {}".format(num1,num2,div))
'''
output=
Enter num1 23
enter num2: 45
addition of 23 and 45 is 68
difference of 23 and 45 is -22
product of 23 and 45 is 1035
division of 23 and 45 is 0.5111
'''



#2-Write a program to take the radius of a circle as input and print its area.
#(Hint: Area = 3.14 * r * r)

r=int(input("Enter radius of circle: "))
area=3.14*r*r
area=round(area,3)
print("area of circle is: ",area)
'''
output=enter radius of circle: 4
area of circle is:  50.24
'''


#3-Write a program to input three numbers and print the largest number.
x=int(input("Enter num1 "))
y=int(input("Enter num2 "))
z=int(input("Enter num3 "))
if(x>y and x>z):
    print("largest num is: ",x)
elif(y>x and y>z):
    print("largest num is: ",y)
else:
    print("largest num is: ",z)
'''
output=
enter num1 12
enter num2 10
enter num3 20
largest num is:  20
'''

#4=Write a program to create a simple calculator that performs addition, subtraction, multiplication, and division based on user choice.
#(Hint: Take two numbers as input and then ask the user to enter +, -, *, or /)


x=int(input("Enter num1 "))
y=int(input("Enter num2 "))
perform=input("enter +,-,*,/  ")
if(perform=="+"):
    print("Adition is: ",x+y)
elif(perform=="-"):
    print("subtraction is: ",x-y)
elif(perform=="*"):
    print("multiplication is: ",x*y)
else:
    print("division is: ",x/y)
'''
enter num1 12
enter num2 17
enter +,-,*,/  *
multiplication is:  204'''

#5=Write a program to input two numbers and check which one is greater using comparison operators.
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
if(n1>n2):
    print("greater num is: ",n1)
else:
    print("gratest number is: ",n2)
'''
output
enter n1: 10
enter n2: 28
gratest number is:  28
'''

#6-Write a program to input a number and print whether it is even or odd using modulus operator %.
num1=int(input("Enter num1"))

if(num1%2==0):
    print(num1," number is even")
else:
    print(num1," number is odd")

#7-Write a program to input a number and find its square and cube using exponent operator **.

num1=int(input("Enter num1"))
sqr=num1**2
print("square of {} is {}".format(num1,sqr))

cube=num1**3
print("square of {} is {}".format(num1,cube))

'''
output
enter num12
square of 2 is 4
square of 2 is 8

'''
#8-Write a program to input a number and check if it is divisible by both 3 and 5.

num=int(input("Enter num"))
if(num%3==0 and num%5==0):
    print(num," divisible by 3 and 5 both")
else:
    print(num," not divisible by 3 and 5")

'''
output
enter num13
13  not divisible by 3 and 5
'''




#9=Write a program to input a person’s age and decide if they are:

'''Child (age < 13)

Teenager (13–19)

Adult (20–59)

Senior (60 and above) '''

age=int(input("Enter age"))
if(age <13):
    print("child")
elif(age>=13 and age<=19):
    print("Teenager")
elif(age>=20 and age<=59):
    print("Adult")
elif(age>60):
    print("Senior")
'''
output
enter age61
Senior
'''

#10-Write a program to input marks of a student and print the Grade:
'''
90 and above → A

80-89 → B

70-79 → C

60-69 → D

Below 60 → Fail
'''
marks=int(input("Enter marks: "))
if(marks>90):
    print("A grade")
elif(marks>=80 and marks<=89):
    print("B")
elif(marks>=70 and marks<=79):
    print("c")
elif(marks>=60 and marks<=69):
    print("D")
elif(marks<60):
    print("fail")
'''
output
Enter marks: 20
fail
'''




#11-Write a program to input a year and check whether it is a leap year or not.
#(Hint: A year is leap if divisible by 400 OR (divisible by 4 but not by 100))


year=int(input("enter year: "))
if(year%400==0 or (year%4==0 and year%100!=0)):
    print(year," is leap year")
else:
    print(year,"not leap year")

''''
enter year: 1920
1920  is leap year
'''












