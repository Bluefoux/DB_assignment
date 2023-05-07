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
    
    def save(mycursor, mydb):
        if(registration.id == 0):
            query = "INSERT INTO REGISTRATIONS (EventNumber, Name, LastName, Team, Age, RegistrationTime)"
            values = (registration.eventnumber, registration.name, registration.lastname, registration.teamname, registration.age, registration.registrationtime)
            mycursor.execute(query, values)
            mydb.commit()
            registration.id = mycursor.lastrowid
            return registration.id
        else:
            print("Registration already exists, update instead")
            query = "UPDATE REGISTRATIONS SET EventNumber = %s, Name = %s, LastName = %s, Team = %s, Age = %s, RegistrationTime = %s WHERE ID = %s"
            values = (registration.eventnumber, registration.name, registration.lastname, registration.teamname, registration.age, registration.registrationtime, registration.id)
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