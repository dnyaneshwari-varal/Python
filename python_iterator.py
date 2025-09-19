#code1
print("----code1----")
product=("TV","Washing machine","Phone")
myit=iter(product)
print(next(myit))
print(next(myit))
print(next(myit))

#output
#TV
#Washing machine
#Phone


#code2
print("----code2----")
my_list=["seed","Infotech","Pune",414033]
my_iter=iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#code3
print("----code3----")
my_list1=["Dnyaneshwari","Nighoj","Pune",414306]
my_iter1=iter(my_list1)
while True:
    try:
        print(next(my_iter1))
    except Exception as e:
        print("end of list! ",e)
        break
