class Employee:
    def cal_sal(self,sal):
        TA=sal*0.05
        print(TA)
        DA=sal*0.05
        total_sal=TA+DA+sal
        print(total_sal)
        return total_sal


empObj=Employee()
id=int(input("Enyer Employee ID: "))
name=input("Enter Employee name: ")
sal=int(input("Enter Salary: "))

total_salary=empObj.cal_sal(sal)
print("ID: {}, name: {}, salary: {}, Total Salary: {} ".format(id,name,sal,total_salary))
