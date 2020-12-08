a = []
passports = 0
hairColor = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
eyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

with open('documents.txt') as f:
    for line in f:
        line = line.strip('\n').split(' ')
        if line[0] == '':
            merged_array = []
            for item in a:
                merged_array += item
            pairs = []
            for item in merged_array:
                item = item.split(':')
                pairs.append((item[0], item[1]))
            i = 0
            for pair in pairs:
                key = pair[0]
                value = pair[1]
                if key == 'byr':
                    if int(value) <= 2002 and int(value) >= 1920:
                        i += 1
                elif key == 'iyr':
                    if int(value) <= 2020 and int(value) >= 2010:
                        i += 1
                elif key == 'eyr':
                    if int(value) <= 2030 and int(value) >= 2020:
                        i += 1
                elif key == 'hgt':
                    if value[-2:] == 'cm' and int(value[:-2]) >= 150 and int(value [:-2]) <= 193:
                        i += 1
                    elif value[-2:] == 'in' and int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                        i += 1
                elif key == 'hcl':
                    if value[0] == '#' and len(value) == 7 and all(x not in value[:1] for x in hairColor):
                        i += 1
                elif key == 'ecl':
                    if value in eyeColor:
                        i += 1
                elif key == 'pid':
                    if len(value) == 9:
                        i += 1
            if i == 7:
                passports += 1
            a.clear()
        else:      
            a.append(line)

print(passports)