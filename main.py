from tkinter import *
from client import Main as clie
root = Tk()
f1 = Frame(root)

# Import thread module 
from _thread import *
import threading 

def Main():
    def raise_frame(frame):
        frame.tkraise()
    
    f1.grid(row=0, column=0, sticky='news')
        
    Label(f1, text='Create client instance?').pack()
    Label(f1, text='Only one server can be active at a time').pack()
    Button(f1, text='Client', command=lambda:start_new_thread(clie())).pack()
    Button(f1, text='Close App', command=root.destroy).pack()
    
    raise_frame(f1)
    root.mainloop()
    
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