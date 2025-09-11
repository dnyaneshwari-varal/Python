class Demo_constr:
    x=10   #class/static variable   we can access it anywhere in class and outside class
    #no parameterized constructor
    def __init__(self):
        print("In no parametrized constructor")

    #parameterized constructor
    def __init__(self,name,sal):
        print("In parametrized constructor")
        print("name and salary is ",name,sal)
    def __Acces(self):
        print("Hello ")

    def demo(self):
        y=10  #instance variable
        print(x)
#obj=Demo_constr()   ata time we only can call one constructor
obj1=Demo_constr("Ram",20000)
#obj1.__Acces()  we are not able to access private method outside from class

print("print x with help of class name: ",Demo_constr.x)
print("print x with help of class obj: ",obj1.x)

#print(obj1.y)  # we cant access y instance var with help of class obj or class name
