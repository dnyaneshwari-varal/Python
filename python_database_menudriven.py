import mysqlx


try:
    connection=mysqlx.get_session({
        "host":"localhost",
        "port":33060,
        "user":"root",
        "password":"varal"})
    print("Successfully connection done!")

    schema=connection.get_schema("library_db")
    table=schema.get_table("book")

    def add_data():
        while True:
            id=int(input("Enter ID of user: "))
            name=input("Enter name: ")
            price=int(input("Enter price: "))
            table.insert(["b_id","b_name","b_price"]).values(id,name,price).execute()
            choice=int(input("If you want to add data press 1 else press 0: "))
            if choice==0:
                break
        qry="SELECT *FROM library_db.book"
        result=connection.sql(qry).execute()

    def display():
        qry="SELECT *FROM library_db.book"
        result=connection.sql(qry).execute()
        print(type(result))
        lst=result.fetch_all()
        print(type(lst)) #list
        print("-------------------------")
        print("ID\t Name \t\t PRICE")
        print("-------------------------")

        for row in lst:
            #print("{0}\t {1}\t {2}".format(row["b_id"],row["b_name"],row["b_price"]))
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
            print("-------------------------")

    def update():
        
        book_name=input("Enter book name you want to update: ")
        vprice=int(input("enter price : "))
       
        #table.update().set("b_price",vprice).where("b_name"==book_name).execute
        qry=f"UPDATE library_db.book SET b_price = {vprice} WHERE b_name = '{book_name}'"
        
        connection.sql(qry).execute()
        print("Book update")
    
    
        result1=table.select("b_name","b_price").where("b_name='book_name'").execute()
        qry1="SELECT * FROM library_db.book"
        result=connection.sql(qry1).execute()
        lst=result.fetch_all()
        if book_name in lst:
            print("found!")
        else:
            print("Not found!")
        if lst:
            print("Book price not updated ")
        else:
            print("Book price updated")
    def delete():
        
        book_name=input("Enter book name ypu want to delete: ")
        
        qry=f"delete from library_db.book where b_name='{book_name}'"
        #print(table.count())
        connection.sql(qry).execute()
    
        #print(table.count())
    
        result1=table.select("b_name","b_price").where("b_name='book_name'").execute()
        qry1="SELECT * FROM library_db.book"
        result=connection.sql(qry1).execute()
        lst=result.fetch_all()
        if book_name in lst:
            print("found!")
        else:
            print("Not found!")
        

    def search():
        book_name=input("Enter book name you want to search: ")
    
        
        qry = f"SELECT b_id, b_name, b_price FROM library_db.book WHERE b_name = '{book_name}'"
    
        result=connection.sql(qry).execute()
        lst=result.fetch_all()
        
        if lst:
            for row in lst:
                print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
        else:
            print("Book not found ")
        

        
    
    while True:
        #print("1.create database")
        print("1.Add data")
        print("2.Display/Read")
        print("3.update data")
        print("4.Delete Data")
        print("5.Search")
        print("6.Exit")

        ch=int(input("Enter what you want to do: "))
        if ch==1:
            add_data()
        elif ch==2:
            display()
        elif ch==3:
            update()
        elif ch==4:
            delete()
        elif ch==5:
            search()
        elif ch==6:
            break
        else:
            print("Enter valid choice!!")

        
        



except Exception as e:
    print("Error: ",e)
finally:
    connection.close()






        
    
