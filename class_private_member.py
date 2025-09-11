class Student:
    #private members
    __name=None
    __roll=None
    __branch=None
    def set_details(self,name,roll,branch):
        #Assign value to private data member
        self.__name=name
        self.__roll=roll
        self.__branch=branch
        #print("__name: ",__name)
        print(self.__name,self.__roll,self.__branch)

    #private member function
    def __displayDetails(self):
        #accesing private data member
        return f'Roll no-{self.__roll}\tName-{self.__name}\t'

    #public member function
    def call_private(self):
        #accessing private member function via public instance function of a class
        return self.__displayDetails()


studObj=Student()
studObj.set_details("sham",12,"IT")
print(studObj.call_private())

#name mangling= access private variable outside the class

print(studObj._Student__name)
