a = []

with open('seats.txt') as f:
    for line in f:
        line = line.strip('\n')
        a.append(line)

def changeSeats(seats):
    array = []
    for row in range (0, len(seats)):
        newRow = ''
        for seat in range (0, len(seats[row])):
            if seats[row][seat] == '.':
                newRow += '.'
            else:
                adjacents = 0
                for i in (-1, 0, 1):
                    for u in (-1, 0, 1):
                        if not (i == 0 and u == 0):
                            x = 1
                            while (row-i*x >= 0 and row-i*x < len(seats) and seat-u*x >= 0 and seat-u*x < len(seats[row])):
                                if seats[row-i*x][seat-u*x] == '#':
                                    adjacents += 1
                                if seats[row-i*x][seat-u*x] != '.':
                                    break
                                x += 1
                if adjacents >= 5:
                    newRow += 'L'
                elif adjacents == 0:
                    newRow += '#'
                else:
                    newRow += seats[row][seat]
        array.append(newRow)
    return array

while True:
    previous = a
    a = changeSeats(a)
    if previous == a:
        break

print(''.join(a).count('#'))


                
                
