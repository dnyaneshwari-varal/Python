#menu driven
import mysqlx

def insert_stud(table):
    s_id=int(input("Enter student id: "))
    s_name=input("Enter student name: ")
    s_price=int(input("Enter student price: "))
    table.insert(["id","name","price",]).values(s_id,s_name,s_price).execute()
    print("Student inserted successfully! \n")
    
def del_stud(connection):
    s_id=int(input("Enter student id to delete: "))
    qry = f"delete from stud_info.data where id={s_id}"
    connection.sql(qry).execute()
    print(f"student with id {s_id} deleted!")

def update_stud(connection):
    s_id=int(input("Enter student id to Update: "))
    new_name=input("Enter new student name: ")
    new_price=int(input("Enter new price: "))
    #qry=f"update library.book set b_name = '{new_name}', b_price={new_price}, WHERE b_id = {b_id}"
    qry = f"UPDATE stud_info.data SET s_name = '{new_name}', s_price = {new_price} WHERE id = {s_id}"
    connection.sql(qry).execute()
    print(f"student with id {s_id} updated successfully!")

def search_stud(connection):
    s_id=int(input("Enter student id to update: "))
    qry=f"select * from stud_info.data where id = {s_id}"
    result=connection.sql(qry).execute()
    row = result.fetch_one()
    if row:
        print("-"*50)
        print("ID \tName \tPrice ")
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
        print("-"*50)

    else:
        print("student not found!")

def display_stud(connection):
    qry="select * from stud_info.data"
    result=connection.sql(qry).execute()
    lst=result.fetch_all()
    if lst:
        print("-"*50)
        print("ID \tName \tPrice ")
        print("-"*50)
        for row in lst:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")

        print("-"*50)

    else:
        print("No record found in Data!")


try:
    connection = mysqlx.get_session({
        "host": "localhost",
        "port": 33060,  
        "user": "root",
        "password": "varal"
    })
    schema=connection.get_schema("stud_info")
    table=schema.get_table("data")

    while True:
        print("Menu")
        print("1. Insert Student")
        print("2. Delete Student")
        print("3. Update Student data")
        print("4. Search Student")
        print("5. Display all Student data")
        print("6. Exit")

        choice=int(input("Enter your choice: "))

        if choice==1:
            insert_stud(table)
        elif choice==2:
            del_stud(connection)
        elif choice==3:
            update_stud(connection)
        elif choice==4:
            search_stud(connection)
        elif choice==5:
            display_stud(connection)
        elif choice==6:
            print("Exited!")
            break

        else:
            print("Enter correct choice!")

except Exception as e:
    print("Error",e)
finally:
    connection.close()
