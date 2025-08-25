Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> day=10
>>> month=12
>>> year=2025
>>> # using Seperator and end
>>> print(day,month,year,sep='-')
10-12-2025
>>> print(day,month,year,sep='/')
10/12/2025
>>> print(day,month,year,sep='-',end="\t")
10-12-2025	
>>> a="hello"
>>> b="Bye"
>>> print(a,b,end='\t')
hello Bye	
>>> print(a,b,end='\n')
hello Bye
>>> print(a,b,end="\n")
hello Bye
>>> print(a,b,sep="*",end='\t')
hello*Bye	
>>> 
>>> 
>>> 
>>> 
>>> a1=""Dnyaneshwari"
SyntaxError: unterminated string literal (detected at line 1)
>>> a1="Dnyaneshwari"
>>> b1=""Varal"
SyntaxError: unterminated string literal (detected at line 1)
>>> b1="Varal"
>>> #concatination
>>> print(a1+" "+b1)
Dnyaneshwari Varal
>>> 
>>> 
>>> 
>>> #useing end
>>> str1="ram"
>>> str2="radha"
>>> print(str1,str2,end='\n')
ram radha
print("done")
done
print(str1,str2,end='\n',sep='*')
ram*radha
print(str1,str2,sep='*',,end='\n')
SyntaxError: invalid syntax
print(str1,str2,sep='*',end='\n')
ram*radha
print(str1,str2,sep='*',end='\t')
ram*radha	
print(str1,str2,end='\n',sep='*')
ram*radha
