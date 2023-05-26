import tkinter as tk
from sqlclass import sqlting

class startlstclass:
    def startlstbuttonclick(eventobj):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        query = "SELECT Name, Lastname, TeamName, RegistrationTime FROM ATHLEATS INNER JOIN EVENT ON ATHLEATS.EventID = EVENT.ID AND EVENT.CompetitionID = %s AND ATHLEATS.EventID = %s ORDER BY RegistrationTime ASC"
        values = (eventobj.competitionid, eventobj.id)
        print(values)
        try:
            sqlclassobj.mycursor.execute(query, values)
            startlst = sqlclassobj.mycursor.fetchall()
        except:
            print("Error: Could not fetch data")
        sqlclassobj.close()

        startwindow = tk.Tk()

        i = 1
        for x in startlst:
            y = 0
            if i==1:
                for k in x.keys():
                    e = tk.Label(startwindow, width=20, text = k, relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                    y += 1
                i += 1
                y = 0
            for key, value in x.items():
                e = tk.Label(startwindow, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
            i += 1
        startwindow.mainloop()
        print("Show start list!")

    def heatlstbuttonclick(eventobj):
        sqlclassobj = sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        query = "SELECT Name, Lastname, TeamName, RegistrationTime FROM ATHLEATS INNER JOIN EVENT ON ATHLEATS.EventID = EVENT.ID AND EVENT.CompetitionID = %s AND ATHLEATS.EventID = %s ORDER BY RegistrationTime ASC"
        values = (eventobj.competitionid, eventobj.id)
        print(values)
        try:
            sqlclassobj.mycursor.execute(query, values)
            startlst = sqlclassobj.mycursor.fetchall()
        except:
            print("Error: Could not fetch data")
        sqlclassobj.close()

        startwindow = tk.Tk()

        i = 1
        for x in startlst:
            y = 0
            if i==1:
                for k in x.keys():
                    e = tk.Label(startwindow, width=20, text = k, relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                    y += 1
                i += 1
                y = 0
            for key, value in x.items():
                e = tk.Label(startwindow, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
            i += 1
        startwindow.mainloop()
        print("Show start list!")