emp={}  
def store_data():
    
    while True:
        
        ID=int(input("Enter ID of employee: "))
        name=input("Enter Name of Employee: ")
        dep=input("Enter Department name: ")
        sal=int(input("Enter Salary: "))

        emp[ID]={"Name":name,"Department":dep,"Salary":sal}
        ch=int(input("want to add anothe emp data? if yes=1 no=0"))
        if ch ==0:
            break
    

def display_data():
    print(emp)    

def search_emp(emp_id):

    if emp_id in emp:
        print(emp[emp_id])
    else:
        print("User not Found!!")
            
def update_emp(emp_id):
    if emp_id in emp:    
        emp[emp_id]["Salary"]+=2000
        print(emp[emp_id])
  
    else:
        print("user not found!!")

def delete_emp(emp_id):
    if emp_id in emp:
        del emp[emp_id]
        print("Deleted succesfully!!!")
   
    else:
        print("user not found!!")
        
        
    
