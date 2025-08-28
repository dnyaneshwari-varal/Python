'''
#1.find sum of all digits in enterd number
num=int(input("Enter number: "))
temp=num
sum=0
count=0
while(temp !=0):
    rem=temp%10
    
    sum=sum+rem
    temp=temp//10
    
    count=count+1

print("sum of all digits in {} is {} ".format(num,sum))
print(count)


'''


#2.find largest and smallest elemnt in list
lst=[17,4,27,39,23,1,6]
size=len(lst)
print(size)
small=lst[0]
largeEle=lst[0]
for i in range(1):
    for j in range(1,size):
        if(small>lst[j]):
            small=lst[j]
            #print(small)
        
print("smallest numb is: ",small)
for i in range(size):
    for j in range(size):
        if(largeEle<lst[j]):
            largeEle=lst[j]
      
print("largest numb is: ",largeEle)

#smallest numb is:  1
#largest numb is:  39

#3
row=5
for i in range(row):
    num=5
    for j in range(row-i):
        print(num,end=' ')
        num-=1
    print(end='\n')
'''
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5
'''


#4
row=5
for i in range(row):
    for j in range(1,row-i+1):
        print(j,end=' ')
        
    print(end='\n')
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''


#5
row=int(input("enter row: "))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()


#pyramid
row=int(input("enter row: "))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(row-1,0,-1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
   
        

