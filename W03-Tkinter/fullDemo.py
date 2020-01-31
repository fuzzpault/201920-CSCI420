'''
Name: Paul Talaga
Date: 1-30-2020
Desc: Full TKinter code, which implements a calculator, text box, and color flasher.

'''
from tkinter import *
from random import *

master = Tk()

computation = ""

def wasClicked(event = None):
  #print(str(dir(event.widget)))
  global computation
  print("you clicked on {}".format(event.widget.mynumber))
  computation += str(event.widget.mynumber)
  print("computation is now {}".format(computation))

def doComputation(event = None):
  global computation
  print(eval(computation))
  computation = ""

def boxStuff(event = None):
  print(dir(event.widget))
  print(event.widget.get())
  event.widget.insert(0,"You typed enter")

colors = ["green","red",'blue']

def changeColor(event = None):
  global master
  global colors
  master.configure(background = colors[randint(0,len(colors)-1)])
  master.after(10, changeColor)


for i in range(10):
  box = Label(master,text = "This is a box")
  box.grid(column=0, row=i)
  button = Button(master,text=i)
  button.grid(column=1, row=i)
  button.bind('<Button>', wasClicked)
  button.mynumber = str(i)
plus = Button(master, text = "+")
plus.grid(column=0, row=10)
plus.mynumber = "+"
plus.bind('<Button>', wasClicked)

eq = Button(master, text = "=")
eq.grid(column=0, row=11)
eq.mynumber = "="
eq.bind('<Button>', changeColor)

b = Entry(master)
b.grid(column=0, row=12)
b.insert(0,"Fill in your own stuff here")
b.bind('<Return>', boxStuff)

master.after(1000, changeColor)
#master.after(2000, changeColor)

mainloop()