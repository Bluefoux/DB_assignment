import mysql.connector

class sqlting:

    def __init__(self=None, mydb=None, mycursor=None):
        self.mydb = mydb
        self.mycursor = mycursor
    
    def connect(self):
        try:
            self.mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="fille2001",
                database="mydb",
                charset="utf8mb4"
            )
            return 1
        except:
            print("Could not connect to database")
            return 0
    
    def createdictcursor(self):
        try:
            self.mycursor = self.mydb.cursor(dictionary=True)
            return 1
        except:
            print("Could not create cursor")
            return 0
        
    def check_forweirdletters(self):
        thisissql = sqlting()
        thisissql.connect()
        thisissql.createdictcursor()
        query = """
            SELECT COLUMN_NAME, CHARACTER_SET_NAME, COLLATION_NAME
            FROM information_schema.columns
            WHERE TABLE_SCHEMA = 'mydb'  -- Replace with your database name
                AND TABLE_NAME = 'COMPETITION'  -- Replace with your table name
                AND COLUMN_NAME = 'CompName'  -- Replace with your column name
        """
        thisissql.mycursor.execute(query)
        result = thisissql.mycursor.fetchone()
        if result:
            column_name, character_set_name, collation_name = result
            print(f"Column: {column_name}")
            print(f"Character Set: {character_set_name}")
            print(f"Collation: {collation_name}")
        else:
            print("Column not found.")
        thisissql.mycursor.close()
        thisissql.mydb.close()
        return 1
    
    def close(self):
        try:
            self.mycursor.close()
            self.mydb.close()
            return 1
        except:
            print("Could not close cursor or database")
            return 0


#if __name__ == '__main__':
#    ting = sqlting()
#    con = ting.connect()
#    mycursor = ting.createdictcursor()
 #   ting.mycursor.execute("LOAD DATA LOCAL INFILE 'E:/Uppgifter/Databas/Competitions.txt' INTO TABLE COMPETITION LINES TERMINATED BY '\r\n'")
#    ting.mydb.commit()
#    ting.mydb.close()

"""
        LOAD DATA LOCAL INFILE 'E:/Uppgifter/Databas/Competitions.txt' INTO TABLE COMPETITION LINES TERMINATED BY '\r\n';
"""

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