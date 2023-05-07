from sqlclass import sqlting


class competition:
    def __init__(self=None, id=None, name=None, StartDate=None, Enddate=None, CompetitionVenue=None, Organizer=None, NumberOfLanes=None, Length=None, IndividualStartFee=None, RelayStartFee=None, Description=None, eventlist=None):
        self.id = id
        self.name = name
        self.StartDate = StartDate
        self.Enddate = Enddate
        self.CompetitionVenue = CompetitionVenue
        self.Organizer = Organizer
        self.NumberOfLanes = NumberOfLanes
        self.Length = Length
        self.IndividualStartFee = IndividualStartFee
        self.RelayStartFee = RelayStartFee
        self.Description = Description
        self.eventlist = eventlist
    
    def getcompetitionid(name, mycursor):
        query = "SELECT * FROM competition WHERE Name LIKE %s"
        values = (name)
        try:
            mycursor.execute(query, values)
            mycompetitions = mycursor.fetchone()
            id = mycompetitions["ID"]
            return id
        except:
            print("No competition with that name found")
            return 0
    
    def printstartlist():
        return 0
    
    def printheatlist():
        return 0

    def printresultlist():
        return 0
    
    def printinvoice():
        return 0
    
    def delete(self, mycursor, mydb):
        if(id == 0):
            print("Competition does not exist")
            return 0
        else:
            self.deleteallatachments(mycursor, mydb)
            query = "DELETE FROM competition WHERE ID = %s"
            values = (self.id)
            try:
                mycursor.execute(query, values)
                mydb.commit()
                self.id = 0
                return 1
            except:
                print("Could not delete competition")
                return 0
    
    
    def deleteallattachments(mycursor, mydb):
        #query = "DELETE FROM REGISTRATION WHERE CompetitionID = %s"
        #querry = "DELETE FROM event WHERE CompetitionID = %s"
        #values = (competition.id)
        return 0

    #def deleteevent(eventid, mycursor, mydb):

    def save(self, mycursor, mydb):
        if(self.id == 0):
            query = "INSERT INTO COMPETITION (Name, StartDate, EndDate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description)"
            values = (self.name, self.StartDate, self.Enddate, self.CompetitionVenue, self.Organizer, self.NumberOfLanes, self.Length, self.IndividualStartFee, self.RelayStartFee, self.Description)
            mycursor.execute(query, values)
            mydb.commit()
            self.id = mycursor.lastrowid
            return self.id
        else:
            print("Competition already exists, update instead")
            query = "UPDATE COMPETITION SET Name = %s, StartDate = %s, EndDate = %s, CompetitionVenue = %s, Organizer = %s, NumberOfLanes = %s, Length = %s, IndividualStartFee = %s, RelayStartFee = %s, Description = %s WHERE ID = %s"
            values = (self.name, self.StartDate, self.Enddate, self.CompetitionVenue, self.Organizer, self.NumberOfLanes, self.Length, self.IndividualStartFee, self.RelayStartFee, self.Description, self.id)
            mycursor.execute(query, values)
            mydb.commit()
            return 0
    
    def getevents(self, mycursor):
        query = "SELECT * FROM event WHERE CompetitionID = %s"
        values = (self.id)
        try:
            mycursor.execute(query, values)
            self.eventlist = mycursor.fetchall()
            return self.eventlist
        except:
            print("No events found")
            return 0




