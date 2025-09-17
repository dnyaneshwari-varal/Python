#deleting data
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
    
    try:
        book_name=input("Enter book name you want to update: ")
        vprice=int(input("enter price : "))
    except:
        print("Enter valid Book name: ")
    #table.update().set("b_price",vprice).where("b_name"==book_name).execute
    qry=f"UPDATE library_db.book SET b_price = {vprice} WHERE b_name = '{book_name}'"
    print(table.count())
    connection.sql(qry).execute()
    print("Book update")
    print(table.count())
    
    result1=table.select("b_name","b_price").where("b_name='book_name'").execute()
    qry1="SELECT * FROM library_db.book"
    result=connection.sql(qry1).execute()
    lst=result.fetch_all()
    if lst:
        print("Book price not updated ")
    else:
        print("Book price updated")
    print(type(lst)) #list
    print("-------------------------")
    print("ID\t Name \t\t PRICE")
    print("-------------------------")
    for row in lst:
        #print("{0}\t {1}\t {2}".format(row["b_id"],row["b_name"],row["b_price"]))
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
        print("-------------------------")

except Exception as e:
    print("Error: ",e)
finally:
    connection.close()
