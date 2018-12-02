from tkinter import *
from client_new import main
#import server_new
root = Tk()
f1 = Frame(root)

def Main():
    def raise_frame(frame):
        frame.tkraise()
    
    f1.grid(row=0, column=0, sticky='news')
        
    Label(f1, text='Create server or client?').pack()
    Label(f1, text='Only one server can be active at a time').pack()
    Button(f1, text='Server', command=lambda:server_new.main()).pack()
    Button(f1, text='Client', command=lambda:client_new.main()).pack()
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