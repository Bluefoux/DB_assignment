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


def savecompbutton_clicked(db, mycursor):
    compname = comp.competition()
    compname.save(mycursor, db)
    print("Save button was clicked!")

def Create_comp_button_clicked(db, mycursor):
    create_compwind = tk.Tk()
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Name", relief="ridge", anchor="w")
    e.grid(row=1, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Start Date", relief="ridge", anchor="w")
    e.grid(row=2, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "End Date", relief="ridge", anchor="w")
    e.grid(row=3, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Venue", relief="ridge", anchor="w")
    e.grid(row=4, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Oranizer", relief="ridge", anchor="w")
    e.grid(row=5, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Number of lanes", relief="ridge", anchor="w")
    e.grid(row=6, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Pool length", relief="ridge", anchor="w")
    e.grid(row=7, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Individual fee", relief="ridge", anchor="w")
    e.grid(row=8, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Relay fee", relief="ridge", anchor="w")
    e.grid(row=9, column=0)
    e = tk.Label(create_compwind, width=20, fg='blue', text = "Description", relief="ridge", anchor="w")
    e.grid(row=10, column=0)
    savecompbutton = tk.Button(create_compwind, text="Save", command=savecompbutton_clicked)
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