import mysql.connector

class sqlting:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect():
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="fille2001",
            database="mydb"
        )
        return mydb
    
    def createcursor():
        mycursor = mydb.cursor(dictionary=True)
        return mycursor
    
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="fille2001",
    database="mydb"
)
mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
except:
    print("Table already exists")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)