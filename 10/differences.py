a = []

a.append(0)

with open('ratings.txt') as f:
    for line in f:
        line = int(line.strip('\n'))
        a.append(line)

a.sort()
a.append(a[len(a)-1] + 3)
a.reverse()

path = {x:-1 for x in a}
path.update({0:-1})
path[a[0]] = 1
for key in path:
    if key != a[0]:
        sum = 0
        for x in range(1,4):
            if key+x in path:
                sum = sum + path[key+x]
        path[key] = sum

print(path[0])