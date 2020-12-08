a = []

with open('loop.txt') as f:
    for line in f:
        a.append(line)

for i in range (0, len(a)):
    c = True
    b = [0] * len(a)
    index = 0
    acc = 0
    array = a.copy()

    pair = array[i].strip('\n').split(' ')
    if pair[0] == 'nop' or pair[0] == 'jmp':
        if pair[0] == 'nop':
            array[i] = 'jmp' + ' ' + pair[1]
        elif pair[0] == 'jmp':
            array[i] = 'nop' + ' ' + pair[1]

        while True:
            if index < 654:  
                if b[index] == 0:
                    pair = array[index].strip('\n').split(' ')
                    b[index] = (pair[0], pair[1])
                    if pair[0] == 'acc':
                        acc += int(pair[1])
                        index = index + 1
                    elif pair[0] == 'jmp':
                        index += int(pair[1])
                    elif pair[0] == 'nop':
                        index += 1
                else:
                    break
            else:
                c = False
                break

        if c == False:
            print(acc)
            break

