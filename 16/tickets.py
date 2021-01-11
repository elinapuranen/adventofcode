array = [0] * 1000
yourTicket = []
nearbyTickets = []
dictionary = {}

with open('tickets.txt') as f:
    line = f.readline()
    while line != '\n':
        a = line.strip('\n').split(': ')
        field = a[0]
        numbers = a[1].split(' or ')
        n1 = numbers[0].split('-')
        n2 = numbers[1].split('-')
        dictionary[field] = ((int(n1[0]), int(n1[1])), (int(n2[0]), int(n2[1])))
        for i in range (int(n1[0]), int(n1[1])+1):
            array[i] = 1
        for i in range (int(n2[0]), int(n2[1])+1):
            array[i] = 1
        line = f.readline()
    line = f.readline()
    line = line.strip('\n')
    if line == 'your ticket:':
        line = f.readline()
        ticket = line.strip('\n').split(',')
        yourTicket = ticket
        line = f.readline()
    line = f.readline()
    line = line.strip('\n')
    if line == 'nearby tickets:':
        line = f.readline()
        while line != '\n':
            ticket = line.strip('\n')
            nearbyTickets.append(ticket)
            line = f.readline()

count = 0
validTickets = nearbyTickets.copy()

for i in nearbyTickets:
    arr = i.split(',')
    for a in arr:
        if array[int(a)] == 0:
            count += int(a)
            if i in validTickets:
                validTickets.remove(i)

fields = [[]] * len(yourTicket)

for i in validTickets:
    arr = i.split(',')
    for a in range (0, len(arr)):
        ticketFields = []
        for d in dictionary.items():
            if d[1][0][0] <= int(arr[a]) <= d[1][0][1] or d[1][1][0] <= int(arr[a]) <= d[1][1][1]:
                ticketFields.append(d[0])
        if len(fields[a]) != 0:
            for field in fields[a]:
                if field not in ticketFields:
                    fields[a].remove(field)
        else:
            fields[a] = ticketFields

filtering = []

while True:
    for i in range (0, len(fields)):
        if len(fields[i]) == 1:
            filtering.append(fields[i][0])
        else: 
            for f in filtering:
                if f in fields[i]:
                    fields[i].remove(f)
    done = True
    for field in fields:
        if len(field) > 1:
            done = False
            break
    if done:
        break

count = 1

for i in range(0, len(fields)):
    if fields[i][0].startswith('departure'):
        count *= int(yourTicket[i])

print(count)

