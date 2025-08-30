#Write a program that checks if a tuple reads the same forwards and backwards.
#palindrom

tup=(1,2,3,2,3,2,1)
#print(tup[-1])
back=-1
size=len(tup)
count=0
#print("size is: ",size)

for i in range(0,(len(tup)//2)):
   if(tup[i]==tup[back]):
            count+=1
   back -=1
if(count==len(tup)//2):
         print("tup is palindrome")
else:
       print("tup is not palindrome")
 
       
# Create a tuple that contains 3 employee records, where each record tuple (ID, Name, Salary).
#Write a program to print the name of the employee with the highest salary

tup=((100,"Ram",20000),(101,"sham",10000),(102,"siya",500000),(102,"priya",10000))
sal=0
for i in range(0,len(tup)):
    for j in tup[i]:
        if(sal<tup[i][2]):
          sal=tup[i][2]
          name=tup[i][1]
          break
print("highest salary of: ",name," is ",sal)
        
