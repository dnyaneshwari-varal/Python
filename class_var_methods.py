#1
class Demo:
    x=10

    def ascess(self):
        y=20
        print("in acess instance method")
    @classmethod
    def Dmethod(cls): #we cant directly accece instance variable
        print(cls.x)

obj1=Demo()
obj1.ascess()
Demo.Dmethod()
'''
#2
class BTech_Student:
    #class variable
    university="US University"
    year="Final year"

    #instance Variable
    fullname=None
    gender=None

    #public instance method or constructor
    def __init__(self,name,gender):
        self.fullname=name
        self.gender=gender

    @classmethod
    def change_year(cls,year):
        #class_name class_variable
        cls.year=year

    @classmethod
    def transfer_university(cls,university):
        #class_name class_variable
        cls.university=university

    @classmethod
    def change_year(cls,year):
        #class_name class_variable
        cls.year=year
        

    #instance method
    def get_details(self):
        res='Name-%s\n'%(self.fullname)
        res +='Gender-%s\n'%(self.gender)
        res +='Year-%s\n'%(self.year)
        res +='University-%s\n'%(BTech_Student.university)
        return res

obj1=BTech_Student("Ram","Female")
BTech_Student.change_year(2025)
BTech_Student.transfer_university("Indian university")
BTech_Student.change_year(2024)
print(obj1.get_details())

print(BTech_Student.year)
print(BTech_Student.university)

print(obj1.fullname)
print(obj1.gender)

'''























    
        
