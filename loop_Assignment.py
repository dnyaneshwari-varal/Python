'''
#find factorial
num=int(input("Enter num: "))
temp=num
fact=1
while(temp>0):
    fact=fact*temp
    temp-=1
    
print("Factorial of, {} is {} ".format(num,fact))




#find digit from number
num1=int(input("Enter num1: "))
temp1=num1
count=0
while(temp1 > 0):
    rem=temp1%10    #get last digit
    
    count+=1
    temp1 //=10   #remove last digit
print(count)




#find prime number or not

num3=int(input("Enter the num3: "))
count=0
for i in range(2,num3+1):
    if(num3%i==0):
        count+=1
        if(count >1):
            break

if(count==1):
    print(num3," is prime number")
else:
    print(num3," is not prime number")




#prime number from 1 to 100
start=int(input("Enter start number"))
end=int(input("Enter end number"))

count2=0
for num in range(start,end+1):
    
    counter=0
    for j in range(1,num+1):
        if(num%j==0):
            counter+=1

    
    if(counter==2):
       print(num," is prime number")
       count2+=1
    else:
      print(num," is not prime number")
    
print(count2)         
    
'''


#menu driven

print("1.find number factorial of number: ","2.find digit of number "," 3.find prime no or not ","4.find even and odd")
for i in range(0,5):
  choice=int(input("Enter choices: "))

  if(choice==1):
    print("find factorial: ")
    num=int(input("Enter num: "))
    temp=num
    fact=1
    while(temp>0):
      fact=fact*temp
      temp-=1
    print("Factorial of, {} is {} ".format(num,fact))
  elif(choice==2):
    num1=int(input("Enter num1: "))
    temp1=num1
    count=0
    while(temp1 > 0):
      rem=temp1%10    #get last digit
    
      count+=1
      temp1 //=10   #remove last digit
    print(count)

  elif(choice==3):
    num3=int(input("Enter the num3: "))
    count=0
    for i in range(2,num3+1):
      if(num3%i==0):
        count+=1
        if(count >1):
            break

    if(count==1):
        print(num3," is prime number")
    else:
        print(num3," is not prime number")

  elif(choice==4):
    num=int(input("Enter num to check even odd: "))
    if(num%2==0):
        print(num," is even")
    else:
        print(num," is odd")

  else:
      print("Enter valid choice please!!")




    
