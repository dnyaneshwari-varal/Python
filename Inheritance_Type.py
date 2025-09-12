class Company:
    def __init__(self,company_name):
        self.company_name=company_name

    def show_company(self):
        print(f"Company:{self.company_name}")

#single Inheritance
class Employee(Company):
    def __init__(self,company_name,emp_name,emp_id):
        super().__init__(company_name)
        self.emp_name=emp_name
        self.emp_id=emp_id

    def show_employee(self):
        print(f"Employee ID: {self.emp_id},Name:{self.emp_name}")

#multilevel Inheritance

class Manager(Employee):
    def __init__(self,company_name,emp_name,emp_id,dept):
        super().__init__(company_name,emp_name,emp_id)
        self.dept=dept

    def show_manager(self):
        print(f"Manager of {self.dept} Department")

#multiple Inheritance
class Department:
    def __init__(self,dept_name):
        self.dept_name=dept_name

    def show_department(self):
        print(f"Department:{self.dept_name}")

#manager inherits from both employee and department
class Senior_Manager(Manager,Department):
    def __init__(self,company_name,emp_name,emp_id,dept,dept_name):
        super().__init__(company_name,emp_name,emp_id,dept)
        Department.__init__(self,dept_name) #explicitly initialize department

    def show_senior_manager(self):
        print(f"Senior Manager of {self.dept} in {self.company_name}, handles {self.dept_name} department")

#hierarchical
class Engineer(Employee):
    def __init__(self,company_name,emp_name,emp_id,skill):
        #Employee.__init__(self,company_name, emp_name, emp_id)
        self.skill=skill

    def show_engineer(self):
        print(f"Engineer:{self.emp_name},skill:{self.skill}")

class hr(Employee):
    def __init__(self,company_name,emp_name,enmp_id,region):
        super().__init__(company_name,emp_name,enmp_id)
        self.region=region

    def show_hr(self):
        print(f"HR{self.emp_name},Region:{self.region}")


#hybrid inheritance TechLead companies seniorManager and engineer

class TechLead(Engineer,Senior_Manager):
    def __init__(self,company_name,emp_name,emp_id,dept,dept_name,skill):
        Senior_Manager.__init__(self,company_name,emp_name,emp_id,dept,dept_name) #initialize SeniorManage
        Engineer.__init__(self,company_name,emp_name,emp_id,skill) #explicitly initialize Engineer

    def show_tech_lead(self):
        print(f"Tech lead:{self.emp_name},Expert in {self.skill},Manages:{self.dept_name}")


#testing class
print("\n __hybrid inheritance___")
t1=TechLead("Wipro","Dnyaneshwari",106,"IT","Software Development","java")
t1.show_company()
t1.show_employee()
t1.show_manager()
t1.show_department()
t1.show_engineer()
t1.show_tech_lead()


    






