'''
Name: Paul Talaga
Date: 1-30-2020
Desc: Simple calculator using eval.

'''

from tkinter import *
from random import *

master = Tk()

computation = ""
str_var = StringVar()  # This is a TKinter variable object, which 
                       # will auto-update anywhere it is placed.

def wasClicked(event = None):
  #print(str(dir(event.widget)))
  global computation
  global str_var
  #print("you clicked on {}".format(event.widget.mynumber))
  computation += str(event.widget.mynumber)
  #print("computation is now {}".format(computation))
  str_var.set(computation)

def doComputation(event = None):
  global computation
  global str_var
  print(dir(b))
  result = eval(computation)
  str_var.set(computation + " = " + str(result))
  computation = ""


# Make 1-9
for i in range(9):
  button = Button(master,text=i+1)
  button.grid(column=i % 3, row= int(i / 3))
  button.bind('<Button>', wasClicked)
  button.mynumber = str(i+1)

button = Button(master,text=0)
button.grid(column=1, row= 4) 
button.bind('<Button>', wasClicked)
button.mynumber = str(i)

# Operators
op = ["+","-","*"]
for c in range(len(op)):
  button = Button(master, text = op[c])
  button.grid(column=c, row=5)
  button.mynumber = op[c]
  button.bind('<Button>', wasClicked)

eq = Button(master, text = "=")
eq.grid(column=1, row=6)
eq.mynumber = "="
eq.bind('<Button>', doComputation)

b = Label(master, textvariable = str_var)  # note whenever we change str_var, this will update!
b.grid(column=1, row=7)


mainloop()