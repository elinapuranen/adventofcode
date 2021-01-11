a = []
b = []
weakness = 0

with open('numbers.txt') as f:
    for line in f:
        line = int(line.strip('\n'))
        a.append(line)

for i in range (0,25):
    b.append(a[i])

for x in range (25,len(a)):
    found = False
    for y in b:
        for z in b:
            if y + z == a[x] and y != z:
                found = True
                b.pop(0)
                b.append(a[x])
                break
        if found == True:
            break
    if found == False:
        weakness = a[x]
        break
    else:
        found == False

c = []

for i in a:
    c.append(i)
    if sum(c) > weakness:
        while sum(c) > weakness:
            c.pop(0)
    if sum(c) == weakness:
        c.sort()
        count = c[0] + c[len(c) - 1]
        print (count)
        break