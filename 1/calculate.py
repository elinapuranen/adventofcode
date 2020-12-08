array = []

with open('numbers.txt') as f:
    for line in f:
        array.append(int(line))

i = 0

for x in array:
    if i != 0:
        break
    for y in array:
        if i != 0:
            break
        for z in array:
            if x + y + z == 2020:
                i = x*y*z
                print (i)
                break