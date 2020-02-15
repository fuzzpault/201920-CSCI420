'''
Name: Paul Talaga
Date: 2-11-2020
Desc: Piano player
      AAAFCAFCA EEEFCA#FCAFCA

'''

import socket
import pickle
from tkinter import *

master = Tk()

port_number = 5555
server_ip = '127.0.0.1'  # put destination address here

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def keyToFreq(key):
  # https://en.wikipedia.org/wiki/Piano_key_frequencies
  return 2.0 ** ((key - 49) / 12.0) * 440

def playSound(freq, dur):
  message = pickle.dumps( (freq,dur) )
  s.sendto( message, (server_ip, port_number))
  print("{} {} sent".format(freq,dur))

def wasClicked(event):
  playSound(event.widget.secretValue, 100)

keys = [1,3,5,6,8,10,12]  # need 13 to finish

for n in keys:
  button = Button(master,text=str(n))
  button.grid(column=n, row= 0) 
  button.bind('<Button>', wasClicked)
  button.secretValue = keyToFreq(n+48) 

for n in keys:
  button = Button(master,text=str(n))
  button.grid(column=n + 12, row= 0) 
  button.bind('<Button>', wasClicked)
  button.secretValue = keyToFreq(n+48 + 12)

mainloop()
