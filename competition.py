import sqlclass as sql


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
        self.eventlist = EventList
    
    def getcompetitionid(name):
        query = "SELECT * FROM competition WHERE Name LIKE %s"
        values = (name)
        try:
            sqlclassobj = sql.sqlting()
            sqlclassobj.connect()
            sqlclassobj.createcursor()
            sqlclassobj.mycursor.execute(query, values)
            mycompetitions = sqlclassobj.mycursor.fetchone()
            id = mycompetitions["ID"]
            return id
        except:
            print("No competition with that name found")
            return 0
    
    def printinvoice(self):
        query = "CALL SP_GetInvoice(%s)"
        values = (self.id)
        try:
            sqlclassobj = sql.sqlting()
            sqlclassobj.connect()
            sqlclassobj.createcursor()
            sqlclassobj.mycursor.execute(query, values)
            invoice = sqlclassobj.mycursor.fetchall()
            for x in invoice: #bara för test
                print(invoice) #ska inte printas, ska returneras
            return invoice
        except:
            print("No competition with that name found")
        return 0
    
    def delete(self):
        if(self.id == 0):
            print("Competition does not exist")
            return 0
        else:
            sqlclassobj = sql.sqlting()
            sqlclassobj.connect()
            sqlclassobj.createcursor()
            query = "DELETE FROM competition WHERE ID = %s"
            values = (self.id)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                self.id = 0
                return 1
            except:
                print("Could not delete competition")
                return 0

    def save(self):
        sqlclassobj = sql.sqlting()
        sqlclassobj.connect()
        sqlclassobj.createcursor()
        if(self.id == 0):
            query = "INSERT INTO COMPETITION (Name, StartDate, EndDate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description)"
            values = (self.name, self.StartDate, self.Enddate, self.CompetitionVenue, self.Organizer, self.NumberOfLanes, self.Length, self.IndividualStartFee, self.RelayStartFee, self.Description)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            self.id = sqlclassobj.mycursor.lastrowid
            return self.id
        else:
            print("Competition already exists, update instead")
            query = "UPDATE COMPETITION SET Name = %s, StartDate = %s, EndDate = %s, CompetitionVenue = %s, Organizer = %s, NumberOfLanes = %s, Length = %s, IndividualStartFee = %s, RelayStartFee = %s, Description = %s WHERE ID = %s"
            values = (self.name, self.StartDate, self.Enddate, self.CompetitionVenue, self.Organizer, self.NumberOfLanes, self.Length, self.IndividualStartFee, self.RelayStartFee, self.Description, self.id)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            return 0
    
    def getevents(self):
        sqlclassobj = sql.sqlting()
        sqlclassobj.connect()
        sqlclassobj.createcursor()
        query = "SELECT * FROM EVENT WHERE CompetitionID = %s"
        values = (self.id,)
        print(self.id)
        #try:
        sqlclassobj.mycursor.execute(query, values)
        myresult = sqlclassobj.mycursor.fetchall()
        for row in myresult:
            event_id = row['ID']
            event_name = row['EventName']
            # Add the event to the eventlist dictionary
            self.eventlist[event_id] = event_name
        return 1
        #except:
        #    print("No events found")
        #    return 0




