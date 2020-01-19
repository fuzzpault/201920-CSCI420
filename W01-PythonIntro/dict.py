'''
Name: Paul Talaga
Date: 1-16-2020
Desc: Demo of different python features: dictionary

'''

d1 = {}

d1["bob"] = 5
d1["donuts"] = 10
d1[1053812] = "pizza"

print(d1)
print(list(d1.keys()))
print(list(d1.values()))

for k in d1.keys():
  print("{} has value {}".format(k, d1[k]))