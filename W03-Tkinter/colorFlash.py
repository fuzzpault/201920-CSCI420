'''
Name: Paul Talaga
Date: 1-30-2020
Desc: Flashes background color

'''

from tkinter import *
from random import *

master = Tk()

master.geometry("800x600")

colors = ["green","red",'blue','purple']
c = 0   # Keeps track of the current color index

def changeColor(event = None):
  global master
  global colors
  global c
  # Randomly pick the next color
  #master.configure(background = colors[randint(0,len(colors)-1)])
  # Rotate the colors
  master.configure(background = colors[c])
  c = c + 1
  c = c % len(colors)
  master.after(500, changeColor)  # Schedule the next funtion call.


master.after(10, changeColor)
#master.after(2000, changeColor)

mainloop()