'''
#code1

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
#output

Enter total keys in dictionary: 3
Enter Key: ram
Enter Value: 58
Enter Key: radha
Enter Value: 57
Enter Key: raj
Enter Value: 89
{'ram': 58, 'radha': 57, 'raj': 89}
{'ram': 'F', 'radha': 'F', 'raj': 'B'}




# code 2
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


#code 3
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






#4 incomplete

#take input as  how many sales men work in specific region
#region are north,south,east,west we need to choose it
#get data of sales men and then make distinary as north is key and {all sales men data}



regions=["North","South","East","West"]
student_per_region=int(input("Enter how many member works: "))

students={}

for region in regions:
    students[region]={}
    for j in range(1,student_per_region+1):
        sid=f"{region}_{j}"
        name=input("Enter Name: ")
        sal=int(input("Enter sal: "))
        students[region][sid]={"SID":sid,"Name":name,"Salary":sal}

for region,student_dict in students.items():
        print(f"\nRegion:{region}")
        for sid,detail in student_dict.items():
            print(detail)
print("1.Display all sales person data")
print("2.Add new sales person data")
print("3.Update sales person data")
print("4.Delete sale person data")
choice=int(input("Enter choice: "))
if choice==1:
    for region,student_dict in students.items():
        print(f"\nRegion:{region}")
        for sid,detail in student_dict.items():
            print(detail)






#5
Employee={}
Total_emp=int(input("Enter total Emloyees: "))

for i in range(1,Total_emp+1):
    emp_id=int(input("Enter Empoyee ID: "))
    emp_name=input("Enter employee name: ")
    Dep=input("Enter employee Department: ")
    sal=int(input("Enter Salary: "))
    Employee[i]={"ID":emp_id,"Name":emp_name,"Department":Dep,"Salary":sal}
    print(Employee[i])

for j in range(1,Total_emp):
        print(Employee[j])


to_search=input("Enter Department name to search: ")
count=0
for i in Employee:
    #print(i)
    #print(Employee[i]["Department"])
    if Employee[i]["Department"]==to_search:
    
         count+=1
         print(count,Employee[i])
       
print(count)
new_dict={}
for i in Employee:
    #print(Employee[i]["Salary"])
    if Employee[i]["Salary"]>10000:
        new_dict[i]=Employee[i]
print(new_dict)
     

#6
#key becomes value value become key


dict1={1:"Dnayneshwari",2:"Isha",3:"Sham",4:"Hanu"}
inverted_dict={}
for key in dict1:
     value=dict1[key]
     inverted_dict[value]=key
    
    
    
print(inverted_dict)
   

#6
#Merge Dictionaries
#Take two dictionaries as input and merge them.
#If a key is common in both, add their values instead of replacing.

dict1={}
dict2={}
items=int(input("How many items for dict: "))
for i in range(items):
    
    num1=int(input("Enter num1: "))  #key
    num2=int(input("Enter num2: ")) #value
    
    dict1[num1]=num2
    
print(dict1)

items1=int(input("How many items for dict: "))
for j in range(items1):
    
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    dict2[num1]=num2
    
print(dict2)

merge={}

for i in dict1:
    merge[i]=dict1[i]

for k in dict2:
    if k in merge:
        merge[k] +=dict2[k]
    else:
        merge[k]=dict2[k]
print("dict1 is: ",dict1)
print("dict2 is: ",dict2)
print("merge Dictionary: ",merge)


#7 Write a program to print all unique values from a dictionary that may have duplicate values.


d1={1:"a",2:"b",3:"c",4:"a",5:"b",6:"z"}
result={}
for i in d1:
    print(d1[i])
    if d1[i] not in result.values():
        result[i]=d1[i]
print(result)

'''

#8
total_stud=int(input("Enter num of students: "))
students={}

subject=int(input("Enter total subjects: "))
for i in range(total_stud):
  name=input("Enter Name: ")
  mark_dict={}
  for j in range(subject): 
    sub=input("Enter subject: ")
    marks=int(input("Enter marks: "))
    mark_dict[sub]=marks
  students[i]={name:mark_dict}

for i in students:
    print(students[i])

for j in students:
    total=0
    count=0
    for name,marks in students[j].items():
        for mark in marks.values():
           total=total+mark
           count=count+1
        avg=total/count
    print("Average marks of student {} is {:.2f} ".format(name,avg))
first_stud=""
for n in students:
    first_stud=n
    break
for sub in students[first_stud]:
    max=0
    topper=""
    for name in students:
        marks=students[name][sub]
        if (marks > max):
          max=marks
          topper=name
    print("Topper name: ",sub,"is ",topper,"with",max,"marks")
        
     

    


        
        

















































    









    
