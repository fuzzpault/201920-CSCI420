'''
Name: Paul Talaga
Date: 1-14-2020
Desc: Demo of different python features

'''

print('hello world')   # This is a comment

a = 5

print("The number is {}".format(a + 1))

a = "Bob"  # Note a now is storing a string

another_variable = float("45")  # the float function converts whatever is given to a float

print("The number is {} - {}".format(a + " more", another_variable + 1))

# for loop example
for i in range(10): # for(int i = 0; i < 10; i++)
  print("i:{}".format(i))

thing = 56

# while loop example
while thing != 10:
  thing = int(input("Give me a number"))  # How to get input and be sure it is an integer
  if thing < 10:  # Conditionals!
    print("Too low")
  elif thing > 10:
    print("Too high")
  else:
    print("That's correct!")
