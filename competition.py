from sqlclass import sqlting


class competition:
    def __init__(self, name=None, StartDate=None, Enddate=None, CompetitionVenue=None, Organizer=None, NumberOfLanes=None, Length=None, IndividualStartFee=None, RelayStartFee=None, EventList=None ,Description=None, id=None):
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
        self.eventlist = {}
    
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
    
    def printinvoice(self, mycursor, mydb):
        query = "CALL SP_GetInvoice(%s)"
        values = (self.id)
        try:
            mycursor.execute(query, values)
            invoice = mycursor.fetchall()
            for x in invoice: #bara för test
                print(invoice) #ska inte printas, ska returneras
            return invoice
        except:
            print("No competition with that name found")
        return 0
    
    def delete(self, mycursor, mydb):
        if(self.id == 0):
            print("Competition does not exist")
            return 0
        else:
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
            myresult = mycursor.fetchall()
            for x in myresult:
                self.eventlist.append(x)
            return 1
        except:
            print("No events found")
            return 0




