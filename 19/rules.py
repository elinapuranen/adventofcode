messages = []
rules = {}
chars = {}
sum = 0
memory = {}

def checkOptions(message, start, end, options):
    if start == end and not options:
        return True
    if start == end:
        return False
    if not options:
        return False
    ok = False
    for i in range(start+1, end+1):
        print(options)
        if checkRules(message, start, i, options[0]) and checkOptions(message, i, end, options[1:]):
            ok = True
    return ok

def checkRules(message, start, end, rule):
    key = (start, end, rule)
    if key in memory:
        return memory[key]
    ok = False
    if rule in chars:
        ok = (message[start:end] == chars[rule])
    else:
        for options in rules[rule]:
            if checkOptions(message, start, end, options):
                ok = True
    memory[key] = ok
    return ok

with open('messages.txt') as f:
    line = f.readline()
    while line != '\n':
        rule = line.strip('\n').split(': ')
        r = rule[0]
        if r == '8':
            rs = '42 | 42 8'
        elif r == '11':
            rs = '42 31 | 42 11 31'
        else:
            rs = ' '.join(rule[1:])
        if "\"" in rs:
            chars[r] = rs[1:-1]
        else:
            options = rs.split(' | ')
            rules[r] = [x.split(' ') for x in options]
        line = f.readline()
    line = f.readline()
    while line != '\n':
        memory.clear()
        message = line.strip('\n')
        print(message)
        if checkRules(message, 0, len(message), '0'):
            sum += 1
        line = f.readline()

print(sum)