class Employee:
    emp_sal=100
    def cal_sal(self,sal):
        
        self.emp_sal=sal
        #print(self.emp_sal)
        TA=self.emp_sal*0.05
        print(TA)
        DA=self.emp_sal*0.05
        total_sal=TA+DA+self.emp_sal
        #print(total_sal)
        return total_sal


empObj=Employee()
id=int(input("Enyer Employee ID: "))
name=input("Enter Employee name: ")
sal=int(input("Enter Salary: "))

total_salary=empObj.cal_sal(sal)
print("ID: {}, name: {}, salary: {}, Total Salary: {} ".format(id,name,sal,total_salary))
