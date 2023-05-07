from sqlclass import sqlting

class registration:
    def __init__(self, id, competitionid, eventnumber, name, lastname, teamname, age, registrationtime):
        self.id = id
        self.competitionid = competitionid
        self.eventnumber = eventnumber
        self.name = name
        self.lastname = lastname
        self.teamname = teamname
        self.age = age
        self.registrationtime = registrationtime
    
    def save(self, mycursor, mydb):
        if(self.id == 0):
            query = "INSERT INTO REGISTRATIONS (CompetitionID, EventNumber, Name, LastName, Team, Age, RegistrationTime)"
            values = (self.competitionid, self.eventnumber, self.name, self.lastname, self.teamname, self.age, self.registrationtime)
            mycursor.execute(query, values)
            mydb.commit()
            self.id = mycursor.lastrowid
            return self.id
        else:
            print("Registration already exists, update instead")
            query = "UPDATE REGISTRATIONS SET CompetitionID = %s, EventNumber = %s, Name = %s, LastName = %s, Team = %s, Age = %s, RegistrationTime = %s WHERE ID = %s"
            values = (self.competitionid, self.eventnumber, self.name, self.lastname, self.teamname, self.age, self.registrationtime, self.id)
            mycursor.execute(query, values)
            mydb.commit()
            return 0
    
    def delete():
        return 0
    
    def importregistrationfile():
        """mysql> LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet
        LINES TERMINATED BY '\r\n';
        """
        
        return 0