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
    sqlclassobj = sql.sqlting()
    sqlclassobj.connect()
    sqlclassobj.createcursor()

    Create_compbutton = tk.Button(wind, text="Create new competition", command= lambda: gui.guiclass.Create_comp_button_clicked(sqlclassobj.mydb, sqlclassobj.mycursor))
    Create_compbutton.grid(row=0, column=0)
    
    sqlclassobj.mycursor.execute("SELECT * FROM competition")
    myresult = sqlclassobj.mycursor.fetchall()
    
    for m in myresult:
        print(m)
        compobjlst.append(comp.competition(m["Name"], m["StartDate"], m["EndDate"], m["CompetitionVenue"], m["Organizer"], m["NumberOfLanes"], m["Length"], m["IndividualStartFee"], m["RelayStartFee"], m["Description"], None, m["ID"]))
    
    i = 1
    for x in myresult:
        y = 0
        if i==1:
            for k in x.keys():
                e = tk.Label(wind, width=20, text = k, relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
        else:
            for key, value in x.items():
                if key == "Name":
                    e = tk.Button(wind, width=20, text = x[key], relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                else:
                    e = tk.Label(wind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                y += 1
            programbutton = tk.Button(wind, width=20, text = "Program", command= lambda: gui.guiclass.programbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor, compobjlst[i-2]), relief="ridge", anchor="w")
            programbutton.grid(row=i, column=y)
            editcompbutton = tk.Button(wind, width=20, text = "edit/delete", command= lambda: gui.guiclass.editcompbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor, compobjlst[i-2]), relief="ridge", anchor="w")
            editcompbutton.grid(row=i, column=y+1)
        i += 1
    sqlclassobj.mycursor.close()
    sqlclassobj.mydb.close()
    wind.mainloop()