'''
Created on 2 Feb 2019

@author: Devel
'''
import tkinter as tk 

win = tk.Tk()

win.title("My First GUI in Python!")
win.minsize(500, 500)

# disable resizing of window
win.resizable(0, 0)
win.mainloop()