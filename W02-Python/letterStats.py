'''
Name: Paul Talaga
Date: 1-23-2020
Desc: Multiple ways of getting the most and least commonly used letter in a string.

'''

text = input("Type something in: ")

counts = {}

for c in text:
  #print(c):
  if c in counts.keys():
    counts[c] += 1
  else:
    counts[c] = 1

# Option 1
'''min_count = counts[ list(counts.keys())[0] ]
min_key = list(counts.keys())[0]


print("Min: ")

for k in counts.keys():
  if counts[k] < min_count:
    min_count = counts[k]
    min_key = k

for k in counts.keys():
  if counts[k] == min_count:
    print("{}:{}".format(k,counts[k]))

max_count = counts[ list(counts.keys())[0] ]
max_key = list(counts.keys())[0]

print("Max: ")

for k in counts.keys():
  if counts[k] > max_count:
    max_count = counts[k]
    max_key = k

for k in counts.keys():
  if counts[k] == max_count:
    print("{}:{}".format(k,counts[k]))

print(counts)
'''

# Option #2
tuples = zip(counts.keys(), counts.values())
tuples = sorted(tuples, key = lambda a: -a[1]  )
maxes = filter(lambda a: a[1] == tuples[0][1], tuples)
mins = filter(lambda a: a[1] == tuples[-1][1], tuples)
print(list(maxes))
print(list(mins))

print(list(tuples))
