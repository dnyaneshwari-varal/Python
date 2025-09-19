'''
import math
#code1
def sqr_root(n):
    return math.sqrt(n)

numbers=[16,36,100,4]
result=map(sqr_root,numbers)
print(f'Square roots-{list(result)}') #Square roots-[4.0, 6.0, 10.0, 2.0]


#with lambda function

numbers=[16,36,100,4]
result=map(lambda n: math.sqrt(n),numbers)
print(f"Square roots - {list(result)}") #Square roots - [4.0, 6.0, 10.0, 2.0]

#code2

#filter
def is_even(n):
    return n%2==0
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=filter(is_even,numbers)
print("Even numbers: ",list(even_numbers)) #Even numbers:  [2, 4, 6, 8, 10]

#with lambda function
even_num=filter(lambda n : n%2==0,numbers)
print(list(even_num)) #[2, 4, 6, 8, 10]



#reduce
#code1
from functools import reduce
def add(x,y):
    return x+y
nums=[2,4,6,8,10]
result=reduce(add,nums)
print("sum of all elements: ",result)   #30

'''
#Assignment
#1.use map() and lambda
#increase each product price by 10% tax

product=[100,500,4600]
after_tax=list(map(lambda n: ((n*0.1)+n),product))
print("after tax: ",after_tax)

#2
#use filter and lambda
#filter out all products that are more than 300 after tax


filter_prod=list(filter(lambda n: n>300,after_tax))
print("all products that are more than 300 after tax ",filter_prod)

#3
#use reduce() and lambda
#find total cost of all product after tax
from functools import reduce
total_cost=reduce(lambda a,b: a+b,after_tax)
print("Total cost of all products after tax:", total_cost)


#4
#find most expensive product befor tax using reduce()

def check_prod:
    
exp_prod=reduce(check_prod,product)















