'''
Name: Paul Talaga
Date: 2-11-2020
Desc: UDP message sender.

'''

import socket

port_number = 5555
server_ip = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("What do you want to send?")

s.sendto( message.encode('ascii'), (server_ip, port_number))

print("Message Sent!")
(msg, addr) = s.recvfrom(1024)
msg = msg.decode('ascii')
print("Got {} from {}".format(msg, addr))