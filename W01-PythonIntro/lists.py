'''
Name: Paul Talaga
Date: 1-14-2020
Desc: Demo of different python features: functions and lists

'''

def addOne(thing=1):
  return thing + 5

a = 1
print("{} and {}".format(a, addOne(thing = 10)))

l = []

print("len: {} values: {}".format(len(l), str(l)))

l.append(10)
l.append(13)
l.append(65)
l.append(75)
l.append(85)

print(l)

print(l[:3])
print(l[-2:])

l2 = map(addOne, l)
l2 = map(lambda a: a + 2, l)

print(list(l2))

l3 = filter(lambda a: a < 20, l)
print(list(l3))

l4 = map(lambda a: (a,1), l)

print(list(l4))