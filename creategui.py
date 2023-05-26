import tkinter as tk
import sqlclass as sql
import competition as comp

"""
TODO:
Add new competition button do stuff
Edit competition 
Add delete competition button
program knapp
Lägg till scroll ting för competitions
"""


def savecompbutton_clicked(db, mycursor, mylst, description):
    compname = comp.competition(mylst[0].get(), mylst[1].get(), mylst[2].get(), mylst[3].get(), mylst[4].get(), mylst[5].get(), mylst[6].get(), mylst[7].get(), mylst[8].get(), description.get())
    compname.save(mycursor, db)
    print("Save button was clicked!")

def Create_comp_button_clicked(db, mycursor):
    create_compwind = tk.Tk()
    mytup = ("Name", "Start Date", "End Date", "Venue", "Organizer", "Number of lanes", "Pool length", "Individual fee", "Relay fee")
    mylst = []
    i=1
    for x in mytup:
        e = tk.Label(create_compwind, width=20, fg='blue', text = x, relief="ridge", anchor="w")
        e.grid(row=i, column=0)
        myentry = tk.Entry(create_compwind, bd = 10)
        myentry.grid(row=i, column=1)
        mylst.append(myentry)
        i += 1
    
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Description", relief="ridge", anchor="w")
    e.grid(row=10, column=0)
    description = tk.Entry(create_compwind, bd = 30)
    e.grid(row=1, column=0)
    savecompbutton = tk.Button(create_compwind, text="Save", command=savecompbutton_clicked(db, mycursor, mylst, description))
    savecompbutton.grid(row=11, column=1)
    create_compwind.mainloop()
    print("Button was clicked!")

def myui():
    wind = tk.Tk()
    #wind.geometry("800x600")
    # Code to add widgets will go here...
    sqlclassobj = sql.sqlting()
    db = sqlclassobj.connect()
    mycursor = sqlclassobj.createcursor()

    Create_compbutton = tk.Button(wind, text="Create new competition", command=Create_comp_button_clicked(db, mycursor))
    #Create_compbutton.pack()
    Create_compbutton.grid(row=0, column=0)
    
    sqlclassobj.mycursor.execute("SELECT * FROM competition")
    myresult = sqlclassobj.mycursor.fetchall()
    i = 1
    for x in myresult:
        y = 0
        if i==1:
            for k in x.keys():
                e = tk.Label(wind, width=20, fg='blue', text = k, relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
        else:
            for key, value in x.items():
                if key == "Name":
                    e = tk.Button(wind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                else:
                    e = tk.Label(wind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                y += 1
        i += 1
    sqlclassobj.mycursor.close()
    sqlclassobj.mydb.close()
    wind.mainloop()