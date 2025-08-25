Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
num=[2,4,6,8,10]
print(num,type(num))
[2, 4, 6, 8, 10] <class 'list'>
num[3]==110
False
num[3]=110
print(num[3])
110
colors=["pink","yellow","red","white"]
print(color,type(color))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(color,type(color))
NameError: name 'color' is not defined. Did you mean: 'colors'?
print(colors,type(colors))
['pink', 'yellow', 'red', 'white'] <class 'list'>
students=[1,"alena",19,"Btech","Intern"]
print(student,type(student))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(student,type(student))
NameError: name 'student' is not defined. Did you mean: 'students'?
>>> print(students,type(students))
[1, 'alena', 19, 'Btech', 'Intern'] <class 'list'>
>>> #dictionary
>>> employee={'empId'=100,'empSalary'=20000,'empDepart'='Python Dev'}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> employee={'empId':100,'empSalary':20000,'empDepart':'Python Dev'}
>>> print(employee)
{'empId': 100, 'empSalary': 20000, 'empDepart': 'Python Dev'}
>>> print(employee,type(employee))
{'empId': 100, 'empSalary': 20000, 'empDepart': 'Python Dev'} <class 'dict'>
>>> print(employee['empSalary']=50000)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print(employee['empSalary']:50000)
... 
SyntaxError: invalid syntax
>>> print(employee['empSalary']==50000)
... 
False
>>> employee['empSalary']=50000
>>> print(employee['empSalary'])
50000
>>> print(employee)
{'empId': 100, 'empSalary': 50000, 'empDepart': 'Python Dev'}
>>> #Student
>>> stud={'id':12,'cource':'fullstack','fees':60000}
>>> print(stud)
{'id': 12, 'cource': 'fullstack', 'fees': 60000}
>>> print(type(stud))
<class 'dict'>
>>> stud['cource']='data analyst'
>>> print(stude['cource'])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(stude['cource'])
NameError: name 'stude' is not defined. Did you mean: 'stud'?
>>> print(stud['cource'])
data analyst
>>> print(stud)
{'id': 12, 'cource': 'data analyst', 'fees': 60000}
