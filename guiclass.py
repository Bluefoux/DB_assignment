import tkinter as tk
import competition as comp

class guiclass:

    def setcompobjlst(myresult):
        compobjlst = []
        for x in myresult:
            compobjlst.append(comp.competition(x["Name"], x["StartDate"], x["EndDate"], x["CompetitionVenue"], x["Organizer"], x["NumberOfLanes"], x["Length"], x["IndividualStartFee"], x["RelayStartFee"], x["Description"], None, x["ID"]))
        return compobjlst

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
    
    def startlstbuttonclick(mydb, mycursor): #needed in programbuttonclick
        print("Show start list!")

    def heatlstbuttonclick(mydb, mycursor): #needed in programbuttonclick
        print("Show heat list!")

    def resultbuttonclick(mydb, mycursor): #needed in programbuttonclick
        print("Show result list!")

    def editcompbuttonclick(mydb, mycursor): #needed in programbuttonclick
        print("edit competition!")

    def programbuttonclick(mydb, mycursor):
        print("Show program!")


    """ Add this to programbuttonclick when needed

    startlstbutton = tk.Button(wind, width=20, text = "Start List", command= lambda: startlstbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
    startlstbutton.grid(row=i, column=y)
    heatlstbutton = tk.Button(wind, width=20, text = "Heat List", command= lambda: heatlstbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
    heatlstbutton.grid(row=i, column=y+1)
    resultlstbutton = tk.Button(wind, width=20, text = "Result List", command= lambda: resultbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
    resultlstbutton.grid(row=i, column=y+2)
    """