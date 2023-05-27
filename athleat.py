#import sqlclass as sqlting
from sqlclass import sqlting
import tkinter as tk

class athlete:
    def __init__(self, statusid=None, eventid=None, name=None, lastname=None, teamname=None, gender=None, age=None, registrationtime=None, resulttime=None, id=None):
        self.id = id
        self.statusid = statusid
        self.eventid = eventid
        self.name = name
        self.lastname = lastname
        self.teamname = teamname
        self.age = age
        self.registrationtime = registrationtime
        self.resulttime = resulttime
        self.gender = gender
    
    def save(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(self.id == 0):
            query = "INSERT INTO ATHLEATS (StatusID, EventID, Name, LastName, TeamName, Gender, Age, Heat, Lane, RegistrationTime, ResultTime)"
            values = (self.statusid, self.eventid, self.name, self.lastname, self.teamname, self.age, self.registrationtime, self.resulttime)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            self.id = sqlclassobj.mycursor.lastrowid
            return self.id
        else:
            print("Event already exists, update instead")
            query = "UPDATE ATHLEATS SET StatusID = %s, EventID = %s, Name = %s, LastName = %s, TeamName = %s, Age = %s, RegistrationTime = %s, ResultTime = %s WHERE ID = %s"
            values = (self.statusid, self.eventid, self.name, self.lastname, self.teamname, self.age, self.registrationtime, self.resulttime, self.id)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            return 0
    
    def delete(self):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        query = "DELETE FROM ATHLEATS WHERE ID = %d"
        value = (self.id)
        sqlclassobj.mycursor.execute(query, value)
        sqlclassobj.mydb.commit()
        sqlclassobj.close()
        return 0
    
    def choosefilebutton_clicked(mylst):
        #open file dialog (utforskaren) and choose file
        print("Choose file button was clicked!")

    def saveathleatbutton_clicked(mylst):
        print("Save button was clicked!")

    def addathleatbuttonclick(eventobj):
        mytup = ("Name", "Last Name", "Team", "Gender", "Age", "Heat", "Lane", "Registration Time")
        mylst = []
        athleatwind = tk.Tk()
        athleatwind.title("Add Athleat")
        
        automaticadd = tk.Label(athleatwind, width=20, fg='blue', text = "Automatic add athleats", relief="ridge", anchor="w")
        automaticadd.grid(row=0, column=0)

        choosefilebutton = tk.Button(athleatwind, text="Choose file", command= lambda: athlete.choosefilebutton_clicked(mylst))
        choosefilebutton.grid(row=1, column=0)

        myfilentry = tk.Entry(athleatwind, bd = 5, width=40)
        myfilentry.grid(row=1, column=1)

        savebutton = tk.Button(athleatwind, text="Save", command= lambda: athlete.saveathleatbutton_clicked(mylst))
        savebutton.grid(row=2, column=1)

        automaticadd = tk.Label(athleatwind, width=20, fg='blue', text = "Add athleats manually", relief="ridge", anchor="w")
        automaticadd.grid(row=4, column=0)
        
        i=5
        for x in mytup:
            e = tk.Label(athleatwind, width=20, fg='blue', text = x, relief="ridge", anchor="w")
            e.grid(row=i, column=0)
            myentry = tk.Entry(athleatwind, bd = 5)
            myentry.grid(row=i, column=1)
            mylst.append(myentry)
            i += 1
        
        #e = tk.Label(athleatwind, width=20, fg='blue', text = "Description", relief="ridge", anchor="w")
        #e.grid(row=10, column=0)
        #description = tk.Entry(athleatwind, bd = 5)
        #description.grid(row=10, column=1)
        saveathleatbutton = tk.Button(athleatwind, text="Save", command= lambda: athlete.saveathleatbutton_clicked(mylst))
        saveathleatbutton.grid(row=i, column=1)
        athleatwind.mainloop()
        print("Add athleat to event!")

    """def saveathleatsbutton_clicked(mylst, description):
        compname = comp.competition(mylst[0].get(), mylst[1].get(), mylst[2].get(), mylst[3].get(), mylst[4].get(), mylst[5].get(), mylst[6].get(), mylst[7].get(), mylst[8].get(), description.get())
        #compname.save(mycursor, db) #uncomment this when change is wanted in database
        print("Save button was clicked!")
    
    def Create_comp_button_clicked():
        create_compwind = tk.Tk()
        mytup = ("Name", "Start Date", "End Date", "Venue", "Organizer", "Number of lanes", "Pool length", "Individual fee", "Relay fee")
        mylst = []
        i=1
        for x in mytup:
            e = tk.Label(create_compwind, width=20, fg='blue', text = x, relief="ridge", anchor="w")
            e.grid(row=i, column=0)
            myentry = tk.Entry(create_compwind, bd = 5)
            myentry.grid(row=i, column=1)
            mylst.append(myentry)
            i += 1
        
        e = tk.Label(create_compwind, width=20, fg='blue', text = "Description", relief="ridge", anchor="w")
        e.grid(row=10, column=0)
        description = tk.Entry(create_compwind, bd = 5)
        description.grid(row=10, column=1)
        savecompbutton = tk.Button(create_compwind, text="Save", command= lambda: guiclass.savecompbutton_clicked(mylst, description))
        savecompbutton.grid(row=11, column=1)
        create_compwind.mainloop()
        print("Button was clicked!")"""

class status:
    def __init__(self, id, statustext):
        self.id = id
        self.statustext = statustext
    
    def save():
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(status.id == 0):
            query = "INSERT INTO STATUS (StatusText)"
            values = (status.statustext)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            status.id = sqlclassobj.mycursor.lastrowid
            return status.id
        else:
            print("Status already exists, update instead")
            query = "UPDATE STATUS SET StatusText = %s WHERE ID = %s"
            values = (status.statustext, status.id)
            sqlclassobj.mycursor.execute(query, values)
            sqlclassobj.mydb.commit()
            sqlclassobj.close()
            return 0
    
    def delete():
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        if(id == 0):
            print("Status does not exist")
            return 0
        else:
            query = "DELETE FROM STATUS WHERE ID = %s"
            values = (status.id)
            try:
                sqlclassobj.mycursor.execute(query, values)
                sqlclassobj.mydb.commit()
                sqlclassobj.close()
                status.id = 0
                return 1
            except:
                print("Could not delete status")
                return 0