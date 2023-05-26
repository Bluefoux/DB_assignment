import tkinter as tk
import competition as comp

class guiclass:
    def __init__() -> None:
        pass

    #def setcompobjlst(x):
    #    compobj = (comp.competition(x["Name"], x["StartDate"], x["EndDate"], x["CompetitionVenue"], x["Organizer"], x["NumberOfLanes"], x["Length"], x["IndividualStartFee"], x["RelayStartFee"], x["Description"], None, x["ID"]))
    #    return compobj

    def savecompbutton_clicked(db, mycursor, mylst, description):
        compname = comp.competition(mylst[0].get(), mylst[1].get(), mylst[2].get(), mylst[3].get(), mylst[4].get(), mylst[5].get(), mylst[6].get(), mylst[7].get(), mylst[8].get(), description.get())
        #compname.save(mycursor, db) #uncomment this when change is wanted in database
        print("Save button was clicked!")
    
    def Create_comp_button_clicked(db, mycursor):
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
        savecompbutton = tk.Button(create_compwind, text="Save", command= lambda: guiclass.savecompbutton_clicked(db, mycursor, mylst, description))
        savecompbutton.grid(row=11, column=1)
        create_compwind.mainloop()
        print("Button was clicked!")

    def editcompbuttonclick(mydb, mycursor, compobj):
        print("edit competition!")

    def addeventbuttonclick(mydb, mycursor):
        print("add event!")
    
    def editeventbuttonclick(mydb, mycursor, compobj): #needed in programbuttonclick
        print("edit event!")

    def startlstbuttonclick(mydb, mycursor): #needed in programbuttonclick
        print("Show start list!")

    def heatlstbuttonclick(mydb, mycursor): #needed in programbuttonclick
        print("Show heat list!")

    def resultbuttonclick(mydb, mycursor): #needed in programbuttonclick
        print("Show result list!")

    def programbuttonclick(mydb, mycursor, compobj):
        progwind = tk.Tk()
        compobj.getevents(mycursor)
        #if len(eventlst) != 0:
        print(len(compobj.eventlist))
        i = 1
        addeventbutton = tk.Button(progwind, text="Add new event", command= lambda: guiclass.addeventbuttonclick(mydb, mycursor))
        addeventbutton.grid(row=0, column=0)
        for x in compobj.eventlist:
            y = 0
            if i==1:
                for k in x.keys():
                    e = tk.Label(progwind, width=20, text = k, relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                    y += 1
            else:
                #make list of competition objects
                for key, value in x.items():
                    if key == "Name":
                        e = tk.Button(progwind, width=20, text = x[key], relief="ridge", anchor="w")
                        e.grid(row=i, column=y)
                    else:
                        e = tk.Label(progwind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                        e.grid(row=i, column=y)
                    y += 1
                startlstbutton = tk.Button(progwind, width=20, text = "Start list", command= lambda: guiclass.startlstbuttonclick(mydb, mycursor, compobj), relief="ridge", anchor="w")
                startlstbutton.grid(row=i, column=y)
                startlstbutton = tk.Button(progwind, width=20, text = "Heat list", command= lambda: guiclass.startlstbuttonclick(mydb, mycursor, compobj), relief="ridge", anchor="w")
                startlstbutton.grid(row=i, column=y)
                startlstbutton = tk.Button(progwind, width=20, text = "Result list", command= lambda: guiclass.startlstbuttonclick(mydb, mycursor, compobj), relief="ridge", anchor="w")
                startlstbutton.grid(row=i, column=y)
                editeventbutton = tk.Button(progwind, width=20, text = "edit/delete", command= lambda: guiclass.editeventbuttonclick(mydb, mycursor, compobj), relief="ridge", anchor="w")
                editeventbutton.grid(row=i, column=y+1)
            i += 1
        
        progwind.mainloop()
        print("Show program!")


    """ Add this to programbuttonclick when needed

    startlstbutton = tk.Button(wind, width=20, text = "Start List", command= lambda: startlstbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
    startlstbutton.grid(row=i, column=y)
    heatlstbutton = tk.Button(wind, width=20, text = "Heat List", command= lambda: heatlstbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
    heatlstbutton.grid(row=i, column=y+1)
    resultlstbutton = tk.Button(wind, width=20, text = "Result List", command= lambda: resultbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
    resultlstbutton.grid(row=i, column=y+2)
    """