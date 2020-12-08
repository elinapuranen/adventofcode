sum = 0
a = []

with open('answers.txt') as f:
    for line in f:
        line = line.strip('\n')
        if len(line) == 0:
            s = set(a[0])
            for i in range (1, len(a)):
                s = s & set(a[i])
            sum += len(s)
            a.clear()
        else:
            a.append(line)

print(sum)