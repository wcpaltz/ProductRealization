# Import socket module 
import socket 

# Import thread module 
from _thread import *
import threading 

# Google Maps
#from googlemaps import *
#from keys import google_api_key
    
# Other imports
import time
#from tkinter import *
from tkinter import *
    
# IP (local host)
# this can be changed
host = '127.0.0.1'

# Define port that's to be connected to
port = 49000

emergency = "Currently No Emergency Has Been Detected"
root = Tk()
current_frame = Frame(root)
#label_1 = Label(root, text='Emergency').pack()

# main frames
f1, f2, f3 = Frame(root), Frame(root), Frame(root)

# lockout frames
f4, f5, f19, f20 = Frame(root), Frame(root), Frame(root), Frame(root)

# shelter frames
f6, f7, f25, f26 = Frame(root), Frame(root), Frame(root), Frame(root)

# evacuate frames
f8, f9, f27 = Frame(root), Frame(root), Frame(root)
h = StringVar()

# medical frames
f10, f11, f21, f22 = Frame(root), Frame(root), Frame(root), Frame(root)
d = StringVar()
e = StringVar()
f = StringVar()
g = StringVar()

# lockdown frames
f12, f13, f17, f18 = Frame(root), Frame(root), Frame(root), Frame(root)

# active shooter frames
f14, f15, f16, f23, f24 = Frame(root), Frame(root), Frame(root), Frame(root), Frame(root)
a = StringVar()
b = StringVar()
c = StringVar()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# connect to server with local IP
s.connect((host,port))

def gui_class():
    global emergency
    global root
    global f1, f2, f3, f4, f5, f6, f7, f8, f9, f10
    global f11, f12, f13, f14, f15, f16, f17, f18
    global f19, f20, f21, f22, f23, f24, f25, f26, f27
    global current_frame
    
    def raise_frame(frame, message):
        global current_frame
        current_frame = frame
        print("Message: " + str(message))
        if(message != "skip" and message != "na"):
            send_alert(message)
        frame.tkraise()

    for frame in (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27):
        frame.grid(row=0, column=0, sticky='news')

    """""""""""""""""""""""""""""""""""""""""""""
                    Main Screen
    """""""""""""""""""""""""""""""""""""""""""""
    Label(f1, text='What is your emergency?').pack()
    Button(f1, text='Lock Out', command=lambda:raise_frame(f4, "na")).pack()
    Button(f1, text='Shelter', command=lambda:raise_frame(f6, "na")).pack()
    Button(f1, text='Evacuate', command=lambda:raise_frame(f8, "na")).pack()
    Button(f1, text='Medical', command=lambda:raise_frame(f10, "na")).pack()
    Button(f1, text='Lock Down', command=lambda:raise_frame(f12, "na")).pack()
    Button(f1, text='Active Shooter', command=lambda:raise_frame(f14, "na")).pack()
    Button(f1, text='Reset App', command=lambda:raise_frame(f1, "reset")).pack()

    # Lockout
    Label(f4, text='Are you sure you want to lock out?').pack()
    Button(f4, text='Yes', command=lambda:raise_frame(f5, "lockout")).pack()
    Button(f4, text='No', command=lambda:raise_frame(f3, "skip")).pack()
    
    # Shelter in place
    Label(f6, text='Are you sure you want to shelter?').pack()
    Button(f6, text='Yes', command=lambda:raise_frame(f7, "shelter")).pack()
    Button(f6, text='No', command=lambda:raise_frame(f3, "skip")).pack()
    
    # Evacuate
    Label(f8, text='Are you sure you want to evacuate?').pack()
    Button(f8, text='Yes', command=lambda:raise_frame(f9, "evacuate")).pack()
    Button(f8, text='No', command=lambda:raise_frame(f3, "skip")).pack()
    
    # Medical
    Label(f10, text='Are you sure you want to call medical?').pack()
    Button(f10, text='Yes', command=lambda:raise_frame(f11, "medical")).pack()
    Button(f10, text='No', command=lambda:raise_frame(f3, "skip")).pack() 
    
    # Lockdown
    Label(f12, text='Are you sure you want to lockdown?').pack()
    Button(f12, text='Yes', command=lambda:raise_frame(f13, "lockdown")).pack()
    Button(f12, text='No', command=lambda:raise_frame(f3, "skip")).pack()
    
    # Active Shooter
    Label(f14, text='Are you sure you want to activate active shooter?').pack()
    Button(f14, text='Yes', command=lambda:raise_frame(f23, "activeshooter")).pack()
    Button(f14, text='No', command=lambda:raise_frame(f3, "skip")).pack()
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
    Label(f5, text='3.) Take attendance and report any discrepancies.').pack()
    Label(f5, text='4.) If possible, return to normal classroom activity.').pack()
    Label(f5, text='Are you in your classroom?').pack()
    Button(f5, text='Yes', command=lambda:raise_frame(f19, "Yes - In Classroom")).pack()
    Button(f5, text='No', command=lambda:raise_frame(f19, "No - Not in Classroom")).pack()
    Label(f19, text='More detailed report: ').pack()
    lo_text = Text(f19, height=2, width=30, borderwidth=1, relief="solid")
    lo_text.pack()
    Button(f19, text='Next', command=lambda:raise_frame(f20, "Details: " + str(lo_text.get("1.0",END + "-1c")))).pack()
    Label(f20, text='Help is on its way!').pack()
    Button(f20, text='Okay', command=lambda:raise_frame(f2, "send")).pack()   
    
    # Shelter in place
    Label(f7, text='Please proceed to designated shelter location.').pack()
    Label(f7, text='Is anyone injured?').pack()
    Button(f7, text='Yes', command=lambda:raise_frame(f25, "Yes - Injuries")).pack()
    Button(f7, text='No', command=lambda:raise_frame(f25, "No - No Injuries")).pack()
    Label(f25, text='More detailed report:').pack()
    s_text = Text(f25, height=2, width=30, borderwidth=1, relief="solid")
    s_text.pack()
    Button(f25, text='Next', command=lambda:raise_frame(f26, "Details: " + str(s_text.get("1.0",END + "-1c")))).pack()
    Label(f26, text='Stay in shelter location until informed of all clear.').pack()
    Button(f26, text='Okay', command=lambda:raise_frame(f2, "send")).pack()
    
    # Evacuate
    Label(f9, text='Location to evacuate?').pack()
    Entry(f9, textvariable = h).pack()
    Button(f9, text='Submit', command=lambda:raise_frame(f27, str("Location: " + h.get()))).pack()
    Label(f27, text='Avoid location until informed of all clear.').pack()
    Button(f27, text='Okay', command=lambda:raise_frame(f2, "send")).pack()
    
    # Medical
    Label(f11, text='What is the medical emergency?').pack()
    Entry(f11, textvariable = d).pack()
    Button(f11, text='Okay', command=lambda:raise_frame(f21, "Details: " + str(d.get()))).pack()
    Label(f21, text='Where are you?').pack()
    Label(f21, text='Building:').pack()
    Entry(f21, textvariable = e).pack()
    Label(f21, text='Floor:').pack()
    Entry(f21, textvariable = f).pack()
    Label(f21, text='Room:').pack()
    Entry(f21, textvariable = g).pack()
    Button(f21, text='Submit', command=lambda:raise_frame(f22, str("Building:" + e.get()) + " Floor:" + str(f.get()) + " Room:" + str(g.get()))).pack()
    Label(f22, text='Help is on its way!').pack()
    Button(f22, text='Okay', command=lambda:raise_frame(f2, "send")).pack()
    
    # Lockdown
    Label(f13, text='Please follow the steps below:').pack()
    Label(f13, text='1.) Close and lock all doors.').pack()
    Label(f13, text='2.) Turn off the lights.').pack()
    Label(f13, text='3.) Leave the corridor window uncovered.').pack()
    Label(f13, text='4.) Be silent and mute mobile phones.').pack()
    Label(f13, text='5.) Take attendance and report any discrepancies.').pack()
    Label(f13, text='Are you in the classroom?').pack()
    Button(f13, text='Yes', command=lambda:raise_frame(f17, "Yes - In Classroom")).pack()
    Button(f13, text='No', command=lambda:raise_frame(f17, "No - Not in Classroom")).pack()
    Label(f17, text='More detailed report:').pack()
    ld_text = Text(f17, height=2, width=30, borderwidth=1, relief="solid")
    ld_text.pack()
    Button(f17, text='Next', command=lambda:raise_frame(f18, "Details: " + str(ld_text.get("1.0",END + "-1c")))).pack()
    Label(f18, text='Help is on its way!').pack()
    Button(f18, text='Okay', command=lambda:raise_frame(f2, "send")).pack()
    
    # Active Shooter
    Label(f23, text='Is anyone injured?').pack()
    Button(f23, text='Yes', command=lambda:raise_frame(f24, "Yes - Injuries")).pack()
    Button(f23, text='No', command=lambda:raise_frame(f24, "No - No Injuries")).pack()
    Label(f24, text='More detailed report:').pack()
    ac_text = Text(f24, height=2, width=30, borderwidth=1, relief="solid")
    ac_text.pack()
    Button(f24, text='Next', command=lambda:raise_frame(f15, "Details: " + str(ac_text.get("1.0",END + "-1c")))).pack()
    Label(f15, text='Where are you?').pack()
    Label(f15, text='Building:').pack()
    Entry(f15, textvariable = a).pack()
    Label(f15, text='Floor:').pack()
    Entry(f15, textvariable = b).pack()
    Label(f15, text='Room:').pack()
    Entry(f15, textvariable = c).pack()
    Button(f15, text='Submit', command=lambda:raise_frame(f16, str("Building:" + a.get()) + " Floor:" + str(b.get()) + " Room:" + str(c.get()))).pack()
    Label(f16, text='Help is on its way!').pack()
    Button(f16, text='Okay', command=lambda:raise_frame(f2, "send")).pack()
    """""""""""""""""""""""""""""""""""""""""""""
    END OF FRAMES THAT ARE DEPENDANT ON EMERGENCY
    """""""""""""""""""""""""""""""""""""""""""""
    
    """""""""""""""""""""""""""""""""""""""""""""
                    ENDING FRAMES
    """""""""""""""""""""""""""""""""""""""""""""
    # Send information
    Label(f2, text='Thank You!').pack()
    Label(f2, text='Your response has been recorded.').pack()
    Button(f2, text='Close App', command=root.destroy).pack()
    Button(f2, text='Home Screen', command=lambda:raise_frame(f1, "na")).pack()
    
    # Do not send information
    Label(f3, text='No information has been sent.').pack()
    Button(f3, text='Close App', command=root.destroy).pack()
    Button(f3, text='Home Screen', command=lambda:raise_frame(f1, "na")).pack()
    """""""""""""""""""""""""""""""""""""""""""""
                END OF ENDING FRAMES
    """""""""""""""""""""""""""""""""""""""""""""
    
    raise_frame(f1, "na")
    start_new_thread(update_alert, (root,))
    root.mainloop()
    

def update_alert(self):
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
#                print("New emergency: " + str(emergency))
                label_1.pack_forget()
                label_1 = Label(current_frame, text=(str(emergency)))
                label_1.pack()
                old_frame = current_frame
            old_emergency = emergency
            time.sleep(0.1)
        s.close() # close the connection 
    except:
        # if exception occurs
        print("Error with emergency thread")
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
    s.close() # close the connection 
#    grab_location()


def send_alert(message):
    s.send(message.encode('ascii'))
    
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
    except:
        # if exception occurs
#        print("Error with receiving data to client")
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