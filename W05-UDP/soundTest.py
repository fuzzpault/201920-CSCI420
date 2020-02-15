'''
Name: Paul Talaga
Date: 2-13-2020
Desc: Sound tester
      https://realpython.com/playing-and-recording-sound-python/
      https://newt.phys.unsw.edu.au/jw/notes.html

'''

import numpy as np
import simpleaudio as sa
import time

def playSound(frequency = 440, duration = 100):
  #frequency = 440  # Our played note will be 440 Hz
  fs = 44100  # 44100 samples per second
  seconds = duration / 1000.0
  
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
  play_obj.wait_done()

# This is a middle C up an octave, no sharps or flats.
notes = [261.6, 293.67,329.63, 349.23, 392.0, 440.0, 493.8, 523.25]
for n in notes:
  playSound(n,100)

time.sleep(1)
for i in [0,2,4,2,0]:
  playSound(notes[i],100)

