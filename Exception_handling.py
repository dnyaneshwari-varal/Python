
def display():
    print("I am in display function!!")
try:
    length=int(input("Enter length \n"))
    breadth=int(input("Enter breadth \n"))
    area=length/breadth
    output=length/0   #exception occure here  zeroDivisionError

except NameError as ne:
    print("Some error: ",ne)
except Exception as e:
    print("Some error: ",e)
else:
    print("Area=",area)
    print("Area calculation succesfully!!")

display()
print("Line outside the try block!!")




#1.using only one exception(catching specific exception)

def show():
    print("Inside show function")
try:
    x=int(input("Enter X value: "))
    y=int(input("Enter Y value: "))
    div=x/y
    print(div)
except ZeroDivisionError as ze:
    print("some error: ",ze)
else:
    print("Successfull!!")


show()


#2.using more than one acception

a=["Hello","Varal",2004]
try:
    print(a[6])
except IndexError as In:
    print("some error: ",In)
except ZeroDivisionError as ze:
    print("some error: ",ze)
except NameError as ne:
    print("Some error: ",ne)   


#3 Exception that find out which exception occured
a=["Hello","Varal",2004]
try:
    print(a[6])

except ZeroDivisionError as ze:
    print("some error: ",ze)
except NameError as ne:
    print("Some error: ",ne)
except Exception as e:
    print("Some error: ",e)


#4 use finally keyword
cube=1
try:
    num=int(input("Ebter number: "))
    print("YOu enter num value ",num)
except ValueError:
    print("Thats not valid number.")
else:
    cube=num**3
    print("num: ",num,"its cude is: ",cube)
finally:
    print("finally always get executed!!")
    print("Program Execution completed!!")


#5 use raise keyword

try:
    name=input("Enter name: ")
    age=int(input("Enter age "))
    if age<18 or age >50:
        raise ValueError("Invalid Age!! for age criteria")
    else:
        print("Welcome {} your age is {}".format(name,age))
    print("Hellow this is last Stastment.")
except Exception as e:
    print(e)


print("Outside try block")








































