#import sqlclass as sqlting
from sqlclass import sqlting

class athlete:
    def __init__(self, statusid=None, eventid=None, name=None, lastname=None, teamname=None, age=None, registrationtime=None, resulttime=None, id=None):
        self.id = id
        self.statusid = statusid
        self.eventid = eventid
        self.name = name
        self.lastname = lastname
        self.teamname = teamname
        self.age = age
        self.registrationtime = registrationtime
        self.resulttime = resulttime
        #missing gender
    
    def save():
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(athlete.id == 0):
            query = "INSERT INTO ATHLEATS (StatusID, EventID, Name, LastName, TeamName, Age, RegistrationTime, ResultTime)"
            values = (athlete.statusid, athlete.eventid, athlete.name, athlete.lastname, athlete.teamname, athlete.age, athlete.registrationtime, athlete.resulttime)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            athlete.id = sqlclassobj.mycursor.lastrowid
            return athlete.id
        else:
            print("Event already exists, update instead")
            query = "UPDATE ATHLEATS SET StatusID = %s, EventID = %s, Name = %s, LastName = %s, TeamName = %s, Age = %s, RegistrationTime = %s, ResultTime = %s WHERE ID = %s"
            values = (athlete.statusid, athlete.eventid, athlete.name, athlete.lastname, athlete.teamname, athlete.age, athlete.registrationtime, athlete.resulttime, athlete.id)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            return 0
    
    def delete(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        query = "DELETE FROM ATHLEATS WHERE ID = %d"
        value = (self.id)
        sqlclassobj.mycursor.execute(query, value)
        sqlclassobj.mydb.commit()
        sqlclassobj.close()
        return 0

class status:
    def __init__(self, id, statustext):
        self.id = id
        self.statustext = statustext
    
    def save():
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(status.id == 0):
            query = "INSERT INTO STATUS (StatusText)"
            values = (status.statustext)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            status.id = sqlclassobj.mycursor.lastrowid
            return status.id
        else:
            print("Status already exists, update instead")
            query = "UPDATE STATUS SET StatusText = %s WHERE ID = %s"
            values = (status.statustext, status.id)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            return 0
    
    def delete():
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(id == 0):
            print("Status does not exist")
            return 0
        else:
            query = "DELETE FROM STATUS WHERE ID = %s"
            values = (status.id)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                status.id = 0
                return 1
            except:
                print("Could not delete status")
                return 0