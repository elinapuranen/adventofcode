def applyMask(value, mask):
    res = ''
    for i in range(0, len(mask)):
        if mask[i] == '1':
            res += '1'
        elif mask[i] == '0':
            res += '0'
        else:
            res += value[i]
    return int(res, 2)

memory = {}
mask = ''
with open('masks.txt') as f:
    for line in f:
        cmd, value = line.strip('\n').split(' = ')
        if cmd == 'mask':
            mask = value
        else:
            address = int(cmd[4:-1])
            value = applyMask('{0:036b}'.format(int(value)), mask)
            memory[address] = value

sum = 0
for value in memory.values():
    sum += value

print(sum)

def addressMask(addr, mask):
    res = ''
    for i in range(0, len(mask)):
        if mask[i] == '1':
            res += '1'
        elif mask[i] == '0':
            res += addr[i]
        else:
            res += 'X'
    return res

def writeMemory(memory, address, n):
    if address.count('X') == 0:
        memory[address] = n
        return
    writeMemory(memory, address.replace('X', '0', 1), n)
    writeMemory(memory, address.replace('X', '1', 1), n)

memory = {}
mask = ''
with open('masks.txt') as f:
    for line in f:
        cmd, value = line.strip('\n').split(' = ')
        if cmd == 'mask':
            mask = value
        else:
            address = int(cmd[4:-1])
            address = addressMask('{0:036b}'.format(int(address)), mask)
            writeMemory(memory, address, int(value))

sum = 0
for value in memory.values():
    sum += value

print(sum)