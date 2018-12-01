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
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# connect to server with local IP
s.connect((host,port))

def gui_class():
    def raise_frame(frame, skip):
        global gui_count
        gui_count += 1
        if(gui_count == 3 and skip != "skip"):
            lockout()
        print("GUI count: " +str(gui_count))
        frame.tkraise()
        
    root = Tk()

    # main frame
    f1 = Frame(root)
    
    # lockout frames
    f2, f3, f4, f5 = Frame(root), Frame(root), Frame(root), Frame(root)
    
    # shelter frames
    f6, f7, f8, f9 = Frame(root), Frame(root), Frame(root), Frame(root)

    for frame in (f1, f2, f3, f4, f5, f6):
        frame.grid(row=0, column=0, sticky='news')

    # Main Screen
    Label(f1, text='What is your emergency?').pack()
    Button(f1, text='Lock Out', command=lambda:raise_frame(f2, "na")).pack()
    Button(f1, text='Shelter in Place', command=lambda:raise_frame(f6, "na")).pack()
    Button(f1, text='Evacuate', command=lambda:raise_frame(f2, "na")).pack()
    Button(f1, text='Medical', command=lambda:raise_frame(f2, "na")).pack()
    Button(f1, text='Lock Down', command=lambda:raise_frame(f2, "na")).pack()
    Button(f1, text='Active Shooter', command=lambda:raise_frame(f2, "na")).pack()
    
    # Verify
    # Lockout
    Label(f2, text='Are you sure you want to lock out?').pack()
    Button(f2, text='Yes', command=lambda:raise_frame(f3, "na")).pack()
    Button(f2, text='No', command=lambda:raise_frame(f5, "skip")).pack()
    # Shelter in place
    Label(f6, text='Are you sure you want to shelter in place?').pack()
    Button(f6, text='Yes', command=lambda:raise_frame(f3, "na")).pack()
    Button(f6, text='No', command=lambda:raise_frame(f5, "skip")).pack()
    
    
    # Steps to follow - frame dependent
    # Lockout
    Label(f3, text='Please follow the steps below:').pack()
    Label(f3, text='1.) Bring everyone inside').pack()
    Label(f3, text='2.) Lock outside door').pack()
    Label(f3, text='3.) Increase your awareness').pack()
    Label(f3, text='4.) Take Attendance').pack()
    Label(f3, text='Are you in your classroom?').pack()
    Button(f3, text='Yes', command=lambda:raise_frame(f4, "na")).pack()
    Button(f3, text='No', command=lambda:raise_frame(f4, "na")).pack()

    Label(f4, text='Information has been sent').pack()
    Button(f4, text='Close App', command=root.destroy).pack()
    
    Label(f5, text='No information has been sent').pack()
    Button(f5, text='Close App', command=root.destroy).pack()

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
    gui_class()
    
    start_new_thread(receive_data, (s,))
    
    while True:
        # message you send to server 
        message = input('Enter Emergency Below: \n')
        
        # send message to server
        s.send(message.encode('ascii')) 

        # sleep to receive data from server
        # since it is on another thread
        time.sleep(1)
        
        # client want to continue?
        ans = input('\nIs the emergency still happening? (y/n) :') 
        if ans == 'y': 
            continue
        else:
            break
            
    s.close() # close the connection 


def lockout():
    message = "lockout"
    s.send(message.encode('ascii'))
    
def shelter():
    message = "shelter"
    s.send(message.encode('ascii'))
    
def evacuate():
    message = "evacuate"
    s.send(message.encode('ascii'))
    
def medical():
    message = "medical"
    s.send(message.encode('ascii'))
    
def lockdown():
    message = "lockdown"
    s.send(message.encode('ascii'))
    
def active():
    message = "active"
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
    try:
        while True:
            # messaga received from server
            data = s.recv(1024)
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