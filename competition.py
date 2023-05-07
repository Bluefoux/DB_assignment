from sqlclass import sqlting


class competition:
    def __init__(self, id, name, StartDate, Enddate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description, eventlist):
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
    
    def delete(mycursor, mydb):
        if(id == 0):
            print("Competition does not exist")
            return 0
        else:
            competition.deleteallatachments(mycursor, mydb)
            query = "DELETE FROM competition WHERE ID = %s"
            values = (competition.id)
            try:
                mycursor.execute(query, values)
                mydb.commit()
                competition.id = 0
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

    def save(mycursor, mydb):
        if(competition.id == 0):
            query = "INSERT INTO COMPETITION (Name, StartDate, EndDate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description)"
            values = (competition.name, competition.StartDate, competition.Enddate, competition.CompetitionVenue, competition.Organizer, competition.NumberOfLanes, competition.Length, competition.IndividualStartFee, competition.RelayStartFee, competition.Description)
            mycursor.execute(query, values)
            mydb.commit()
            competition.id = mycursor.lastrowid
            return competition.id
        else:
            print("Competition already exists, update instead")
            query = "UPDATE COMPETITION SET Name = %s, StartDate = %s, EndDate = %s, CompetitionVenue = %s, Organizer = %s, NumberOfLanes = %s, Length = %s, IndividualStartFee = %s, RelayStartFee = %s, Description = %s WHERE ID = %s"
            values = (competition.name, competition.StartDate, competition.Enddate, competition.CompetitionVenue, competition.Organizer, competition.NumberOfLanes, competition.Length, competition.IndividualStartFee, competition.RelayStartFee, competition.Description, competition.id)
            mycursor.execute(query, values)
            mydb.commit()
            return 0
    
    def getevents(mycursor):
        query = "SELECT * FROM event WHERE CompetitionID = %s"
        values = (competition.id)
        try:
            mycursor.execute(query, values)
            competition.eventlist = mycursor.fetchall()
            return competition.eventlist
        except:
            print("No events found")
            return 0




