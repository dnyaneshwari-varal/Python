Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data Types
#numeric
a=10
a
10
#OR
print(a)
10
print(type(a))
<class 'int'>
a=5
a
5
a="Hello"
a
'Hello'


#float

a=10.6
print(type(a))
<class 'float'>


#complex number
b=3+4i
SyntaxError: invalid decimal literal
b=1j
print(b,type(b))
1j <class 'complex'>



Boolean
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Boolean
NameError: name 'Boolean' is not defined
#boolean


>>> #Boolean
>>> x=true
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> x=0
>>> print(x)
0
>>> x=True
>>> x
True
>>> print(x,type(x))
True <class 'bool'>
>>> y=False
>>> print(x,y,type(x,y))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(x,y,type(x,y))
TypeError: type() takes 1 or 3 arguments
>>> print(x,y,type(y))
True False <class 'bool'>
>>> 
>>> 
>>> 
>>> 
>>> #String
>>> name="dnyaneshwari"
>>> father name='vinayak'
SyntaxError: invalid syntax
>>> father_name='vinayak'
>>> profesion='''currently doing java full
... stack to get job as a fullstack developer'''
>>> print(name ,father_name,profesion)
dnyaneshwari vinayak currently doing java full
stack to get job as a fullstack developer
>>> print(name \n,father_name \n,profesion)
SyntaxError: unexpected character after line continuation character
>>> print(name ,father_name,profesion,sep="\n")
dnyaneshwari
vinayak
currently doing java full
stack to get job as a fullstack developer
print(name + "\n" + father_name + "\n" + profession)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(name + "\n" + father_name + "\n" + profession)
NameError: name 'profession' is not defined. Did you mean: 'profesion'?
print(name +"\n",father_name +"\n",profesion)
dnyaneshwari
 vinayak
 currently doing java full
stack to get job as a fullstack developer
print(name ,+"\n"father_name,+"\n"profesion)
SyntaxError: invalid syntax. Perhaps you forgot a comma?


#len() it is used to find length of string
z="hello"
print(len(z




          ))
5
#hello=5
z="hello buddy!"
len(z)
12
print(z[1])
e
#indexing start from 0 in string






#collection

#list
'''list is mutable(can change)
   use to store multiple type of data
   represent in []
'''
'list is mutable(can change)\n   use to store multiple type of data\n   represent in []\n'
lst=[1,2,"Varal",10.2]
lst
[1, 2, 'Varal', 10.2]
len(lst)
4
print(lst[2])
Varal
lst[2]=Dnyana
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    lst[2]=Dnyana
NameError: name 'Dnyana' is not defined
lst[2]="Dnyana"
lst[2]
'Dnyana'
lst
[1, 2, 'Dnyana', 10.2]
lst[1]="varal"
lst
[1, 'varal', 'Dnyana', 10.2]



#tuple
#immutable(not change values)
#store multiple type of data
#represents in ()

tpl=(10,10.2,True,"xyz")
print(tpl,type(tpl))
(10, 10.2, True, 'xyz') <class 'tuple'>
len(tpl)
4
#not mutable
tpl[1]=16
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    tpl[1]=16
TypeError: 'tuple' object does not support item assignment



#Dictionary
#Key:value pair
#key must be unique
#values are duplicate no problem
#keys are immutable cant change but values can be change

#represent in{}

dict={1:"Ram",2:"Sham",3:"radha"}
print(dict,type(dict))
{1: 'Ram', 2: 'Sham', 3: 'radha'} <class 'dict'>
print(dict(2))
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    print(dict(2))
TypeError: 'dict' object is not callable
#so here dict is class but we assign variable to it thats why error is come

dict1={1:"Ram",2:"Sham",3:"radha"}
print(dict1[2])
Sham
dict1[2]="prem"
print(dict)
{1: 'Ram', 2: 'Sham', 3: 'radha'}
print(dict1)
{1: 'Ram', 2: 'prem', 3: 'radha'}
dict1[4]
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    dict1[4]
KeyError: 4

#add new pair
dict1["name"]="Rani"
dict1
{1: 'Ram', 2: 'prem', 3: 'radha', 'name': 'Rani'}



#homework
#dictionary for student
student={'name':'Dnayana',"studId":1,"cource":"fullstack"}
print(student,type(student))
{'name': 'Dnayana', 'studId': 1, 'cource': 'fullstack'} <class 'dict'>
print(student['studId'])
1
student['studId']=5
student
{'name': 'Dnayana', 'studId': 5, 'cource': 'fullstack'}
#add
student["fees"]=60000
student
{'name': 'Dnayana', 'studId': 5, 'cource': 'fullstack', 'fees': 60000}

#dictionary for employee
#1.print dictionary
emp={'empId':1,'department':"SE","salary":40000}
print(emp,type(emp))
{'empId': 1, 'department': 'SE', 'salary': 40000} <class 'dict'>
#update
emp["salary"]=50000
print(emp["salary"])
50000
#add
emp["laguage"]="Python"
emp
{'empId': 1, 'department': 'SE', 'salary': 50000, 'laguage': 'Python'}
