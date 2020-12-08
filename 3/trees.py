a = []

with open('journey.txt') as f:
    for line in f:
        line = line.strip('\n')
        a.append(line)

def sliceArray(array, n):
    a = array[::n]
    return a

def calculateTrees(right, down):
    array = a
    trees = 0
    u = 0
    if (down > 1):
        array = sliceArray(array, down)
    for item in array:
        if len(item) <= u:
            u = u - len(item)
        if item[u] == '#':
            trees += 1
        u += right
    return trees

result = 1

result *= calculateTrees(1,1)
result *= calculateTrees(3,1)
result *= calculateTrees(5,1)
result *= calculateTrees(7,1)
result *= calculateTrees(1,2)

print(result)