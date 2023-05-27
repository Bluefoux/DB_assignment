import tkinter as tk
from sqlclass import sqlting
from athleat import athlete
import event as event

class startlstclass:

    def startlstbutton_clicked(eventobj):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        query = "SELECT Name, Lastname, TeamName, RegistrationTime FROM ATHLEATS INNER JOIN EVENT ON ATHLEATS.EventID = EVENT.ID AND EVENT.CompetitionID = %s AND ATHLEATS.EventID = %s ORDER BY RegistrationTime ASC"
        values = (eventobj.competitionid, eventobj.id)
        print(values)
        try:
            sqlclassobj.mycursor.execute(query, values)
            startlst = sqlclassobj.mycursor.fetchall()
        except:
            print("Error: Could not fetch data")
        sqlclassobj.close()

        startwindow = tk.Tk()
        startwindow.title("Start list")

        addeventbutton = tk.Button(startwindow, text="Add athleat", command= lambda: startlstclass.addathleatbutton_click(eventobj))
        addeventbutton.grid(row=0, column=0)

        i = 1
        for x in startlst:
            y = 0
            if i==1:
                for k in x.keys():
                    e = tk.Label(startwindow, width=20, text = k, relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                    y += 1
                i += 1
                y = 0
            for key, value in x.items():
                e = tk.Label(startwindow, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
            i += 1
        startwindow.mainloop()
        print("Show start list!")

    def heatlstbutton_clicked(eventobj):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        
        query = "SELECT Name, Lastname, TeamName, Heat, Lane, RegistrationTime FROM ATHLEATS INNER JOIN EVENT ON ATHLEATS.EventID = EVENT.ID AND EVENT.CompetitionID = %s AND ATHLEATS.EventID = %s ORDER BY Heat, Lane ASC"
        values = (eventobj.competitionid, eventobj.id)
        print(values)
        try:
            sqlclassobj.mycursor.execute(query, values)
            startlst = sqlclassobj.mycursor.fetchall()
        except:
            print("Error: Could not fetch data")
        sqlclassobj.close()

        heatwindow = tk.Tk()
        heatwindow.title("Heat list")  

        i = 1
        for x in startlst:
            y = 0
            if i==1:
                for k in x.keys():
                    e = tk.Label(heatwindow, width=20, text = k, relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                    y += 1
                i += 1
                y = 0
            for key, value in x.items():
                e = tk.Label(heatwindow, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
            i += 1
        heatwindow.mainloop()
        print("Show start list!")

    def choosefilebutton_clicked(mylst): #fix this in the future
        #open file dialog (utforskaren) and choose file
        print("Choose file button was clicked!")

    def saveathleatbutton_clicked(mylst):
        athobj = athlete(name=mylst[0].get(), lastname=mylst[1].get(), teamname=mylst[2].get(), gender=mylst[3].get(), age=mylst[4].get(), registrationtime=mylst[5].get())
        #athobj.save() #uncomment this when change is wanted in database
        print("Save button was clicked!") #return athobj?

    def savefromfilebutton_clicked(mylst): #fix this in the future
        print("Save from file button was clicked!")

    def addathleatbutton_click(eventobj):
        mytup = ("Name", "Last Name", "Team", "Gender", "Age", "Registration Time")
        mylst = []
        athleatwind = tk.Tk()
        athleatwind.title("Add Athleat")

        automaticadd = tk.Label(athleatwind, width=20, text = "Automatic add athleats", relief="ridge", anchor="w")
        automaticadd.grid(row=0, column=0)

        choosefilebutton = tk.Button(athleatwind, text="Choose file", command= lambda: startlstclass.choosefilebutton_clicked(mylst))
        choosefilebutton.grid(row=1, column=0)

        myfilentry = tk.Entry(athleatwind, bd = 5, width=50)
        myfilentry.grid(row=1, column=1)

        savebutton = tk.Button(athleatwind, text="Save", command= lambda: startlstclass.savefromfilebutton_clicked(mylst))
        savebutton.grid(row=2, column=1)

        automaticadd = tk.Label(athleatwind, width=20, text = "Add athleats manually", relief="ridge", anchor="w")
        automaticadd.grid(row=4, column=0)
        
        i=5
        for x in mytup:
            e = tk.Label(athleatwind, width=20, text = x, relief="ridge", anchor="w")
            e.grid(row=i, column=0)
            myentry = tk.Entry(athleatwind, bd = 5)
            myentry.grid(row=i, column=1)
            mylst.append(myentry)
            i += 1
        
        saveathleatbutton = tk.Button(athleatwind, text="Save", command= lambda: startlstclass.saveathleatbutton_clicked(mylst))
        saveathleatbutton.grid(row=i, column=1)
        athleatwind.mainloop()
        print("Add athleat to event!")