'''
Created on 2 Feb 2019

@author: Devel
'''
import tkinter as tk
from tkinter import Menu, mainloop
from tkinter import ttk  # themed tk 

def _quit():
    win.quit()      
    win.destroy()
    exit() 


win = tk.Tk()         
win.title("Python Projects")
win.minsize(200, 200)

menuBar = Menu()
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# Tab Control
tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
  
# container frame for widgets
weather_conditions_frame = ttk.LabelFrame(
    tab1, text=' Current Weather Conditions ')

# tkinter grid layout manager
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(weather_conditions_frame, 
          text="Location:").grid(column=0, row=0, sticky='W')


# App Start
win.mainloop()