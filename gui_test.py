from tkinter import *


def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Label(f1, text='What is your emergency?').pack()
Button(f1, text='Lock Out', command=lambda:raise_frame(f2)).pack()

Label(f2, text='Are you sure you want to lock out?').pack()
Button(f2, text='Yes', command=lambda:raise_frame(f3)).pack()
Button(f2, text='No', command=lambda:raise_frame(f3)).pack()

Label(f3, text='Please follow the steps below:').pack()
Label(f3, text='1.) Bring everyone inside').pack()
Label(f3, text='2.) Lock outside door').pack()
Label(f3, text='3.) Increase your awareness').pack()
Label(f3, text='4.) Take Attendance').pack()
Label(f3, text='Are you in your classroom?').pack()
Button(f3, text='Yes', command=lambda:raise_frame(f4)).pack()
Button(f3, text='No', command=lambda:raise_frame(f4)).pack()

Label(f4, text='Information has been sent').pack()
Button(f4, text='Close App', command=root.destroy).pack()

raise_frame(f1)
root.mainloop()