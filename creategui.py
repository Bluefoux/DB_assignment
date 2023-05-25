import tkinter as tk

def Create_comp_button_clicked():
    print("Button was clicked!")

def myui():
    wind = tk.Tk()
    # Code to add widgets will go here...
    #what to add:
    Create_compbutton = tk.Button(wind, text="Create new competition", command=Create_comp_button_clicked)
    wind.mainloop()