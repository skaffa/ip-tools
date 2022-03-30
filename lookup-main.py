#from tkinter import *
import tkinter
import tkinter as tk
import os
from random import randint
import logger
import sessionTimer
import time
#import sessionTimer
gui = tk.Tk()
###Widgets Start###
log = logger.log
profiles = ''
lastPage = ''


def globalButtonColorReset():
    print("COLOR RESET TRIGGERED")
    profiles.configure(bg= "white")
    blacklist.configure(bg= "white")

def profiles():
    print('Clicked profiles')
    profiles.configure(bg = "black")

def blacklist():
    print('Clicked blacklist')
    self.globalButtonColorReset
    blacklist.configure(bg = "black")

def scripts():
    pass

def statistics():
    pass

sessionTimerElement = tk.Label(gui, text=randint(10,10000))

def Refresher():
    global gui
    global sessionTimerElement
    sessionTimerElement.configure(text=time.time())
    gui.after(1000, Refresher) 


gui.geometry("1920x1080")
gui.title("Devkit - ip-tools")

profiles = tk.Button(gui, text='Profiles', cursor="center_ptr", command=lambda:[profiles(), globalButtonColorReset()])
profiles.grid(ipadx=1, ipady=1, columnspan=20, sticky="WE")


blacklist = tk.Button(gui,cursor="center_ptr", text='Blacklist', command=lambda:[blacklist, globalButtonColorReset])
blacklist.grid(ipadx=1, ipady=1, columnspan=20, sticky="WE")

tool3 = tk.Button(gui,text="Scripts", cursor="center_ptr",command=lambda:[scripts, globalButtonColorReset])
tool3.grid(ipadx=1, ipady=1, columnspan=20, sticky="WE")

tool2 = tk.Button(gui, text="Statistics", cursor="center_ptr",command=lambda:[statistics, globalButtonColorReset])
tool2.grid(ipadx=1, ipady=1, columnspan=20, sticky="WE")



version = tk.Label(gui, text='Session ID: ' + logger.sessionID)
version.grid(ipadx=1,ipady=1,columnspan=20, sticky="SE")
print(sessionTimer.timer)



###Widgets End###
Refresher()
gui.mainloop()