#function
import math
#code1

x=44
def message():
    print("This is void and argument less function ",end="\n")
    print("writting functions in python",end="\n")
    print("value of X=",x,end="\n")

message()

'''
#code2

print("Enter 1st name: ")
name=input()
print("Last name: ")
last_name=input()

def print_name(name,last_name):
    print("name is {} {} ".format(name,last_name))
    
print_name()
# output : error :print_name() missing 2 required positional arguments: 'name' and 'last_name'





#code2
print("Enter 1st name: ")
name=input()
print("Last name: ")
last_name=input()

def print_name(First_name,last_name):
    print("name is {} {} ".format(first_name,last_name))
    
print_name(name,last_name)



#code3
#call funtion methods and return 1 value
def find_product(a,b,c):
    res=a*b*c
    return res

print("Enter value of a: ")
a=int(input())
print("Enter value of b: ")
b=int(input())
print("Enter value of c: ")
c=int(input())


#method1
res=find_product(a,b,c)
print(res)

#method 2
print(find_product(a,b,c))

#method3 use return value in expression
y=3
print("value of x is ",y+find_product(a,b,c))

#method4 using build in function
print(math.sqrt(find_product(a,b,c)))

'''

#code5
#positional parameter
#return multiple values

def operation(a,b,c):
    sum=a+b+c
    mul=a*b*c
    squ_sum=(a*a)+(b*b)+(c*c)
    return sum,mul,squ_sum
#caling function
n1,n2,n3=2,3,4
add,prod,sqsummation=operation(n1,n2,n3)
    
print("Addition of n1,n2,n3 is ",add)
print("Multiplication of n1,n2,n3 is ",prod)
print("Addition of square of n1,n2,n3 is ",sqsummation)













