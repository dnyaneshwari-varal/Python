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
    qry="SELECT *FROM library_db.book"
    result=connection.sql(qry).execute()
    lst=result.fetch_all()

    print("-------------------------")
    print("ID\t Name \t\t PRICE")
    print("-------------------------")

    for row in lst:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
        print("-------------------------")

except Exception as e:
    print("Error: ",e)
finally:
    connection.close()
