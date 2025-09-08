from my_package.Calculator import *
from Geometrical_shapes import *


while True:
    print("1. Find Area of Rectangle: ")
    print("2. Find Area of Square: ")
    print("3. Find Area of Circle: ")

    choice=int(input("Enter which function you want to perform: "))
   

    if choice==1:
        length=int(input("Enter length of rectangle: "))
        width=int(input("Enter width of rectangle: "))
        
        print("Area of rectangle is: ",rectArea(length,width))

    elif choice==2:
        side=int(input("Enter length of side: "))
        print("Area of square is: ",sqrArea(side))

    elif choice==3:
        radius=int(input("Enter radius of circle: "))
        print("Area of circle is: ",circleArea(radius))
    else:
        break

        
print("Addition: ",add(10,2))
print("Multiplication: ",mul(12,7))
print("Subtraction: ",sub(10,4))
print("Division: ",div(12,6))
print("Square of num: ",find_sqr(5))
