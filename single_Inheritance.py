class Company:
    def __init__(self,project,location):
        self._project=project
        self.location=location

    def __str__(self):
        res="Project Title: "+self._project
        res=res+' To be executed at: '+self.location
        return res

class Employee(Company):
    def __init__(self,name,project,loc):
        super().__init__(project,loc)
        self.name=name

    def show(self):
        res="Employee name: "+self.name +"\n"
        res +="Working on project: "+self._project+"\n"
        res +="Project location: "+self.location+ "\n"
        return res
    def __str__(self):
        return "Employee name: "+self.name+" " +super().__str__()

emp=Employee("Varun Dhavan","Account mgmt","Pune")
print(emp.show())
print(emp)
