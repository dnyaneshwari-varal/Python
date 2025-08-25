'''1. write code to find area of right angle traingle(0.5*base*height) based on input and height'''


base=int(input("enter base: "))
height=float(input("enter height: "))
area=(0.5*base*height)
print("area of right angle is ",area)
#output
'''
enter base: 5
enter height: 10
area of right angle is  25.0'''


#2 
'''
DA is 5% of salary
HRA is 3% of salary
pf=750 it is detucted as 7% of salary
calculate gross=salary+hRA+DA
while net salary=gross-pf-IT
ouput
emp name:abc
Designation:team leader
Department:development
salary:40000
DA... HRA... IT... PF...
net salary...
'''
emp_name=input("employee name: ")
Designation=input("Designation: ")
Department=input("Department: ")
salary=int(input("salary: "))
DA=(5/100)*salary
HRA=(3/100)*salary
PF=750
IT=(7/100)*salary #tax on your salary
IT=round(IT,2)

Gross=salary+HRA+DA
print("DA- {}  HRA- {} IT- {} PF- {}".format(DA,HRA,IT,PF))
netSal=Gross-PF-IT
print("Net Salary- ",netSal)
'''
employee name: ram
Designation: team leader
Department: dev
salary: 50000
DA- 2500.0  HRA- 1500.0 IT- 3500.0 PF- 750
Net Salary-  49750.0
'''



#3 calculate and display the area,diameter and circumference of a circle.
#area=3.14*r^2
#circumference=2*3.14*r or  c=3.14*diameter
#diameter=2r

r=int(input("enter radius: "))
Pi=3.14
area=Pi*(r**2)
diameter=2*r
c=Pi*diameter
c=round(c,3)
print("area of circle is {}, diameter of circle is {}, circumference of circle is {}".format(area,diameter,c))

'''output
enter radius: 3
area of circle is 28.26, diameter of circle is 6, circumference of circle is 18.84'''



#4 output will be
'''
student name-...
marks:maths-.. english-.... science-...
Total-.... average-...
'''
name=input("Student Name: ")
Eng_Mark=int(input("English marks: "))
Sci_Mark=int(input("Science marks: "))
Math_Mark=int(input("Maths marks: "))
total=Eng_Mark+Sci_Mark+Math_Mark
Avg=total/3
print("Student name ",name)
print("Marks:Maths-{}  English-{} Science-{}".format(Math_Mark,Eng_Mark,Sci_Mark,))
print("Total-{}  Average-{} ".format(total,Avg))

'''output
Student Name: ram
English marks: 46
Science marks: 46
Maths marks: 46
Student name  ram
Marks:Maths-46  English-46 Science-46
Total-138  Average-46.0
'''






