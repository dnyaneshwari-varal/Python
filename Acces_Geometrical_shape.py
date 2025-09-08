from Geometrical_shapes import *
while True:
    print("1. Find Area of Rectangle: ")
    print("2. Find Area of Square: ")
    print("3. Find Area of Circle: ")

    choice=int(input("Enter which function you want to perform: "))
    if choice==0:
        print("Enter valid choice please!!!")

    elif choice==1:
        length=int(input("Enter length of rectangle: "))
        width=int(input("Enter width of rectangle: "))
        
        print("Area of rectangle is: ",rectArea(length,width))

    elif choice==2:
        side=int(input("Enter length of side: "))
        print("Area of square is: ",sqrArea(side))

    elif choice==3:
        radius=int(input("Enter radius of circle: "))
        print("Area of circle is: ",circleArea(radius))  

   
