from sqlclass import sqlting

class registration:
    def __init__(self, id=0, competitionid=None, eventnumber=None, name=None, lastname=None, teamname=None, age=None, registrationtime=None):
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
        sqlclassobj.createdictcursor()
        if(self.id == 0):
            query = "INSERT INTO REGISTRATIONS (ID, CompetitionID, EventNumber, RegName, LastName, Team, Age, RegistrationTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.id, self.competitionid, self.eventnumber, self.name, self.lastname, self.teamname, self.age, self.registrationtime)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                self.id = sqlclassobj.mycursor.lastrowid
                sqlclassobj.close()
                return 1
            except:
                print("Could not insert registration")
                return 0
        else:
            print("Registration already exists, update instead")
            query = "UPDATE REGISTRATIONS SET CompetitionID = %s, EventNumber = %s, RegName = %s, LastName = %s, Team = %s, Age = %s, RegistrationTime = %s WHERE ID = %s"
            values = (self.competitionid, self.eventnumber, self.name, self.lastname, self.teamname, self.age, self.registrationtime, self.id)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                return 0
            except:
                print("Could not update registration")
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
    
