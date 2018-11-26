#importing TKinter
from tkinter import *


#sub-routines
def speak():
    print("you forgot a command")
def are_you_sure_lockout():
    #clear window
    GUIFrame0.destroy()
    GUIFrame1.destroy()
    GUIFrame2.destroy()
    GUIFrame3.destroy()
    GUIFrame4.destroy()
    #Frame
    GUIFrame5 = Frame(main)
    GUIFrame5.grid(row=1, column=0)
    # add a name
    Label(main, text="Are you sure you want to Lock Out").grid(row=0, column=0)
    #buttons
    Button(GUIFrame5, text="YES", width=12, command=lock_out).grid(row=0, column=0)
    Button(GUIFrame5, text="NO", width=12, command=exit).grid(row=0, column=1)
def lock_out():
    #new window
    lockout = Tk()
    lockout.title("Intelagis")
    lockout.geometry("200x200")
    # add a name
    Label(lockout, text="Please Follow Steps Below").grid(row=0, column=0)
    Label(lockout, text="1:Bring Everyone Inside").grid(row=1, column=0)
    Label(lockout, text="2:Lock Outside Doors").grid(row=2, column=0)
    Label(lockout, text="3:Increase Your Awareness").grid(row=3, column=0)
    Label(lockout, text="4:Take Attendance").grid(row=4, column=0)
    Label(lockout, text="Are you in Your Classroom?").grid(row=5, column=0)
    # Frame
    GUIFrame6 = Frame(lockout)
    GUIFrame6.grid(row=6, column=0)
    # buttons
    Button(GUIFrame6, text="YES", width=12, command=speak).grid(row=0, column=0)
    Button(GUIFrame6, text="NO", width=12, command=exit).grid(row=0, column=1)
def active_shooter():
    #new window
    shooter = Tk()
    shooter.title("Intelagis")
    shooter.geometry("200x200")
    # add a name
    Label(shooter, text="HELP IS ON THE WAY!").grid(row=0, column=0)


#make gui window
main=Tk()
main.title("Intelagis")
main.geometry("400x400")
#adding frame
GUIFrame0=Frame(main)
GUIFrame0.grid(row=0, column=0)
GUIFrame1=Frame(main)
GUIFrame1.grid(row=1, column=0)
GUIFrame2=Frame(main)
GUIFrame2.grid(row=2, column=0)
GUIFrame3=Frame(main)
GUIFrame3.grid(row=3, column=0)
GUIFrame4=Frame(main)
GUIFrame4.grid(row=4, column=0)


#add a name
Label(GUIFrame0, text="What is your Emergency?").grid(row=0, column=0)


#add buttons
Button(GUIFrame1, text="Lock Out", width=12, command=are_you_sure_lockout).grid(row=0, column=0)
Button(GUIFrame1, text="Shelter", width=12, command=speak).grid(row=0, column=1)
Button(GUIFrame2, text="Evacuate", width=12, command=speak).grid(row=0, column=0)
Button(GUIFrame2, text="Medical", width=12, command=speak).grid(row=0, column=1)
Button(GUIFrame3, text="Intruder", width=24, command=speak).grid(row=0, column=0)
Button(GUIFrame4, text="Active Shooter", width=24, command=active_shooter).grid(row=0, column=0)
main.mainloop()