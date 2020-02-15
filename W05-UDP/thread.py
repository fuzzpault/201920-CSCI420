'''
Name: Paul Talaga
Date: 2-13-2020
Desc: Threading demo.

'''

import threading
import time

trigger = False

def printStuff():
  stuff = "nothing"
  global trigger
  while True:
    if not trigger:
      print(stuff)
    time.sleep(1)


threading.Thread(target=printStuff).start()
while True:
  i = input("Give me text")
  print(i)
  if i == "huh":
    trigger = True
  else:
    trigger = False
