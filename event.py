#skapa gui

#skriv klart funktioner

#procedur för heatindelning
#börja göra select, hårdkoda competitionid och eventid
#gör sortering på registrationtime

import mysql.connector
from sqlclass import sqlting

class event:
    def __init__(self, id=None, competitionid=None, eventnumber=None, eventname=None, distance=None, gender=None, maxage=None, qualifyingtime=None, relay=None):
        self.id = id
        self.competitionid = competitionid
        self.eventnumber = eventnumber
        self.eventname = eventname
        self.distance = distance
        self.gender = gender
        self.maxage = maxage
        self.qualifyingtime = qualifyingtime
        self.relay = relay
        
    def save(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(self.id == 0):
            try:
                query = "INSERT INTO EVENT (CompetitionID, EventNumber, EventName, Distance, Gender, MaxAge, QualifyingTime, Relay)"
                values = (self.competitionid, self.eventnumber, self.eventname, self.distance, self.gender, self.maxage, self.qualifyingtime, self.relay)
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                self.id = sqlclassobj.mycursor.lastrowid
                sqlclassobj.close()
                return self.id
            except:
                print("Error when inserting event")
                sqlclassobj.close()
                return 0
        else:
            print("Event already exists, update instead")
            try:
                query = "UPDATE EVENT SET CompetitionID = %s, EventNumber = %s, EventName = %s, Distance = %s, Gender = %s, MaxAge = %s, QualifyingTime = %s, Relay = %s WHERE ID = %s"
                values = (self.competitionid, self.eventnumber, self.eventname, self.distance, self.gender, self.maxage, self.qualifyingtime, self.relay, self.id)
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                return 0
            except:
                print("Error when updating event")
                sqlclassobj.close()
                return 0
    
    def delete(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        try:
            query = "DELETE FROM EVENT WHERE CompetitionID = %s, ID = %d"
            value = (self.competitionid, self.id)
            sqlclassobj.mycursor.execute(query, value)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            return 1
        except:
            print("Error when deleting event")
            sqlclassobj.close()
            return 0

    def getathleats():
        return 0
    
    def printstartlist(self):
        if(self.id == 0):
            print("event does not exist")
        return 0
    
    def printheatlist(self):
        if(self.id == 0):
            print("event does not exist") 
        return 0

    def printresultlist(self):
        if(self.id == 0):
            print("event does not exist") 
        return 0
    