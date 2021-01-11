array = []

with open('cubes.txt') as f:
    for line in f:
        line = line.strip('\n')
        array.append(line)

cubes = {}

for i in range (0, len(array)):
    for j in range (0, len(array[i])):
        if array[i][j] == '#':
            cubes[(j, i, 0, 0)] = '#'
        else:
            cubes[(j, i, 0, 0)] = '.'

def findNeighbors(c):
    neighbors = []
    x = -1
    while x < 2:
        y = -1
        while y < 2:
            z = -1
            while z < 2:
                w = -1
                while w < 2:
                    if not (x == 0 and y == 0 and z == 0 and w == 0):
                        neighbors.append((c[0] + x, c[1] + y, c[2] + z, c[3] + w))
                    w += 1
                z += 1
            y += 1
        x += 1
    return neighbors

def checkNeighbors(c, cubes):
    neighbors = findNeighbors(c)
    total = 0
    for n in neighbors:
        if n in cubes:
            if cubes[n] == '#':
                total += 1
    return total

def simulate(cubes):
    newCubes = {}
    for c in cubes:
        i = checkNeighbors(c, cubes)
        if cubes[c] == '#':
            if i == 2 or i == 3:
                newCubes[c] = '#'
            else:
                newCubes[c] = '.'
            neighbors = findNeighbors(c)
            for n in neighbors:
                if n not in cubes:
                    x = checkNeighbors(n, cubes)
                    if x == 3:
                        newCubes[n] = '#'
        elif cubes[c] == '.':
            if i == 3:
                newCubes[c] = '#'
            else:
                newCubes[c] = '.'
    return newCubes 

i = 0
total = 0

while i < 6:
    cubes = simulate(cubes)
    i += 1

for i in cubes:
    if cubes[i] == '#':
        total += 1

print(total)


