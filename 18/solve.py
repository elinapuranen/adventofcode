array = []
sum = 0

with open('homework.txt') as f:
    for line in f:
        line = line.strip('\n')
        array.append(line)

def calculate(i, array, multiply):
    sum = 0
    operator = '+'
    while i < len(array):
        if array[i] == ' ':
            i += 1
        elif array[i].isdigit():
            if operator == '+':
                sum += int(array[i])
            else:
                sum *= int(array[i])
            i += 1
        elif array[i] == '+':
            operator = '+'
            i += 1
        elif array[i] == '*':
            operator = '*'
            i += 1
            m, i = calculate(i, array, True)
            sum *= m
        elif array[i] == '(':
            i += 1
            m, i = calculate(i, array, False)
            if operator == '+':
                sum += m
            else:
                sum *= m
        else:
            if multiply == True:
                break
            i += 1
            break
    return sum, i

for i in array:
    sum += (calculate(0, i, False))[0]

print(sum)


        