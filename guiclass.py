import tkinter as tk
import competition as comp
import sqlclass as sql
import startlstgui as startlst
import event as event

class guiclass:
    def __init__() -> None:
        pass

    #def setcompobjlst(x):
    #    compobj = (comp.competition(x["Name"], x["StartDate"], x["EndDate"], x["CompetitionVenue"], x["Organizer"], x["NumberOfLanes"], x["Length"], x["IndividualStartFee"], x["RelayStartFee"], x["Description"], None, x["ID"]))
    #    return compobj

    def savecompbutton_clicked(mylst, description):
        compname = comp.competition(mylst[0].get(), mylst[1].get(), mylst[2].get(), mylst[3].get(), mylst[4].get(), mylst[5].get(), mylst[6].get(), mylst[7].get(), mylst[8].get(), description.get())
        #compname.save() #uncomment this when change is wanted in database
        print("Save button was clicked!")
    
    def Create_comp_button_clicked():
        create_compwind = tk.Tk()
        create_compwind.title("Create new competition")
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
        print("Button was clicked!")

    def editcompbuttonclick(compobj):
        print("edit competition!")

    def addeventbuttonclick(compobj):
        print("add event!")
    
    def editeventbuttonclick(compobj): #needed in programbuttonclick
        print("edit event!")

    def resultbuttonclick(compobj): #needed in programbuttonclick
        print("Show result list!")

    def programbuttonclick(compobj):
        progwind = tk.Tk()
        eventobjlst = []
        progwind.title("Program")

        addeventbutton = tk.Button(progwind, text="Add new event", command= lambda: guiclass.addeventbuttonclick(compobj))
        addeventbutton.grid(row=0, column=0)

        sqlclassobj = sql.sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        sqlquery = "SELECT * FROM EVENT WHERE CompetitionID = %s"
        values = (compobj.id,)  # Enclose compobj.id in a tuple
        try:
            sqlclassobj.mycursor.execute(sqlquery, values)
            myresult = sqlclassobj.mycursor.fetchall()
            sqlclassobj.close()
        except:
            print("Error in sql query")
            sqlclassobj.close()
            return None
        
        for m in myresult:
            eventobjlst.append(event.event(id=m["ID"], competitionid=m["CompetitionID"], eventnumber=m["EventNumber"], eventname=m["EventName"], distance=m["Distance"], gender=m["Gender"], maxage=m["MaxAge"], qualifyingtime=m["QualifyingTime"], relay=m["Relay"]))

        i = 1
        for x in myresult:
            y = 0
            if i==1:
                for k in x.keys():
                    e = tk.Label(progwind, width=20, text = k, relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                    y += 1
                i += 1
                y = 0
            for key, value in x.items():
                e = tk.Label(progwind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
            startlstbutton = tk.Button(
                progwind,
                width=20,
                text="Start list",
                command=lambda i=i: startlst.startlstclass.startlstbuttonclick(eventobjlst[i-2]),
                relief="ridge",
                anchor="w"
            )
            #startlstbutton = tk.Button(progwind, width=20, text = "Start list", command= lambda: startlst.startlstclass.startlstbuttonclick(eventobjlst[i-2]), relief="ridge", anchor="w")
            startlstbutton.grid(row=i, column=y)
            heatlstbutton = tk.Button(
                progwind,
                width=20,
                text="Heat list",
                command=lambda i=i: startlst.startlstclass.heatlstbuttonclick(eventobjlst[i-2]),
                relief="ridge",
                anchor="w"
            )
            #heatlstbutton = tk.Button(progwind, width=20, text = "Heat list", command= lambda: guiclass.heatlstbuttonclick(eventobjlst[i-2]), relief="ridge", anchor="w")
            heatlstbutton.grid(row=i, column=y+1)
            resultlstbutton = tk.Button(
                progwind,
                width=20,
                text="Result list",
                command=lambda i=i: guiclass.resultbuttonclick(eventobjlst[i-2]),
                relief="ridge",
                anchor="w"
            )
            #resultlstbutton = tk.Button(progwind, width=20, text = "Result list", command= lambda: guiclass.resultbuttonclick(eventobjlst[i-2]), relief="ridge", anchor="w")
            resultlstbutton.grid(row=i, column=y+2)
            editeventbutton = tk.Button(
                progwind,
                width=20,
                text="edit/delete",
                command=lambda i=i: guiclass.editeventbuttonclick(eventobjlst[i-2]),
                relief="ridge",
                anchor="w"
            )
            #editeventbutton = tk.Button(progwind, width=20, text = "edit/delete", command= lambda: guiclass.editeventbuttonclick(eventobjlst[i-2]), relief="ridge", anchor="w")
            editeventbutton.grid(row=i, column=y+3)
            i += 1
        progwind.mainloop()
        print("Show program!")
        