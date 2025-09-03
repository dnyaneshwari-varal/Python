
#1
#DEfine function to check no is odd or even


def even_odd(num):
    if(num%2==0):
        print(num," is even")
    else:
        print(num," is odd")
    #return res1,res2
print("Enter number to check if it is odd or even: ")
num=int(input())
even_odd(num)

#2
#write function to calculate area of rectangle function should return output
def reac_area(length,width):
    area1=length*width
    return area1

print("Enter length: ")
length=int(input())
print("Enter Width: ")
width=int(input())

area=reac_area(length,width)
print("Area of reactangle is: ",area)



#create function to convert celsius to fahrenheit.return output
def cels_fahr(tempc):
    tempF=(tempc*1.8)+32
    return tempF


print("Enter temperature in celsius to conver fahrenheit: ")
tempC=int(input())
Fahr=cels_fahr(tempC)
print("Temperature in Fahrenheit: ",Fahr)
