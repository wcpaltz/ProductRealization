#importing TKinter
from tkinter import *
global other

#sub-routines
def speak():
    print("you forgot a command")
def speak_server_lockout():
    print("Insert Lockout communication here")
def speak_server_shelter():
        print("Insert Shelter communication here")
def speak_server_evacuate():
    print("Insert Evacuate communication here")
def speak_server_medical():
    print("Insert Medical communication here")
def speak_server_lock_down():
    print("Insert Lock Down communication here")
def are_you_sure_lockout():
    #clear window
    GUIFrame0.grid_remove()
    GUIFrame2.grid_remove()
    GUIFrame3.grid_remove()
    GUIFrame4.grid_remove()
    # add a name
    Label(main, text="Are you sure you want to Lock Out").grid(row=0, column=0)
    #buttons
    Button(GUIFrame1, text="YES", width=12, command=lock_out).grid(row=0, column=0)
    Button(GUIFrame1, text="NO", width=12, command=exit).grid(row=0, column=1)
def lock_out():
    #clear window
    GUIFrame0.grid_remove()
    GUIFrame1.grid_remove()
    Label(main, text="            Please Follow Steps Below           ").grid(row=0, column=0)
    Label(main, text="1:Bring Everyone Inside").grid(row=1, column=0)
    Label(main, text="2:Lock Outside Doors").grid(row=2, column=0)
    Label(main, text="3:Increase Your Awareness").grid(row=3, column=0)
    Label(main, text="4:Take Attendance").grid(row=4, column=0)
    Label(main, text="Are you in Your Classroom?").grid(row=5, column=0)
    # buttons
    Button(GUIFrame6, text="YES", width=12, command=speak_server_lockout).grid(row=0, column=0)
    Button(GUIFrame6, text="NO", width=12, command=exit).grid(row=0, column=1)
    
def are_you_sure_shelter():
    #clear window
    GUIFrame0.grid_remove()
    GUIFrame2.grid_remove()
    GUIFrame3.grid_remove()
    GUIFrame4.grid_remove()
    #instructions
    Label(main, text="Are you sure you want to Shelter in Place").grid(row=0, column=0)
    #buttons
    Button(GUIFrame1, text="YES", width=12, command=shelter).grid(row=0, column=0)
    Button(GUIFrame1, text="NO", width=12, command=exit).grid(row=0, column=1)
def shelter():
    #clear window
    GUIFrame1.grid()
    GUIFrame2.grid()
    GUIFrame3.grid()
    GUIFrame4.grid()
    GUIFrame6.grid()
    #Reasons
    Label(main, text="          Reason for Shelter in Place?            ").grid(row=0, column=0)
    # buttons
    Button(GUIFrame1, text="Tornado", width=26, command=speak_server_shelter).grid(row=0, columnspan=2)
    Button(GUIFrame2, text="Hazmat", width=26, command=speak_server_shelter).grid(row=0, columnspan=2)
    Button(GUIFrame3, text="Earthquake", width=26, command=speak_server_shelter).grid(row=0, columnspan=2)
    Button(GUIFrame4, text="Tsunami", width=26, command=speak_server_shelter).grid(row=0, columnspan=2)
    #text entry
    other = Entry(main)
    other.insert(13, "Other")
    other.grid(row=5, column=0)
    Button(GUIFrame6,text="Enter", width=13, command=speak_server_shelter).grid(row=0, column=0)
    Button(GUIFrame6,text="Cancel", width=13, command=exit).grid(row=0, column=1)
def are_you_sure_evacuate():
    #clear window
    GUIFrame0.grid_remove()
    GUIFrame2.grid_remove()
    GUIFrame3.grid_remove()
    GUIFrame4.grid_remove()
    #instructions
    Label(main, text="Are you sure you want to Evacuate").grid(row=0, column=0)
    #buttons
    Button(GUIFrame1, text="YES", width=12, command=speak_server_evacuate).grid(row=0, column=0)
    Button(GUIFrame1, text="NO", width=12, command=exit).grid(row=0, column=1)
def are_you_sure_medical():
    #clear window
    GUIFrame0.grid_remove()
    GUIFrame2.grid_remove()
    GUIFrame3.grid_remove()
    GUIFrame4.grid_remove()
    #instructions
    Label(main, text="Are you sure you want to Call Medical").grid(row=0, column=0)
    #buttons
    Button(GUIFrame1, text="YES", width=12, command=medical).grid(row=0, column=0)
    Button(GUIFrame1, text="NO", width=12, command=exit).grid(row=0, column=1)
def medical():
    #clear window
    GUIFrame1.grid_remove()
    GUIFrame1.grid()
    GUIFrame2.grid()
    #Reasons
    Label(main, text="     What is your medical Emergency?      ").grid(row=0, column=0)
    #text entry
    other = Entry(main)
    other.insert(26, "Enter Emergency")
    other.grid(row=1, columnspan=2)
    Button(GUIFrame2, text="Enter", width=13, command=speak_server_shelter).grid(row=0, column=0)
    Button(GUIFrame2, text="Cancel", width=13, command=exit).grid(row=0, column=1)
def are_you_sure_lockdown():
    #clear window
    GUIFrame0.grid_remove()
    GUIFrame2.grid_remove()
    GUIFrame3.grid_remove()
    GUIFrame4.grid_remove()
    #instructions
    Label(main, text="Are you sure you want Lock Down").grid(row=0, column=0)
    #buttons
    Button(GUIFrame2, text="YES", width=12, command=lock_down).grid(row=0, column=0)
    Button(GUIFrame3, text="NO", width=12, command=exit).grid(row=0, column=1)
def lock_down():
    #clear window
    GUIFrame1.grid()
    GUIFrame2.grid()
    GUIFrame3.grid()
    GUIFrame5.grid()
    #Reasons
    Label(main, text="Reason for Lock Down?").grid(row=0, column=0)
    # buttons
    Button(GUIFrame1, text="Dangerous Person Inside", width=26, command=speak_server_lock_down).grid(row=0, columnspan=2)
    Button(GUIFrame2, text="Fight", width=26, command=speak_server_lock_down).grid(row=0, columnspan=2)
    Button(GUIFrame3, text="Dangerous Animal Inside", width=26, command=speak_server_lock_down).grid(row=0, columnspan=2)
    #text entry
    other = Entry(main)
    other.insert(26, "Other")
    other.grid(row=4, column=0)
    Button(GUIFrame5, text="Enter", width=13, command=speak_server_lock_down).grid(row=0, column=0)
    Button(GUIFrame5, text="Cancel", width=13, command=exit).grid(row=0, column=1)
def are_you_sure_shooter():
    #clear window
    GUIFrame0.grid_remove()
    GUIFrame2.grid_remove()
    GUIFrame3.grid_remove()
    GUIFrame4.grid_remove()
    #instructions
    Label(main, text="Are you sure you want to activate Active Shooter Protocol").grid(row=0, column=0)
    #buttons
    Button(GUIFrame1, text="YES", width=12, command=active_shooter).grid(row=0, column=0)
    Button(GUIFrame1, text="NO", width=12, command=exit).grid(row=0, column=1)
def active_shooter():
    #clear window
    GUIFrame0.grid_remove()
    GUIFrame1.grid_remove()
    GUIFrame2.grid_remove()
    GUIFrame3.grid_remove()
    GUIFrame4.grid_remove()
    # add a name
    Label(main, text="                            HELP IS ON THE WAY!                                ").grid(row=0, column=0)
    print("Insert Active Shooter communication here")
    
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
#Frame Lockout
GUIFrame5 = Frame(main)
GUIFrame5.grid(row=5, column=0)
#Frame Lockout
GUIFrame6 = Frame(main)
GUIFrame6.grid(row=6, column=0)

#add a name
Label(GUIFrame0, text="What is your Emergency?").grid(row=0, column=0)

#add buttons
Button(GUIFrame1, text="Lock Out", width=12, command=are_you_sure_lockout).grid(row=0, column=0)
Button(GUIFrame1, text="Shelter in Place", width=12, command=are_you_sure_shelter).grid(row=0, column=1)
Button(GUIFrame2, text="Evacuate", width=12, command=are_you_sure_evacuate).grid(row=0, column=0)
Button(GUIFrame2, text="Medical", width=12, command=are_you_sure_medical).grid(row=0, column=1)
Button(GUIFrame3, text="Lock Down", width=24, command=are_you_sure_lockdown).grid(row=0, column=0)
Button(GUIFrame4, text="Active Shooter", width=24, command=are_you_sure_shooter).grid(row=0, column=0)
main.mainloop()