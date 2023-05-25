import tkinter as tk
import sqlclass as sql

def Create_comp_button_clicked():
    print("Button was clicked!")

def myui():
    wind = tk.Tk()
    # Code to add widgets will go here...
    Create_compbutton = tk.Button(wind, text="Create new competition", command=Create_comp_button_clicked)
    Create_compbutton.pack()

    sqlclassobj = sql.sqlting()
    db = sqlclassobj.connect()
    mycursor = sqlclassobj.createcursor()
    sqlclassobj.mycursor.execute("SELECT * FROM competition")
    myresult = sqlclassobj.mycursor.fetchall()
    for row in myresult:
        print(row)
    
    sqlclassobj.mycursor.close()
    sqlclassobj.mydb.close()
    wind.mainloop()