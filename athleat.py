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
    
    def save(mycursor, mydb):
        if(athlete.id == 0):
            query = "INSERT INTO ATHLEATS (StatusID, EventID, Name, LastName, TeamName, Age, RegistrationTime, ResultTime)"
            values = (athlete.statusid, athlete.eventid, athlete.name, athlete.lastname, athlete.teamname, athlete.age, athlete.registrationtime, athlete.resulttime)
            mycursor.execute(query, values)
            mydb.commit()
            athlete.id = mycursor.lastrowid
            return athlete.id
        else:
            print("Event already exists, update instead")
            query = "UPDATE ATHLEATS SET StatusID = %s, EventID = %s, Name = %s, LastName = %s, TeamName = %s, Age = %s, RegistrationTime = %s, ResultTime = %s WHERE ID = %s"
            values = (athlete.statusid, athlete.eventid, athlete.name, athlete.lastname, athlete.teamname, athlete.age, athlete.registrationtime, athlete.resulttime, athlete.id)
            mycursor.execute(query, values)
            mydb.commit()
            return 0
    
    def delete(self, mycursor, mydb):
        query = "DELETE FROM ATHLEATS WHERE ID = %d"
        value = (self.id)
        mycursor.execute(query, value)
        mydb.commit()
        return 0

class status:
    def __init__(self, id, statustext):
        self.id = id
        self.statustext = statustext
    
    def save(mycursor, mydb):
        if(status.id == 0):
            query = "INSERT INTO STATUS (StatusText)"
            values = (status.statustext)
            mycursor.execute(query, values)
            mydb.commit()
            status.id = mycursor.lastrowid
            return status.id
        else:
            print("Status already exists, update instead")
            query = "UPDATE STATUS SET StatusText = %s WHERE ID = %s"
            values = (status.statustext, status.id)
            mycursor.execute(query, values)
            mydb.commit()
            return 0
    
    def delete(mycursor, mydb):
        if(id == 0):
            print("Status does not exist")
            return 0
        else:
            query = "DELETE FROM STATUS WHERE ID = %s"
            values = (status.id)
            try:
                mycursor.execute(query, values)
                mydb.commit()
                status.id = 0
                return 1
            except:
                print("Could not delete status")
                return 0