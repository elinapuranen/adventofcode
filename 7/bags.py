class Bags:
    bags = 0
    array = []

class NumberOfBags:
    bags = 0

def findColors(shade, color):
    with open('colors.txt') as f:
        for line in f: 
            line = line.strip('\n').split(' ')
            if color in line:
                indices = [i for i, x in enumerate(line) if x == color]
                for index in indices:
                    if index != 1:
                        if line[index-1] == shade:
                            if (line[0], line[1]) not in Bags.array:
                                Bags.bags += 1
                                Bags.array.append((line[0], line[1]))
                                findColors(line[0], line[1])

def findNumberOfBags(shade, color, number):
    with open('colors.txt') as f:
        for line in f:
            line = line.strip('\n').split(' ')
            if line[0] == shade and line [1] == color:
                line = line[4:]
                for i in range (0, len(line)):
                    if (int(i) == 0 or int(i) % 4 == 0) and line[i] != 'no': 
                            NumberOfBags.bags += number*int(line[i])
                            findNumberOfBags(line[i+1], line[i+2], number*int(line[i]))

findNumberOfBags('shiny', 'gold', 1)

print(NumberOfBags.bags)