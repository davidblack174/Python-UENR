import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    password="admin",
    database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print("Table created successfully")





