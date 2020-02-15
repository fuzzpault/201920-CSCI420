'''
Name: Paul Talaga
Date: 2-13-2020
Desc: UDP message sound server.

'''

import socket
import numpy as np
import simpleaudio as sa
import time
import pickle

port_number = 5555
#server_ip = '127.0.0.1'  # This will only listen for requests from localhost
server_ip = '0.0.0.0'     # This will listen for requests from any host

active_clients = {}


def playSound(frequency = 440, duration = 100):
  #frequency = 440  # Our played note will be 440 Hz
  fs = 44100  # 44100 samples per second
  seconds = float(duration) / 1000.0
  frequency = float(frequency)
  
  # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
  t = np.linspace(0, seconds, seconds * fs, False)

  # Generate a 440 Hz sine wave
  note = np.sin(frequency * t * 2 * np.pi)

  # Ensure that highest value is in 16-bit range
  audio = note * (2**15 - 1) / np.max(np.abs(note))
  # Convert to 16-bit data
  audio = audio.astype(np.int16)

  # Start playback
  play_obj = sa.play_buffer(audio, 1, 2, fs)

  # Wait for playback to finish before exiting
  #play_obj.wait_done()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind( (server_ip, port_number) )

while True:
  (msg, addr) = s.recvfrom(1024)
  active_clients[addr[0]] = addr
  try:
    (frequency, duration) = pickle.loads(msg)
    frequency = float(frequency)
    duration = float(duration)
  except:   # was there an error unpickling or converting to a float?
    print("Error from {}".format(addr))
    next
  print("frequency (hz): {} duration (ms): {}".format(frequency,duration))
  #print("Got {} from {}".format(msg, addr))
  print("Num user: {} {}".format(len(active_clients), str(active_clients)))
  playSound(frequency, duration)
  