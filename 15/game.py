turns = {5: 1, 1: 2, 9: 3, 18: 4, 13: 5, 8: 6, 0: 7}
i = 9

lastNum = 0
while i <= 30000000:
    if lastNum in turns.keys():
        previous = turns[lastNum]
        turns[lastNum] = i - 1
        lastNum = turns[lastNum] - previous
    else:
        turns[lastNum] = i - 1
        lastNum = 0
    i += 1

print(lastNum)
