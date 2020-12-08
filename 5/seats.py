a = []

def halves(c, min, max):
    middle = (min + max) / 2
    if c == 'F' or c == 'L':
        return (min, middle - 0.5)
    if c == 'B' or c == 'R':
        return (middle + 0.5, max)

with open('passports.txt') as f:
    for line in f:
        line = line.strip('\n')
        row = (0, 127)
        column = (0, 7)
        for char in line:
            if char == 'F' or char == 'B':
                row = halves(char, row[0], row[1])
            if char == 'L' or char == 'R':
                column = halves(char, column[0], column[1])
        a.append(row[0] * 8 + column[0])

for item in range (0, 880):
    if item not in a:
        if item - 1 in a and item + 1 in a:
            print(item)