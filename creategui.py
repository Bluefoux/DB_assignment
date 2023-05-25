import tkinter as tk
import sqlclass as sql

"""
TODO:
Add new competition button do stuff
Edit competition 
Add delete competition button
program knapp
Lägg till scroll ting för competitions
"""

def Create_comp_button_clicked():
    print("Button was clicked!")

def myui():
    wind = tk.Tk()
    #wind.geometry("800x600")
    # Code to add widgets will go here...
    Create_compbutton = tk.Button(wind, text="Create new competition", command=Create_comp_button_clicked)
    #Create_compbutton.pack()
    Create_compbutton.grid(row=0, column=0)

    sqlclassobj = sql.sqlting()
    db = sqlclassobj.connect()
    mycursor = sqlclassobj.createcursor()
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