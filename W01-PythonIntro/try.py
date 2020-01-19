'''
Name: Paul Talaga
Date: 1-16-2020
Desc: Demo of different python features: try except

'''

s = 0

try:
  while True:
    v = int(input(""))
    s += v

except EOFError:
    print("")
    print("Sum: {}".format(s))

except :
  print("Something else happened")