'''
Name: Paul Talaga
Date: 2-13-2020
Desc: Threading demo.

'''

import threading
import time

def doStuff():
  for i in range(1,10):
    str = "Kristiāns is "
    for x in range(i):
      str += " awesome"
    str += "!"
    print(str)
    time.sleep(0.5)

threading.Thread(target=doStuff).start()
print("I'm here")


