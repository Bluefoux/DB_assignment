from sqlclass import sqlting

class registration:
    def __init__(self, id=None, competitionid=None, eventnumber=None, name=None, lastname=None, teamname=None, age=None, registrationtime=None):
        self.id = id
        self.competitionid = competitionid
        self.eventnumber = eventnumber
        self.name = name
        self.lastname = lastname
        self.teamname = teamname
        self.age = age
        self.registrationtime = registrationtime
    
    def save(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createcursor()
        if(self.id == 0):
            query = "INSERT INTO REGISTRATIONS (CompetitionID, EventNumber, Name, LastName, Team, Age, RegistrationTime)"
            values = (self.competitionid, self.eventnumber, self.name, self.lastname, self.teamname, self.age, self.registrationtime)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            self.id = sqlclassobj.mycursor.lastrowid
            return self.id
        else:
            print("Registration already exists, update instead")
            query = "UPDATE REGISTRATIONS SET CompetitionID = %s, EventNumber = %s, Name = %s, LastName = %s, Team = %s, Age = %s, RegistrationTime = %s WHERE ID = %s"
            values = (self.competitionid, self.eventnumber, self.name, self.lastname, self.teamname, self.age, self.registrationtime, self.id)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            return 0
    
    def delete():
        return 0
    
    def importregistrationfile():
        """
        LOAD DATA LOCAL INFILE 'E:/Uppgifter/Databas/Competitions.txt' INTO TABLE COMPETITION 
        LINES TERMINATED BY '\r\n'
        (Name, StartDate, EndDate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description);
        """
        return 0
    
