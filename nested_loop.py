#code1
for i in range(1,6):
    for j in range(3):
        print(i)
    print(end='\n')
    

#code2
for i in range(1,6):
    for j in range(3):
        print(j)
    print(end='\n')



#code3
for i in range(1,6):
    for j in range(3):
        print(i,end=' ')
    print(end='\n')


#code4
num=1
for i in range(1,6):
    for j in range(i):
        print(num,end=' ')
        num+=1
    print(end='\n')


#code5

for i in range(1,6):
    num1=1
    for j in range(i):
        print(num1,end=' ')
        num1+=1
    print(end='\n')


#code6
num2=1
for i in range(1,6):
    for j in range(i):
        print(num2,end=' ')
    print(end='\n')


#code6
#print table from 2 to 10

for i in range(2,10):
    print("table of ",i,end='\n')
    for j in range(1,11):
        res=i*j
        print("{}*{} = {}".format(i,j,res),end=' \n'),
    print(end='\n')












