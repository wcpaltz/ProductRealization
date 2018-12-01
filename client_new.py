# Import socket module 
import socket 

# Import thread module 
from _thread import *
import threading 

# Other imports
import time
#from tkinter import *
from tkinter import *
    
# IP (local host)
# this can be changed
host = '127.0.0.1'

# Define port that's to be connected to
port = 49000

gui_count = 0
received = False
emergency = "Currently No Emergency Has Been Detected"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# connect to server with local IP
s.connect((host,port))

def gui_class():
    global emergency

    def raise_frame(frame, message):
        global gui_count
        gui_count += 1
        print("Message: " + str(message))
        if(message != "skip" and message != "na"):
            send_alert(message)
        print("GUI count: " +str(gui_count))
        frame.tkraise()
        
    root = Tk()

    # main frames
    f1, f2, f3 = Frame(root), Frame(root), Frame(root)
    
    # lockout frames
    f4, f5 = Frame(root), Frame(root)
    
    # shelter frames
    f6, f7 = Frame(root), Frame(root)
    
    # evacuate frames
    f8, f9 = Frame(root), Frame(root)
    
    # medical frames
    f10, f11 = Frame(root), Frame(root)
    v = StringVar()
    
    # lockdown frames
    f12, f13 = Frame(root), Frame(root)
    
    # active shooter frames
    f14, f15 = Frame(root), Frame(root)
    
    for frame in (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15):
        frame.grid(row=0, column=0, sticky='news')

    # Main Screen
    Label(f1, text='What is your emergency?').pack()
    Button(f1, text='Lock Out', command=lambda:raise_frame(f4, "na")).pack()
    Button(f1, text='Shelter in Place', command=lambda:raise_frame(f6, "na")).pack()
    Button(f1, text='Evacuate', command=lambda:raise_frame(f8, "na")).pack()
    Button(f1, text='Medical', command=lambda:raise_frame(f10, "na")).pack()
    Button(f1, text='Lock Down', command=lambda:raise_frame(f12, "na")).pack()
    Button(f1, text='Active Shooter', command=lambda:raise_frame(f14, "na")).pack()
    
    # Verify
    # Lockout
    Label(f4, text='Are you sure you want to lock out?').pack()
    Button(f4, text='Yes', command=lambda:raise_frame(f5, "lockout")).pack()
    Button(f4, text='No', command=lambda:raise_frame(f3, "skip")).pack()
    # Shelter in place
    Label(f6, text='Are you sure you want to shelter in place?').pack()
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
    Button(f14, text='Yes', command=lambda:raise_frame(f15, "lockdown")).pack()
    Button(f14, text='No', command=lambda:raise_frame(f3, "skip")).pack()
    
    # Steps to follow - frame dependent
    # Lockout
    Label(f5, text='Please follow the steps below:').pack()
    Label(f5, text='1.) Bring everyone inside').pack()
    Label(f5, text='2.) Lock outside door').pack()
    Label(f5, text='3.) Increase your awareness').pack()
    Label(f5, text='4.) Take Attendance').pack()
    Label(f5, text='Are you in your classroom?').pack()
    Button(f5, text='Yes', command=lambda:raise_frame(f2, "na")).pack()
    Button(f5, text='No', command=lambda:raise_frame(f2, "na")).pack()
    # Shelter in place
    Label(f7, text='Reason for shelter in place?').pack()
    Button(f7, text='Tornado', command=lambda:raise_frame(f2, "Tornado")).pack()
    Button(f7, text='Hazmat', command=lambda:raise_frame(f2, "Hazmat")).pack()
    Button(f7, text='Earthquake', command=lambda:raise_frame(f2, "Earthquake")).pack()
    Button(f7, text='Tsunami', command=lambda:raise_frame(f2, "Tsunami")).pack()
    # Evacuate
    Label(f9, text='Please follow the steps below:').pack()
    Label(f9, text='1.) Run').pack()
    Label(f9, text='2.) Keep Running').pack()
    Label(f9, text='3.) Keep Running!').pack()
    Button(f9, text='Okay', command=lambda:raise_frame(f2, "na")).pack()
    # Medical
    Label(f11, text='What is the medical emergency?').pack()
    Entry(f11, textvariable = v).pack()
    Button(f11, text='Okay', command=lambda:raise_frame(f2, v.get())).pack()
    # Lockdown
    Label(f13, text='Reason for Lock Down?').pack()
    Button(f13, text='Fight', command=lambda:raise_frame(f2, "Fight")).pack()
    Button(f13, text='Dangerous Person Inside', command=lambda:raise_frame(f2, "DPI")).pack()
    Button(f13, text='Dangerous Animal Inside', command=lambda:raise_frame(f2, "DAI")).pack()
    # Active Shooter
    Label(f15, text='Help is on its way!').pack()
    Button(f15, text='Okay', command=lambda:raise_frame(f2, "na")).pack()
    
    # Send information
    Label(f2, text='Information has been sent').pack()
    Button(f2, text='Close App', command=root.destroy).pack()
    
    # Do not send information
    Label(f3, text='No information has been sent').pack()
    Button(f3, text='Close App', command=root.destroy).pack()

    raise_frame(f1, "na")
    root.mainloop()

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
    global emergency
    
    start_new_thread(receive_data, (s,))
    gui_class()
    
#    while True:
#        # message you received from server 
#        message = input('Enter Emergency Below: \n')
#        
#        # send message to server
#        s.send(message.encode('ascii')) 
#
#        # sleep to receive data from server
#        # since it is on another thread
#        time.sleep(1)
#        
#        # client want to continue?
#        ans = input('\nIs the emergency still happening? (y/n) :') 
#        if ans == 'y': 
#            continue
#        else:
#            break
            
    s.close() # close the connection 


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
            # messaga received from server
            data = s.recv(1024)
            received = True
            emergency = "EMERGENCY DETECTED: " + str(data.decode('ascii'))
            if not data:
                break
            # print the received message 
            # here it would be a reverse of sent message 
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