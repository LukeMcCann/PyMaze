'''
Created on 2 Feb 2019

@author: Devel
'''
import tkinter as tk
from tkinter import Menu, mainloop
from tkinter import ttk  # themed tk 

### functions
def _quit():
    win.quit()
    win.destroy()
    exit()
    
    
win = tk.Tk()
win.minsize(500, 500)
win.title("Python GUI")

menuBar = Menu()
win.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = "New")
fileMenu.add_separator()
fileMenu.add_command(label= "Exit", command = _quit)
menuBar.add_cascade(label = "File", menu = fileMenu)



mainloop()