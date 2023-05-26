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
    savecompbutton = tk.Button(create_compwind, text="Save", command= lambda: savecompbutton_clicked(db, mycursor, mylst, description))
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

def myui():
    wind = tk.Tk()
    sqlclassobj = sql.sqlting()
    sqlclassobj.connect()
    sqlclassobj.createcursor()

    Create_compbutton = tk.Button(wind, text="Create new competition", command= lambda: Create_comp_button_clicked(sqlclassobj.mydb, sqlclassobj.mycursor))
    Create_compbutton.grid(row=0, column=0)
    
    sqlclassobj.mycursor.execute("SELECT * FROM competition")
    myresult = sqlclassobj.mycursor.fetchall()
    i = 1
    for x in myresult:
        y = 0
        if i==1:
            for k in x.keys():
                e = tk.Label(wind, width=20, text = k, relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
        else:
            #make list of competition objects
            for key, value in x.items():
                if key == "Name":
                    e = tk.Button(wind, width=20, text = x[key], relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                else:
                    e = tk.Label(wind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                y += 1
            programbutton = tk.Button(wind, width=20, text = "Start List", command= lambda: programbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
            programbutton.grid(row=i, column=y)
            editcompbutton = tk.Button(wind, width=20, text = "edit/delete", command= lambda: editcompbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
            editcompbutton.grid(row=i, column=y+1)
            """
            startlstbutton = tk.Button(wind, width=20, text = "Start List", command= lambda: startlstbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
            startlstbutton.grid(row=i, column=y)
            heatlstbutton = tk.Button(wind, width=20, text = "Heat List", command= lambda: heatlstbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
            heatlstbutton.grid(row=i, column=y+1)
            resultlstbutton = tk.Button(wind, width=20, text = "Result List", command= lambda: resultbuttonclick(sqlclassobj.mydb, sqlclassobj.mycursor), relief="ridge", anchor="w")
            resultlstbutton.grid(row=i, column=y+2)
            """
        i += 1
    sqlclassobj.mycursor.close()
    sqlclassobj.mydb.close()
    wind.mainloop()