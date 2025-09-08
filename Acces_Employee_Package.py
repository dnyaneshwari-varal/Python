from Employee_Package import Employee_Details as em

while True:    
    print("1.Store Data: ")
    print("2.Display All employee Data: ")
    print("3.search specific employee with help of ID: ")
    print("4.Update Employee Data: ")
    print("5.Delete Employee Data: ")

    choice=int(input("Enter choice: "))
    if choice==1:
        em.store_data()
    elif choice==2:
        em.display_data()
    elif choice==3:
        emp_id=int(input("Enter Employee ID:"))
        em.search_emp(emp_id)
    elif choice==4:
        emp_id=int(input("Enter Employee ID:"))
        em.update_emp(emp_id)
    elif choice==5:
        emp_id=int(input("Enter Employee ID:"))
        em.delete_emp(emp_id)
    elif choice==6:
        print("Exit")
    else:
        print("Ënter valid choice!!")
    
        
