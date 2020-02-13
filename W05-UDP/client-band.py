'''
Name: Paul Talaga
Date: 2-11-2020
Desc: UDP message sender.

'''

import socket
import pickle

port_number = 5555
server_ip = '127.0.0.1'  # put destination address here

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
  freq = input("What frequency?")
  dur = input("What duration in ms?")

  message = pickle.dumps( (freq,dur) )

  s.sendto( message, (server_ip, port_number))

  print("Message Sent!")
