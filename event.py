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
    
    def save():
        mysqlclass = sqlting()
        mydb = mysqlclass.connect()
        mycursor = mysqlclass.createcursor()
        querry = "INSERT INTO EVENT (CompetitionID, RegistrationID, EventNumber, EventName, Dinstance, Gender, MagAge, QualifyingTime, Relay)"
        values = (event.competitionid, event.registrationid, event.eventnumber, event.eventname, event.distance, event.gender, event.maxage, event.qualifyingtime, event.relay)
        return  #add execution of querry
    
    def delete():
        return 0
    
    def update():
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
    