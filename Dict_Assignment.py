'''
def student_dict(d1):
 for i in d1:
   #print(i,d1[i])
   if(d1[i]>=90 and d1[i]<=100):
       d1[i]="A"
   elif(d1[i]>=80 and d1[i]<=89):
       d1[i]="B"
   elif(d1[i]>=70 and d1[i]<=79):
       d1[i]="C"
   elif(d1[i]>=60 and d1[i]<=69):
       d1[i]="D"
   else:
       d1[i]="F"
 return d1
    
       


d1={"Ram":89,"Sham":57,"Prem":67,"Raj":87,"Siya":90}
result=student_dict(d1)
print(result,end='\n')
'''
'''
keys=int(input("Enter total keys in dictionary: "))
d1={}
#dict_grade={}
for i in range(0,keys):
    key=input("Enter Key: ")
    value=int(input("Enter Value: "))
    d1[key]=value

print(d1)

student_grade={}
for i in d1:
    if(d1[i]>=90 and d1[i]<=100):
       d1[i]="A"
       student_grade[i]=d1[i]
    elif(d1[i]>=80 and d1[i]<=89):
       d1[i]="B"
       student_grade[i]=d1[i]
    elif(d1[i]>=70 and d1[i]<=79):
       d1[i]="C"
       student_grade[i]=d1[i]
    elif(d1[i]>=60 and d1[i]<=69):
       d1[i]="D"
       student_grade[i]=d1[i]
    else:
       d1[i]="F"
       student_grade[i]=d1[i]
print(student_grade)

Enter total keys in dictionary: 3
Enter Key: ram
Enter Value: 58
Enter Key: radha
Enter Value: 57
Enter Key: raj
Enter Value: 89
{'ram': 58, 'radha': 57, 'raj': 89}
{'ram': 'F', 'radha': 'F', 'raj': 'B'}

'''

'''
#2
text=input("Enter Text: ")
text=text.lower()
#keys are words and values are there occurance count
words=text.split()
dict1={}
print(words)
for i in words: 
  count=0

  for j in words:
    if i==j:
        count+=1
  
  #dict1.update({i:count})
  dict1[i]=count
print(dict1) 

'''
#3
dict={
    'SI9012340':{"Name":"Amit","Cource":"FSD-DS"},
    'SI9012341':{"Name":"Raj","Cource":"FSD-DS"},
    'SI9012342':{"Name":"Prem","Cource":"FSD-DS"},
    'SI9012343':{"Name":"Radha","Cource":"FSD-DS"},
    'SI9012344':{"Name":"Sham","Cource":"FSD-DS"}
    }
for i in dict:
    print(i , end="\t")
    for j in dict[i] :
       print(j,": ",dict[i][j],end="\t")
    print()





#4
    '''
total_key=int(input("Enter Total keys: "))
for i in range(total_keys):
    key=int(input("Enter Key: "))
'''


#take input as  how many sales men work in specific region
#region are north,south,east,west we need to choose it
#get data of sales men and then make distinary as north is key and {all sales men data}

region=input("Enter region: ")
sales_men=int(input("Enter how many member works: "))


s_1={}
s_2={}
s_3={}
s_4={}




for i in range(sales_men):
    Id=int(input("enter sales_men Id: "))
    name=input("Enter Name: ")
    sal=int(input("Enter sal: "))
    s_1={"Id":Id,"Name":name,"Salary":sal}
print(s_1)
    






































































    









    
