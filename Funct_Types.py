'''
#Types of Function
#Positional arguments
def pos_arg(num1,num2,num3):
    print(num1+num2+num3)


pos_arg(10,20,30)




#Default Argument
#code 1
def default_Arg(arg1,arg2,arg3=10,arg4=8):  
    print(arg1,arg2,arg3,arg4)

default_Arg(20,17,68)

#code2
def default_Arg(arg1=34,arg2=67,arg3,arg4):  #(arg1=1,arg2=2,arg3=6,arg4,arg5) we cant write that give error 
    print(arg1,arg2,arg3,arg4)

default_Arg(20,17)

#code3
def default_Arg(arg1=34,arg2,arg3=9,arg4=1):  #error not work
    print(arg1,arg2,arg3,arg4)

default_Arg(20) 


#Keyword Argument

def emp_add(name,des,Basic,company="Apple"):
    TA=Basic*(0.5)
    DA=Basic*(0.7)
    pf=Basic*(0.8)
    total_sal=Basic+DA+TA-pf
    return total_sal,Basic
    
Total_sal,basic_sal=emp_add(Basic=50000,name="Dnyaneshwari",des="Software Engineer")
print("Salary before adding TA DA and PF: ",basic_sal)
print("Salary after adding TA DA and PF: ",Total_sal)


emp=emp_add(Basic=50000,name="Dnyaneshwari",des="Software Engineer")
print(emp)


'''




#Arbitrary Argument
#1.variable length arguments(*arg)
def fun_Arb(*arg):
    print(type(arg)) #tuple
    for var in arg:
        print(var)
    #for i in range(len(arg)):
    #   print(arg[i])

fun_Arb(10,20,30)
fun_Arb("hello","Students")


#2

def ArbKey(**info):
    print(type(info))
    for i in info.items():
        print(i)

#ArbKey(1="DS",2="java")  we cant give values like this

ArbKey(course1="DSA",cource2="DA",cource3="DS",Cource4=".Net")






























