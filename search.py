import tkinter
import tkinter as tk
import os
gui = tk.Tk()



gui.geometry("1920x1080")
gui.title("Devkit - Database Search")



search = tk.Entry()
search.grid()

searchExec = tk.Button(text="Submit Query", command=seachdb)
searchExec.grid()

gui.mainloop()




#search bar RegEx