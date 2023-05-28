import tkinter as tk
import tkinter.messagebox as tkmb
import sqlclass as sql
import startlstgui as startlst
import event as event

class guiclasstwo:
    def __init__() -> None:
        pass

    def saveventbutton_clicked(mylst, eventobj, rel): #mybool used to determine if it is a new event or an existing one
        valid_attr = ("eventnumber", "eventname", "distance", "gender", "maxage", "qualifyingtime")
        i=0
        for attr, value in vars(eventobj).items():
            if attr in valid_attr:
                setattr(eventobj, attr, mylst[i].get())
                i += 1
        setattr(eventobj, "relay", rel.get())
        eventobj.save()
    
    def update_checkvar(checkvar):
        if(checkvar.get() == 0):
            checkvar.set(1)
        else:
            checkvar.set(0)

    def Create_start_heat_mm_buttons(progwind, eventobjlst, i, y, compobj):
        startlstbutton = tk.Button(
            progwind,
            width=20,
            text="Start list",
            command=lambda i=i: startlst.startlstclass.startlstbutton_clicked(progwind, eventobjlst[i-2]),
            relief="ridge",
            anchor="w"
        )
        startlstbutton.grid(row=i, column=y)
        heatlstbutton = tk.Button(
            progwind,
            width=20,
            text="Heat list",
            command=lambda i=i: startlst.startlstclass.heatlstbutton_clicked(progwind, eventobjlst[i-2]),
            relief="ridge",
            anchor="w"
        )
        heatlstbutton.grid(row=i, column=y+1)
        resultlstbutton = tk.Button(
            progwind,
            width=20,
            text="Result list",
            command=lambda i=i: guiclasstwo.resultbutton_clicked(eventobjlst[i-2]),
            relief="ridge",
            anchor="w"
        )
        resultlstbutton.grid(row=i, column=y+2)
        editeventbutton = tk.Button(
            progwind,
            width=20,
            text="edit/delete",
            command=lambda i=i: guiclasstwo.editeventbutton_clicked(progwind, eventobjlst[i-2], compobj),
            relief="ridge",
            anchor="w"
        )
        editeventbutton.grid(row=i, column=y+3)

    def on_close(progwind, compobj, addevwind):
        guiclasstwo.event_layout(progwind, compobj)
        progwind.update()
        addevwind.destroy()

    def showeventvals(progwind, eventobjlst, myresult, compobj):
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

            guiclasstwo.Create_start_heat_mm_buttons(progwind, eventobjlst, i, y, compobj)
            i += 1

    def addeventbutton_clicked(compobj, progwind):
        mytup = ("eventnumber", "eventname", "distance", "gender", "maxage", "qualifyingtime")
        mylst = []
        eventobj = event.event(competitionid=compobj.id)
        addevwind = tk.Toplevel(progwind)
        addevwind.title("Add event")
        
        i=5
        for x in mytup:
            e = tk.Label(addevwind, width=20, text = x, relief="ridge", anchor="w")
            e.grid(row=i, column=0)
            myentry = tk.Entry(addevwind, bd = 5)
            myentry.grid(row=i, column=1)
            mylst.append(myentry)
            i += 1
        
        checkvar = tk.IntVar()
        
        checkbutton = tk.Checkbutton(addevwind, text = "Relay", variable=checkvar, command= lambda: guiclasstwo.update_checkvar(checkvar))
        checkbutton.grid(row=i, column=0)

        saveathleatbutton = tk.Button(addevwind, text="Save", command= lambda: guiclasstwo.saveventbutton_clicked(mylst, eventobj, checkvar))
        saveathleatbutton.grid(row=i+1, column=1)
        addevwind.protocol("WM_DELETE_WINDOW", lambda: guiclasstwo.on_close(progwind, compobj, addevwind))
        addevwind.mainloop()
        
    
    def editeventbutton_clicked(progwind, eventobj, compobj):
        mylst = []
        edit_evepwind = tk.Toplevel(progwind)
        edit_evepwind.title("edit event")
        mytup = ("Event number", "Name", "Distance", "Gender", "Max age", "Qualifying time")
        valid_attr = ("eventnumber", "eventname", "distance", "gender", "maxage", "qualifyingtime")
        
        i=1
        for attr, value in vars(eventobj).items():
            if attr in valid_attr:
                e = tk.Label(edit_evepwind, width=20, fg='blue', text = mytup[i-1], relief="ridge", anchor="w")
                e.grid(row=i, column=0)
                myentry = tk.Entry(edit_evepwind, bd = 5)
                myentry.insert(0, value)
                myentry.grid(row=i, column=1)
                mylst.append(myentry)
                i += 1

        checkvar = tk.IntVar()
        
        checkbutton = tk.Checkbutton(edit_evepwind, text = "Relay", variable=checkvar, command= lambda: guiclasstwo.update_checkvar(checkvar))
        checkvar.set(eventobj.relay)
        checkbutton.grid(row=i, column=0)

        savecompbutton = tk.Button(
            edit_evepwind,
            width=20,
            text="Save changes",
            command= lambda: guiclasstwo.saveventbutton_clicked(mylst, eventobj, checkvar)
        )
        savecompbutton.grid(row=i+1, column=1)
        edit_evepwind.protocol("WM_DELETE_WINDOW", lambda: guiclasstwo.on_close(progwind, compobj, edit_evepwind))
        edit_evepwind.mainloop()

    def resultbutton_clicked(eventobj): #future work
        print("Show result list!")
    
    def event_layout(progwind, compobj):
        eventobjlst = []

        sqlclassobj = sql.sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        sqlquery = "SELECT * FROM EVENT WHERE CompetitionID = %s"
        values = (compobj.id,)
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

        addeventbutton = tk.Button(progwind, text="Add new event", command= lambda: guiclasstwo.addeventbutton_clicked(compobj, progwind))
        addeventbutton.grid(row=0, column=0)

        guiclasstwo.showeventvals(progwind, eventobjlst, myresult, compobj)

    def programbuttonclick(compobj):
        progwind = tk.Tk()
        progwind.title("Program")

        guiclasstwo.event_layout(progwind, compobj)
        progwind.mainloop()
        