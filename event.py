#skapa gui

#skriv klart funktioner

#procedur för heatindelning
#börja göra select, hårdkoda competitionid och eventid
#gör sortering på registrationtime

import mysql.connector
from sqlclass import sqlting

class event:
    def __init__(self, id, competitionid, eventnumber, eventname, distance, gender, maxage, qualifyingtime, relay):
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
            query = "INSERT INTO EVENT (CompetitionID, EventNumber, EventName, Distance, Gender, MaxAge, QualifyingTime, Relay)"
            values = (self.competitionid, self.eventnumber, self.eventname, self.distance, self.gender, self.maxage, self.qualifyingtime, self.relay)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            self.id = sqlclassobj.mycursor.lastrowid
            sqlclassobj.close()
            return self.id
        else:
            print("Event already exists, update instead")
            query = "UPDATE EVENT SET CompetitionID = %s, EventNumber = %s, EventName = %s, Distance = %s, Gender = %s, MaxAge = %s, QualifyingTime = %s, Relay = %s WHERE ID = %s"
            values = (self.competitionid, self.eventnumber, self.eventname, self.distance, self.gender, self.maxage, self.qualifyingtime, self.relay, self.id)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            return 0
    
    def delete(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        query = "DELETE FROM EVENT WHERE CompetitionID = %s, ID = %d"
        value = (self.competitionid, self.id)
        sqlclassobj.mycursor.execute(query, value)
        sqlclassobj.mydb.commit()
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
    