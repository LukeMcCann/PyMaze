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


# add a combobox - location selection
city = tk.StringVar()
citySelected = ttk.Combobox(weather_conditions_frame, width=15, textvar = city)

citySelected['values'] = ('Leeds', 'Manchester', 'London', 'Bristol', 'Birmingham')

citySelected.grid(column=1, row=0)
citySelected.current(0)

# set max combobox length to the length of the longest value
max_width  = max([len(x)for x in citySelected['values']])
new_width = max_width
citySelected.config(width=new_width)

ENTRY_WIDTH = max_width + 3 

# Label and textBox widgets
ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='W')
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='W')               # <== increment row for each
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')                                  # <== increment row for each
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='W')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row=3, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Dewpoint:").grid(column=0, row=4, sticky='W')
dew = tk.StringVar()
dewEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=dew, state='readonly')
dewEntry.grid(column=1, row=4, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='W')
rel_humi = tk.StringVar()
rel_humiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=rel_humi, state='readonly')
rel_humiEntry.grid(column=1, row=5, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Wind:").grid(column=0, row=6, sticky='W')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=6, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Visibility:").grid(column=0, row=7, sticky='W')
visi = tk.StringVar()
visiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=visi, state='readonly')
visiEntry.grid(column=1, row=7, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="MSL Pressure:").grid(column=0, row=8, sticky='W')
msl = tk.StringVar()
mslEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=msl, state='readonly')
mslEntry.grid(column=1, row=8, sticky='W')
#---------------------------------------------
ttk.Label(weather_conditions_frame, text="Altimeter:").grid(column=0, row=9, sticky='W')
alti = tk.StringVar()
altiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=alti, state='readonly')
altiEntry.grid(column=1, row=9, sticky='W')
# App Start
win.mainloop()