from sqlclass import sqlting
import mysql.connector

class event:
    def __init__(self, id, competitionid, registrationid, eventnumber, eventname, distance, gender, maxage, qualifyingtime, relay):
        self.id = id
        self.competitionid = competitionid
        self.registrationid = registrationid
        self.eventnumber = eventnumber
        self.eventname = eventname
        self.distance = distance
        self.gender = gender
        self.maxage = maxage
        self.qualifyingtime = qualifyingtime
        self.relay = relay
        
    def save(self, mycursor, mydb):
        if(self.id == 0):
            query = "INSERT INTO EVENT (CompetitionID, RegistrationID, EventNumber, EventName, Distance, Gender, MaxAge, QualifyingTime, Relay)"
            values = (self.competitionid, self.registrationid, self.eventnumber, self.eventname, self.distance, self.gender, self.maxage, self.qualifyingtime, self.relay)
            mycursor.execute(query, values)
            mydb.commit()
            self.id = mycursor.lastrowid
            return self.id
        else:
            print("Event already exists, update instead")
            query = "UPDATE EVENT SET CompetitionID = %s, RegistrationID = %s, EventNumber = %s, EventName = %s, Distance = %s, Gender = %s, MaxAge = %s, QualifyingTime = %s, Relay = %s WHERE ID = %s"
            values = (self.competitionid, self.registrationid, self.eventnumber, self.eventname, self.distance, self.gender, self.maxage, self.qualifyingtime, self.relay, self.id)
            mycursor.execute(query, values)
            mydb.commit()
            return 0
    
    def delete():
        return 0
    
    def getathleats():
        return 0
    
    def generateheatlist():
        return 0
    
    def printheatlist():
        return 0

    def printstartlist():
        return 0
    
    def printresultlist():
        return 0
    