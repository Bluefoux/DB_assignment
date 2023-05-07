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
    
    def getcompetition():
        sqlclass = sqlting()
        mydb = sqlclass.mydb
        mycursor = sqlclass.createcursor()
        mycursor.execute("SELECT * FROM competition")
        mycompetitions = mycursor.fetchall()
        return mycompetitions
    
    def printstartlist():
        return 0
    
    def printheatlist():
        return 0

    def printresultlist():
        return 0
    
    def printinvoice():
        return 0
    
    def delete():
        return 0
    
    def save():
        return 0
    
    def update():
        return 0
    
    def getevents():
        return 0




