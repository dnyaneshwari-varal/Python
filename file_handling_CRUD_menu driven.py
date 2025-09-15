#menu driven
class EmpData:
    def __init__(self):
        self.emp_dict={}
        
    def Add_data(self):
        data=open("emp_data.txt","a+")
        id=int(input("Enter ID of Employee: "))
        name=input("Enter name of Employee: ")
        loc=input("Enter location of Company: ")
        self.emp_dict[id]={"ID":id,"Name":name,"Location":loc,}
        data.write(str(self.emp_dict[id])+'\n')
        print("Employee data added successfully.")
        

    def Update_data(self,emp_id):
        if emp_id in self.emp_dict:
            #print("Update Data")
            new_loc=input("Update location: ")
            self.emp_dict[emp_id]["Location"]=new_loc
        else:
            print("Employee not found!")
        

    def Search(self,emp_id):
        print("In search")
        if emp_id in self.emp_dict:
            print(self.emp_dict[emp_id])
        else:
            print("emp_id not found!")
    def Display(self,emp_id):
        print("In display")
        if emp_id in self.emp_dict:
            print(self.emp_dict[emp_id])
        else:
            print("Employee not found!")

    def Delete(self,emp_id):
        print("In Delete")
        if emp_id in self.emp_dict:
            del self.emp_dict[emp_id]
            print("Data deleted!!")
        else:
            print("Employee not found!")
        

    
obj=EmpData()        
while True:
    print("1.Add data of Employee: ")
    print("2.Update employee data: ")
    print("3.Search employee detail by Id: ")
    print("4.Display Employee data: ")
    print("5.Delete Data: ")
    print("6.Exit")
    choice=int(input("Enter choice which ypu want to perform operation: "))

    if choice==1:
        obj.Add_data()

    elif choice==2:
        
        emp_id=int(input("Enter Emp id which you want update location: "))
        obj.Update_data(emp_id)
            
    elif choice==3:
        emp_id=int(input("Enter Emp id which you want search: "))
        obj.Search(emp_id)

    elif choice==4:
        emp_id=int(input("Enter Emp id which you want Display: "))
        obj.Display(emp_id)

    elif choice==5:
        emp_id=int(input("Enter Emp id which you want Delete: "))
        obj.Delete(emp_id)
        
    elif choice==6:
        break
    else:
        print("Enter valid choice please!!")
        
        
