#adding data in database using user input
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
    #taking input
    #adding data in database
    while True:
        id=int(input("Enter ID of user: "))
        name=input("Enter name: ")
        price=int(input("Enter price: "))
        table.insert(["b_id","b_name","b_price"]).values(id,name,price).execute()
        choice=int(input("If you want to add data press 1 else press 0: "))
        if choice==0:
            break


    #table.insert(["b_id","b_name","b_price"]).values(6,"tableu",200).execute()
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

except Exception as e:
    print("Error: ",e)
finally:
    connection.close()
