import sqlclass as sql


class competition:
    def __init__(self, name=None, StartDate=None, Enddate=None, CompetitionVenue=None, Organizer=None, NumberOfLanes=None, Length=None, IndividualStartFee=None, RelayStartFee=None, Eventdict=None ,Description=None, id=0):
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
        self.eventdict = {}
    
    def getcompetitionid(name):
        query = "SELECT * FROM competition WHERE CompName LIKE %s"
        values = (name)
        try:
            sqlclassobj = sql.sqlting()
            sqlclassobj.connect()
            sqlclassobj.createdictcursor()
            sqlclassobj.mycursor.execute(query, values)
            mycompetitions = sqlclassobj.mycursor.fetchone()
            sqlclassobj.close()
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
            sqlclassobj.createdictcursor()
            sqlclassobj.mycursor.execute(query, values)
            invoice = sqlclassobj.mycursor.fetchall()
            sqlclassobj.close()
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
            sqlclassobj.createdictcursor()
            query = "DELETE FROM competition WHERE ID = %s"
            values = (self.id)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                self.id = 0
                return 1
            except:
                print("Could not delete competition")
                return 0

    def save(self):
        sqlclassobj = sql.sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(self.id == 0):
            queryinsert = "INSERT INTO COMPETITION (ID, CompName, StartDate, EndDate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valuesinsert = (self.id, self.name, self.StartDate, self.Enddate, self.CompetitionVenue, self.Organizer, self.NumberOfLanes, self.Length, self.IndividualStartFee, self.RelayStartFee, self.Description)
            try:
                sqlclassobj.mycursor.execute(queryinsert, valuesinsert)
                sqlclassobj.mydb.commit()
                self.id = sqlclassobj.mycursor.lastrowid
                sqlclassobj.close()
                return 1
            except:
                print("Could not insert competition")
                return 0
        else:
            print("Competition already exists, update instead")
            queryupdate = "UPDATE COMPETITION SET CompName = %s, StartDate = %s, EndDate = %s, CompetitionVenue = %s, Organizer = %s, NumberOfLanes = %s, Length = %s, IndividualStartFee = %s, RelayStartFee = %s, Description = %s WHERE ID = %s"
            valuesupdate = (self.name, self.StartDate, self.Enddate, self.CompetitionVenue, self.Organizer, self.NumberOfLanes, self.Length, self.IndividualStartFee, self.RelayStartFee, self.Description, self.id)
            try:
                sqlclassobj.mycursor.execute(queryupdate, valuesupdate)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                return 0
            except:
                print("Could not update competition")
                return 0
    
    def getevents(self):
        sqlclassobj = sql.sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        query = "SELECT * FROM EVENT WHERE CompetitionID = %s"
        values = (self.id,)
        try:
            sqlclassobj.mycursor.execute(query, values)
            myresult = sqlclassobj.mycursor.fetchall()
            sqlclassobj.close()

            for row in myresult:
                event_id = row['ID']
                event_name = row['EventName']
                # Add the event to the eventdict dictionary
                self.eventdict[event_id] = event_name
            return 1
        except:
            print("No events found")
            sqlclassobj.close()
            return 0




