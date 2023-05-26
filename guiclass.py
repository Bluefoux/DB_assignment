import tkinter as tk
import sqlclass as sql
import competition as comp

class guiclass:
    def savecompbutton_clicked(db, mycursor, mylst, description):
        compname = comp.competition(mylst[0].get(), mylst[1].get(), mylst[2].get(), mylst[3].get(), mylst[4].get(), mylst[5].get(), mylst[6].get(), mylst[7].get(), mylst[8].get(), description.get())
        #compname.save(mycursor, db) #uncomment this when change is wanted in database
        print("Save button was clicked!")
    
    
