import sqlclass as sqlting

class athlete:
    def __init__(self, id, statusid, eventid, name, lastname, teamname, age, registrationtime, resulttime):
        self.id = id
        self.statusid = statusid
        self.eventid = eventid
        self.name = name
        self.lastname = lastname
        self.teamname = teamname
        self.age = age
        self.registrationtime = registrationtime
        self.resulttime = resulttime
    
    def save():
        return 0
    def delete():
        return 0
    def update():
        return 0
    
class status:
    def __init__(self, id, statustext):
        self.id = id
        self.statustext = statustext
    
    def save():
        return 0
    def delete():
        return 0
    def update():
        return 0