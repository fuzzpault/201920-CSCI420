'''
Name: Paul Talaga
Date: 2-11-2020
Desc: Can we cause an error by updating a global error using multiple threads?
      https://wiki.python.org/moin/GlobalInterpreterLock

'''

import threading
import time

counter = 0

def doStuff():
  global counter
  for i in range(100000):
    counter += 1
    #time.sleep(0.5)

def doMoreStuff():
  global counter
  for i in range(100000):
    counter += 1
    #time.sleep(0.5)

a = threading.Thread(target=doStuff)
a.start()
b = threading.Thread(target=doMoreStuff)
b.start()

a.join()
b.join()

print("counter: {}".format(counter))


