import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sachin5031",
    database="dummy"
)
# print(mydb)

mycursor=mydb.cursor()

# mycursor.execute("CREATE DATABASE Pythonprogramming")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE employee(name VARCHAR(255),address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

mycursor.execute("SELECT * FROM employee")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

# myresult=mycursor.fetchone()
# print(myresult)
