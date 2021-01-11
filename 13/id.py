a = []

with open('buses.txt') as f:
    for line in f:
        line = line.strip('\n')
        a.append(line)

time = int(a[0])
buses = a[1].split(',')
difference = time
bestBus = 0

for bus in buses:
    if bus != 'x':
        number = int(bus)
        while number <= time:
            number += int(bus)
        if difference > number - time:
            difference = number - time
            bestBus = int(bus)

print(difference*bestBus)
  
import collections
import math
import re

lines = a

def crt(pairs):
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * pow(b, mx-2, mx)
        total %= M
    return total

pairs = []
for i, bus in enumerate(buses):
    if bus != 'x':
        bus = int(bus)
        pairs.append((bus - i, bus))

print(crt(pairs))
