import tkinter as tk
import sqlclass as sql
import competition as comp
import guiclass as gui
import startlstgui as startlst

class myguiclass:

    def __init__() -> None:
        pass
    
    def myui():
        wind = tk.Tk()
        wind.title("Competition list")

        myguiclass.myuilayout(wind)
        wind.mainloop()
    
    def myuilayout(wind):
        compobjlst = []

        sqlclassobj = sql.sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        try:
            sqlclassobj.mycursor.execute("SELECT * FROM competition")
            myresult = sqlclassobj.mycursor.fetchall()
            sqlclassobj.close()
        except:
            print("No competitions found")
            sqlclassobj.close()
            return None
        
        for m in myresult:
            compobj = comp.competition(id=m['ID'], name=m['CompName'], StartDate=m['StartDate'], Enddate=m['EndDate'], CompetitionVenue=m['CompetitionVenue'], Organizer=m['Organizer'], NumberOfLanes=m['NumberOfLanes'], Length=m['Length'], IndividualStartFee=m['IndividualStartFee'], RelayStartFee=m['RelayStartFee'], Description=m['Description'])
            compobjlst.append(compobj)
        
        Create_compbutton = tk.Button(
                wind,
                width=20,
                text="Create new competition",
                command=lambda wind=wind: myguiclass.Add_comp_button_clicked(wind),
                relief="ridge",
                anchor="w"
            )
        Create_compbutton.grid(row=0, column=0)
        
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
                if key == "CompName":
                    e = tk.Button(wind, width=20, text = x[key], relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                else:
                    e = tk.Label(wind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                y += 1

            getinvoicebutton = tk.Button(
                wind,
                width=20,
                text="Invoice",
                command=lambda i=i: myguiclass.getinvoicebuttonclick(wind, compobjlst[i-2]),
                relief="ridge",
                anchor="w"
            )
            getinvoicebutton.grid(row=i, column=y)

            programbutton = tk.Button(
                wind,
                width=20,
                text="Program",
                command=lambda i=i: gui.guiclasstwo.programbuttonclick(compobjlst[i-2]),
                relief="ridge",
                anchor="w"
            )
            programbutton.grid(row=i, column=y+1)

            editcompbutton = tk.Button(
                wind,
                width=20,
                text="Edit/Delete",
                command=lambda i=i: myguiclass.editcompbuttonclick(wind, compobjlst[i-2]),
                relief="ridge",
                anchor="w"
            )
            editcompbutton.grid(row=i, column=y+2)
            i += 1

    def getinvoicebuttonclick(wind, compobj):
        get_invoicewind = tk.Toplevel(wind)
        get_invoicewind.title("Invoice List")

        sqlclassobj = sql.sqlting()
        sqlclassobj.connect()
        sqlclassobj.createdictcursor()
        try:
            query = "CALL SP_GetInvoice(%s)"
            values = (compobj.id,)
            sqlclassobj.mycursor.execute(query, values)
            myresult = sqlclassobj.mycursor.fetchall()
            sqlclassobj.close()
        except:
            print("No competitions found")
            sqlclassobj.close()
            return None
        i = 1
        for x in myresult:
            y = 0
            if i==1:
                for k in x.keys():
                    e = tk.Label(get_invoicewind, width=20, text = k, relief="ridge", anchor="w")
                    e.grid(row=i, column=y)
                    y += 1
                i += 1
                y = 0
            for key, value in x.items():
                e = tk.Label(get_invoicewind, width=20, fg='blue', text = x[key], relief="ridge", anchor="w")
                e.grid(row=i, column=y)
                y += 1
            i += 1

    def on_close_editcomp(wind, edit_compwind):
        myguiclass.myuilayout(wind)
        wind.update()
        edit_compwind.destroy()

    def editcompbuttonclick(wind, compobj):
        mylst = []
        edit_compwind = tk.Toplevel(wind)
        edit_compwind.title("edit competition")
        mytup = ("Name", "Start Date", "End Date", "Venue", "Organizer", "Number of lanes", "Pool length", "Individual fee", "Relay fee")
        valid_attr = ("name", "StartDate", "Enddate", "CompetitionVenue", "Organizer", "NumberOfLanes", "Length", "IndividualStartFee", "RelayStartFee")
        i=1
        for attr, value in vars(compobj).items():
            if attr in valid_attr:
                e = tk.Label(edit_compwind, width=20, fg='blue', text = mytup[i-1], relief="ridge", anchor="w")
                e.grid(row=i, column=0)
                myentry = tk.Entry(edit_compwind, bd = 5)
                myentry.insert(0, value)
                myentry.grid(row=i, column=1)
                mylst.append(myentry)
                i += 1
        
        e = tk.Label(edit_compwind, width=20, fg='blue', text = "Description", relief="ridge", anchor="w")
        e.grid(row=i, column=0)
        description = tk.Entry(edit_compwind, bd = 5)
        description.insert(0, compobj.Description)
        description.grid(row=i, column=1)
        savecompbutton = tk.Button(
            edit_compwind,
            width=20,
            text="Save changes",
            command= lambda: myguiclass.savecompbutton_clicked(compobj, mylst, description)
        )
        savecompbutton.grid(row=i+1, column=1)

        edit_compwind.protocol("WM_DELETE_WINDOW", lambda: myguiclass.on_close_editcomp(wind, edit_compwind))
        edit_compwind.mainloop()
    
    def on_close_addcomp(wind, create_compwind):
        myguiclass.myuilayout(wind)
        wind.update()
        create_compwind.destroy()

    def Add_comp_button_clicked(wind):
        compobj = comp.competition()
        create_compwind = tk.Toplevel(wind)
        create_compwind.title("Create new competition")
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
        e.grid(row=i, column=0)
        description = tk.Entry(create_compwind, bd = 5)
        description.grid(row=i, column=1)
        savecompbutton2 = tk.Button(
            create_compwind,
            width=20,
            text="Save",
            command=lambda : myguiclass.savecompbutton_clicked(compobj, mylst, description)
        )
        savecompbutton2.grid(row=i+1, column=1)
        create_compwind.protocol("WM_DELETE_WINDOW", lambda: myguiclass.on_close_addcomp(wind, create_compwind))
        create_compwind.mainloop()

    def savecompbutton_clicked(compobj, mylst, description):
        valid_attr = ("name", "StartDate", "Enddate", "CompetitionVenue", "Organizer", "NumberOfLanes", "Length", "IndividualStartFee", "RelayStartFee")
        i=0
        for attr, value in vars(compobj).items():
            if attr in valid_attr:
                setattr(compobj, attr, mylst[i].get())
                i += 1
        setattr(compobj, "Description", description.get())
        
        compobj.save()