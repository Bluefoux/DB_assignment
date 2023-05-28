#import sqlclass as sqlting
from sqlclass import sqlting
import tkinter as tk

class athlete:
    def __init__(self, statusid=None, eventid=None, name=None, lastname=None, teamname=None, gender=None, age=None, registrationtime=None, resulttime=None, id=0):
        self.id = id
        self.statusid = statusid
        self.eventid = eventid
        self.name = name
        self.lastname = lastname
        self.teamname = teamname
        self.age = age
        self.registrationtime = registrationtime
        self.resulttime = resulttime
        self.gender = gender
    
    def save(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(self.id == 0):
            query = "INSERT INTO ATHLEATS (ID, StatusID, EventID, AthleatName, LastName, TeamName, Gender, Age, RegistrationTime, ResultTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.id, self.statusid, self.eventid, self.name, self.lastname, self.teamname, self.gender, self.age, self.registrationtime, self.resulttime)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                self.id = sqlclassobj.mycursor.lastrowid
                return self.id
            except:
                print("Error in saving athleat")
                sqlclassobj.close()
                return 0
        else:
            print("Event already exists, update instead")
            query = "UPDATE ATHLEATS SET StatusID = %s, EventID = %s, AthleatName = %s, LastName = %s, TeamName = %s, Gender = %s, Age = %s, RegistrationTime = %s, ResultTime = %s WHERE ID = %s"
            values = (self.statusid, self.eventid, self.name, self.lastname, self.teamname, self.gender, self.age, self.registrationtime, self.resulttime, self.id)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                return 0
            except:
                print("Error in updating athleat")
                sqlclassobj.close()
                return 0
    
    def delete(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        query = "DELETE FROM ATHLEATS WHERE ID = %d"
        value = (self.id)
        try:
            sqlclassobj.mycursor.execute(query, value)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            return 0
        except:
            print("Error in deleting athleat")
            sqlclassobj.close()
            return 0

class status:
    def __init__(self, id, statustext):
        self.id = id
        self.statustext = statustext
    
    def save(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(self.id == 0):
            query = "INSERT INTO STATUS (StatusText)"
            values = (self.statustext)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                self.id = sqlclassobj.mycursor.lastrowid
                return self.id
            except:
                print("Error in saving status")
                sqlclassobj.close()
                return 0
        else:
            print("Status already exists, update instead")
            query = "UPDATE STATUS SET StatusText = %s WHERE ID = %s"
            values = (self.statustext, self.id)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                return 0
            except:
                print("Error in updating status")
                sqlclassobj.close()
                return 0
    
    def delete(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(id == 0):
            print("Status does not exist")
            return 0
        else:
            query = "DELETE FROM STATUS WHERE ID = %s"
            values = (self.id)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                self.id = 0
                return 1
            except:
                print("Could not delete status")
                sqlclassobj.close()
                return 0