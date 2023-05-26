import tkinter as tk
import sqlclass as sql
import competition as comp
import guiclass as gui

"""
TODO:
Add new competition button do stuff (kinda done)
Edit competition 
Add delete competition button (done)
program knapp (need to make things happen when clicked)
Lägg till scroll ting för competitions

consider making a class for most of this (its starting to get messy)
"""


def myui():
    compobjlst = []
    wind = tk.Tk()

    Create_compbutton = tk.Button(wind, text="Create new competition", command= lambda: gui.guiclass.Create_comp_button_clicked())
    Create_compbutton.grid(row=0, column=0)

    sqlclassobj = sql.sqlting()
    sqlclassobj.connect()
    sqlclassobj.createdictcursor()
    sqlclassobj.mycursor.execute("SELECT * FROM competition")
    myresult = sqlclassobj.mycursor.fetchall()
    sqlclassobj.close()
    
    for m in myresult:
        compobjlst.append(comp.competition(name=m["Name"], StartDate=m["StartDate"], Enddate=m["EndDate"], CompetitionVenue=m["CompetitionVenue"], Organizer=m["Organizer"], NumberOfLanes=m["NumberOfLanes"], Length=m["Length"], IndividualStartFee=m["IndividualStartFee"], RelayStartFee=m["RelayStartFee"], Description=m["Description"], id=m["ID"]))
    
    #for i in range(len(compobjlst)):
    #    print(compobjlst[i].id)
    
    i = 1
    for x in myresult:
        y = 0
        if i==1:
            for k in x.keys():
                e = tk.Label(wind, width=20, text = k, relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
            y=0
            i += 1

        for key, value in x.items():
            if key == "Name":
                e = tk.Button(wind, width=20, text = x[key], relief="ridge", anchor="w")
                e.grid(row=i, column=y)
            else:
                e = tk.Label(wind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                e.grid(row=i, column=y)
            y += 1
        programbutton = tk.Button(
            wind,
            width=20,
            text="Program",
            command=lambda i=i: gui.guiclass.programbuttonclick(compobjlst[i-2]),
            relief="ridge",
            anchor="w"
        )
        programbutton.grid(row=i, column=y)

        editcompbutton = tk.Button(
            wind,
            width=20,
            text="edit/delete",
            command=lambda i=i: gui.guiclass.editcompbuttonclick(compobjlst[i-2]),
            relief="ridge",
            anchor="w"
        )
        editcompbutton.grid(row=i, column=y+1)
        i += 1
    wind.mainloop()