import mysql.connector

class sqlting:

    def __init__(self, mydb, mycursor):
        self.mydb = mydb
        self.mycursor = mycursor
    
    def connect():
        try:
            sqlting.mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="fille2001",
                database="mydb"
            )
            return 1
        except:
            print("Could not connect to database")
            return 0
    
    def createcursor():
        try:
            sqlting.mycursor = sqlting.mydb.cursor(dictionary=True)
            return 1
        except:
            print("Could not create cursor")
            return 0

""" 
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
"""