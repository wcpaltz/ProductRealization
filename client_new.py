"""""""""""""""""""""""""""""""""""""""""""""
                Imports
"""""""""""""""""""""""""""""""""""""""""""""
# Import socket module 
import socket 

# Import thread module 
from _thread import *
import threading 

# Other imports
import time
import os
import platform
from tkinter import *

"""""""""""""""""""""""""""""""""""""""""""""
            Define Global Variables
"""""""""""""""""""""""""""""""""""""""""""""
#ip_con = "172.20.10.10"
#host = ip_con
host = "Wills-MacBook-Pro.local"

# Define port that's to be connected to
port = 49000

emergency = "Currently No Emergency Has Been Detected"

# Create GUI root
root = Tk()
root.resizable(width=False, height=False)
current_frame = Frame(root)
frame_array = []

# main frames
f1, f2, f3 = Frame(root), Frame(root), Frame(root)
frame_array.extend([f1, f2, f3])

# lockout frames
f4, f5, f6, f7 = Frame(root), Frame(root), Frame(root), Frame(root)
frame_array.extend([f4, f5, f6, f7])

# shelter frames
f8, f9, f10, f11 = Frame(root), Frame(root), Frame(root), Frame(root)
frame_array.extend([f8, f9, f10, f11])

# evacuate frames
f12, f13, f14 = Frame(root), Frame(root), Frame(root)
evac_a = StringVar()
frame_array.extend([f12, f13, f14])

# medical frames
f15, f16, f17, f18 = Frame(root), Frame(root), Frame(root), Frame(root)
med_a, med_b, med_c, med_d = StringVar(), StringVar(), StringVar(), StringVar()
frame_array.extend([f15, f16, f17, f18])

# lockdown frames
f19, f20, f21, f22 = Frame(root), Frame(root), Frame(root), Frame(root)
frame_array.extend([f19, f20, f21, f22])

# active shooter frames
f23, f24, f25, f26, f27 = Frame(root), Frame(root), Frame(root), Frame(root), Frame(root)
ac_a, ac_b, ac_c = StringVar(), StringVar(), StringVar()
frame_array.extend([f23, f24, f25, f26, f27])

# Create socket connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

try:
    # connect to server with local IP
    s.connect((host,port))
except Exception as e:
    print("Could not connect to server: " + str(e))
    exit()

"""""""""""""""""""""""""""""""""""""""""""""
    Define Global Variables Completed
"""""""""""""""""""""""""""""""""""""""""""""

def gui_class():
    """
    Functionality:
        Needed a simple way to create a GUI. This function will 
        create and manage the GUI as the user interacts. The idea
        of frames is utilized to manage the GUI class. The GUI 
        communicates with the server to send different types
        of emergencies.
    Input:
        N/A
    Output:
        N/A
    """
    global emergency
    global root
    global frame_array
    global current_frame
    
    def raise_frame(frame, message):
        """
        Functionality:
            Needed a simple way to create and manage the frames of the GUI. 
            This is done by utilizing a current frame architecture and
            receiving info from frames whenever they are communicated
            with by the user. Each frame is based in the root of the GUI.
            Whenever a message is receieved that does not include "skip"
            or "na" a message will be sent to the server.
        Input:
            frame   : Frame
            message : String
        Output:
            N/A
        """
        global current_frame
        current_frame = frame
        if(message != "skip" and message != "na"):
            send_alert(message)
        frame.tkraise()

    for frame in frame_array:
        frame.grid(row=0, column=0, sticky='news')

    """""""""""""""""""""""""""""""""""""""""""""
                    Main Screen
    """""""""""""""""""""""""""""""""""""""""""""
    Label(f1, text='What is your emergency?').pack(side=TOP)
    Button(f1, text='Lock Out', width=10, command=lambda:raise_frame(f4, "na")).pack(padx=5, pady=2)
    Button(f1, text='Shelter', width=10, command=lambda:raise_frame(f8, "na")).pack(padx=5, pady=2)
    Button(f1, text='Evacuate', width=10, command=lambda:raise_frame(f12, "na")).pack(padx=5, pady=2)
    Button(f1, text='Medical', width=10, command=lambda:raise_frame(f15, "na")).pack(padx=5, pady=2)
    Button(f1, text='Lock Down', width=10, command=lambda:raise_frame(f19, "na")).pack(padx=5, pady=2)
    Button(f1, text='Active Shooter', width=10, command=lambda:raise_frame(f23, "na")).pack(padx=5, pady=2)
    Button(f1, text='Reset App', width=10, command=lambda:raise_frame(f1, "reset")).pack(padx=5, pady=2)

    # Lockout
    Label(f4, text='Are you sure you want to lock out?').pack()
    Button(f4, text='Yes', width=6, command=lambda:raise_frame(f5, "lockout")).pack()
    Button(f4, text='No', width=6, command=lambda:raise_frame(f3, "skip")).pack()
    
    # Shelter in place
    Label(f8, text='Are you sure you want to shelter?').pack()
    Button(f8, text='Yes', width=6, command=lambda:raise_frame(f9, "shelter")).pack()
    Button(f8, text='No', width=6, command=lambda:raise_frame(f3, "skip")).pack()
    
    # Evacuate
    Label(f12, text='Are you sure you want to evacuate?').pack()
    Button(f12, text='Yes', width=6, command=lambda:raise_frame(f13, "evacuate")).pack()
    Button(f12, text='No', width=6, command=lambda:raise_frame(f3, "skip")).pack()
    
    # Medical
    Label(f15, text='Are you sure you want to call medical?').pack()
    Button(f15, text='Yes', width=6, command=lambda:raise_frame(f16, "medical")).pack()
    Button(f15, text='No', width=6, command=lambda:raise_frame(f3, "skip")).pack() 
    
    # Lockdown
    Label(f19, text='Are you sure you want to lockdown?').pack()
    Button(f19, text='Yes', width=6, command=lambda:raise_frame(f20, "lockdown")).pack()
    Button(f19, text='No', width=6, command=lambda:raise_frame(f3, "skip")).pack()
    
    # Active Shooter
    Label(f23, text='Are you sure you want to activate active shooter?').pack()
    Button(f23, text='Yes', width=6, command=lambda:raise_frame(f24, "activeshooter")).pack()
    Button(f23, text='No', width=6, command=lambda:raise_frame(f3, "skip")).pack()
    """""""""""""""""""""""""""""""""""""""""""""
            END OF MAIN EMERGENCY SCREENS
    """""""""""""""""""""""""""""""""""""""""""""
    
    """""""""""""""""""""""""""""""""""""""""""""
        Steps to follow - Frame Dependent
    """""""""""""""""""""""""""""""""""""""""""""
    # Lockout
    Label(f5, text='Please follow the steps below:').pack()
    Label(f5, text='1.) Bring everyone inside.').pack()
    Label(f5, text='2.) Lock perimeter door.').pack()
    Label(f5, text='3.) Take attendance and report\nany discrepancies.').pack()
    Label(f5, text='4.) If possible, return to\nnormal classroom activity.\n').pack()
    Label(f5, text='Are you in your classroom?').pack()
    Button(f5, text='Yes', width=6, command=lambda:raise_frame(f6, "Yes - In Classroom")).pack()
    Button(f5, text='No', width=6, command=lambda:raise_frame(f6, "No - Not in Classroom")).pack()
    Label(f6, text='More detailed report: ').pack()
    lo_text = Text(f6, height=2, width=30, borderwidth=1, relief="solid")
    lo_text.pack()
    Button(f6, text='Next', width=6, command=lambda:raise_frame(f7, "Details: " + str(lo_text.get("1.0",END + "-1c")))).pack()
    Label(f7, text='Help is on its way!').pack()
    Button(f7, text='Okay', width=6, command=lambda:raise_frame(f2, "send")).pack()   
    
    # Shelter in place
    Label(f9, text='Please proceed to designated shelter location.').pack()
    Label(f9, text='Is anyone injured?').pack()
    Button(f9, text='Yes', width=6, command=lambda:raise_frame(f10, "Yes - Injuries")).pack()
    Button(f9, text='No', width=6, command=lambda:raise_frame(f10, "No - No Injuries")).pack()
    Label(f10, text='More detailed report:').pack()
    s_text = Text(f10, height=2, width=30, borderwidth=1, relief="solid")
    s_text.pack()
    Button(f10, text='Next', width=6, command=lambda:raise_frame(f11, "Details: " + str(s_text.get("1.0",END + "-1c")))).pack()
    Label(f11, text='Stay in shelter location until informed of all clear.').pack()
    Button(f11, text='Okay', width=6, command=lambda:raise_frame(f2, "send")).pack()
    
    # Evacuate
    Label(f13, text='Location to evacuate from?').pack()
    Entry(f13, textvariable = evac_a).pack()
    Button(f13, text='Submit', width=6, command=lambda:raise_frame(f14, str("Location: " + evac_a.get()))).pack()
    Label(f14, text='Avoid location until informed of all clear.').pack()
    Button(f14, text='Okay', width=6, command=lambda:raise_frame(f2, "send")).pack()
    
    # Medical
    Label(f16, text='What is the medical emergency?').pack()
    Entry(f16, textvariable = med_a).pack()
    Button(f16, text='Okay', width=6, command=lambda:raise_frame(f17, "Details: " + str(med_a.get()))).pack()
    Label(f17, text='Where are you?').pack()
    Label(f17, text='Building:').pack()
    Entry(f17, textvariable = med_b).pack()
    Label(f17, text='Floor:').pack()
    Entry(f17, textvariable = med_c).pack()
    Label(f17, text='Room:').pack()
    Entry(f17, textvariable = med_d).pack()
    med_string = str(("Building:" +  med_b.get()) + " Floor:" + str(med_c.get()) + " Room:" + str(med_d.get()))
    Button(f17, text='Submit', width=6, command=lambda:raise_frame(f18, str(med_string))).pack()
    Label(f18, text='Help is on its way!').pack()
    Button(f18, text='Okay', width=6, command=lambda:raise_frame(f2, "send")).pack()
    
    # Lockdown
    Label(f20, text='Please follow the steps below:').pack()
    Label(f20, text='1.) Close and lock all doors.').pack()
    Label(f20, text='2.) Turn off the lights.').pack()
    Label(f20, text='3.) Leave the corridor\nwindow uncovered.').pack()
    Label(f20, text='4.) Be silent and mute\nmobile phones.').pack()
    Label(f20, text='5.) Take attendance and\nreport any discrepancies.\n').pack()
    Label(f20, text='Are you in the classroom?').pack()
    Button(f20, text='Yes', width=6, command=lambda:raise_frame(f21, "Yes - In Classroom")).pack()
    Button(f20, text='No', width=6, command=lambda:raise_frame(f21, "No - Not in Classroom")).pack()
    Label(f21, text='More detailed report:').pack()
    ld_text = Text(f21, height=2, width=30, borderwidth=1, relief="solid")
    ld_text.pack()
    Button(f21, text='Next', width=6, command=lambda:raise_frame(f22, "Details: " + str(ld_text.get("1.0",END + "-1c")))).pack()
    Label(f22, text='Help is on its way!').pack()
    Button(f22, text='Okay', width=6, command=lambda:raise_frame(f2, "send")).pack()
    
    # Active Shooter
    Label(f24, text='Is anyone injured?').pack()
    Button(f24, text='Yes', width=6, command=lambda:raise_frame(f25, "Yes - Injuries")).pack()
    Button(f24, text='No', width=6, command=lambda:raise_frame(f25, "No - No Injuries")).pack()
    Label(f25, text='More detailed report:').pack()
    ac_text = Text(f24, height=2, width=30, borderwidth=1, relief="solid")
    ac_text.pack()
    Button(f25, text='Next', width=6, command=lambda:raise_frame(f26, "Details: " + str(ac_text.get("1.0",END + "-1c")))).pack()
    Label(f26, text='Where are you?').pack()
    Label(f26, text='Building:').pack()
    Entry(f26, textvariable = ac_a).pack()
    Label(f26, text='Floor:').pack()
    Entry(f26, textvariable = ac_b).pack()
    Label(f26, text='Room:').pack()
    Entry(f26, textvariable = ac_c).pack()
    ac_string = str(("Building:" +  ac_a.get()) + " Floor:" + str(ac_b.get()) + " Room:" + str(ac_c.get()))
    Button(f26, text='Submit', width=6, command=lambda:raise_frame(f27, str(ac_string))).pack()
    Label(f27, text='Help is on its way!').pack()
    Button(f27, text='Okay', width=6, command=lambda:raise_frame(f2, "send")).pack()
    """""""""""""""""""""""""""""""""""""""""""""
    END OF FRAMES THAT ARE DEPENDANT ON EMERGENCY
    """""""""""""""""""""""""""""""""""""""""""""
    
    """""""""""""""""""""""""""""""""""""""""""""
                    ENDING FRAMES
    """""""""""""""""""""""""""""""""""""""""""""
    # Send information
    Label(f2, text='Thank You!').pack()
    Label(f2, text='Your response has been recorded.').pack()
    Button(f2, text='Close App', width=9, command=root.destroy).pack()
    Button(f2, text='Home Screen', width=9, command=lambda:raise_frame(f1, "na")).pack()
    
    # Do not send information
    Label(f3, text='No information has been sent.').pack()
    Button(f3, text='Close App', width=9, command=root.destroy).pack()
    Button(f3, text='Home Screen', width=9, command=lambda:raise_frame(f1, "na")).pack()
    """""""""""""""""""""""""""""""""""""""""""""
                END OF ENDING FRAMES
    """""""""""""""""""""""""""""""""""""""""""""
    
    raise_frame(f1, "na")
    start_new_thread(update_alert, (root,))
    root.mainloop()

def update_alert(self):
    """
    Functionality:
        Needed a simple way to update the current emergency alert.
        This is an essential part of the app so that users can
        be notified, at the bottom of the screen, whenever an emergency
        is ongoing.
    Input:
        self : Tk (Tkinter root)
    Output:
        N/A
    """
    global emergency
    global current_frame
    old_emergency = emergency
    old_frame = Frame(self)
    count = 0
    label_1 = Label(current_frame, text=(str(emergency)))
    label_1.pack()
    try:
        while True:
            if(old_frame != current_frame or old_emergency != emergency):
                label_1.pack_forget()
                label_1 = Label(current_frame, text=(str(emergency)))
                label_1.pack()
                old_frame = current_frame
            old_emergency = emergency
            time.sleep(0.1)
        s.close() # close the connection 
    except Exception as e:
        # if exception occurs
        print("Error with emergency thread: " + str(e))
        s.close() # close the connection 

#def grab_location():
#    gmaps = googlemaps.Client(key=google_api_key)
#    geocode_result = gmaps.geocode('23325')
#    print(geocode_result)
    
def Main():
    """
    Functionality:
        Needed a simple way to connect to a socket on a designated 
        server. This function will continue to loop until the 
        connection is closed, in which it will close the connection
        gracefully. A thread will also be created to receive data
        from the server. 
    Input:
        N/A
    Output:
        N/A
    """
    start_new_thread(receive_data, (s,))
    gui_class()
    # close the connection
    s.close()

def send_alert(message):
    """
    Functionality:
        Needed a simple way to send an alert to a server that is
        connected through the connection established.
    Input:
        message : String
    Output:
        N/A
    """
    try:
        s.send(message.encode('ascii'))
    except Exception as e:
        print("Could not send alert to server: " + str(e))
    
def receive_data(s):
    """
    Functionality:
        Needed a simple way asynchronously receive data from 
        the server the client is connected to. A new thread 
        is create since sending and receiving are two seperate 
        tasks. Without a tread the server would not be able to 
        send alerts to the client asynchronously. 
    Input:
        s : socket
    Output:
        N/A
    """
    global emergency
    try:
        while True:
            # message received from server
            data = s.recv(1024) 
            if(data.decode('ascii') == "reset"):
                emergency = "Currently No Emergency Has Been Detected"
            else:
                emergency = "EMERGENCY DETECTED: " + str(data.decode('ascii'))
            if not data:
                break
            # print the received message 
            print("\nALERT - " + str(data.decode('ascii')))    
        s.close() # close the connection 
    except Exception as e:
        # if exception occurs
        print("Error receiving data from server: " + str(e))
        s.close() # close the connection 

if __name__ == '__main__':
    """
    Functionality:
        Calls Main(), when script is called locally
    Input:
        N/A
    Output:
        N/A
    """
    Main()