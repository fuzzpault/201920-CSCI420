'''
Name: Paul Talaga
Date: 1-14-2020
Desc: Demo of different python features: functions and lists

'''

def addOne(thing=1):
  return thing + 1

a = 1
print("{} and {}".format(a, addOne(thing = 10)))

l = []

print("len: {} values: {}".format(len(l), str(l)))

l.append(10)

print("len: {} values: {}".format(len(l), str(l)))

l.append("hi")

print("len: {} values: {}".format(len(l), str(l)))