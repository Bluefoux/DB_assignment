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
        
    def save(mycursor, mydb):
        if(event.id == 0):
            query = "INSERT INTO EVENT (CompetitionID, RegistrationID, EventNumber, EventName, Dinstance, Gender, MaxAge, QualifyingTime, Relay)"
            values = (event.competitionid, event.registrationid, event.eventnumber, event.eventname, event.distance, event.gender, event.maxage, event.qualifyingtime, event.relay)
            mycursor.execute(query, values)
            mydb.commit()
            event.id = mycursor.lastrowid
            return event.id
        else:
            print("Event already exists, update instead")
            query = "UPDATE EVENT SET CompetitionID = %s, RegistrationID = %s, EventNumber = %s, EventName = %s, Dinstance = %s, Gender = %s, MaxAge = %s, QualifyingTime = %s, Relay = %s WHERE ID = %s"
            values = (event.competitionid, event.registrationid, event.eventnumber, event.eventname, event.distance, event.gender, event.maxage, event.qualifyingtime, event.relay, event.id)
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
    