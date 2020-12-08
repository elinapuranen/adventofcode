i = 0

with open('passwords.txt') as f:
    for line in f:
        firstNumber = int(line.split("-")[0])
        secondNumber = int(line.split("-")[1].split(" ")[0])
        letter = line.split("-")[1].split(" ")[1].split(':')[0]
        password = line.split("-")[1].split(" ")[2]
        y = password[firstNumber-1]
        z = password[secondNumber-1]
        if y == letter and z != letter or y != letter and z == letter:
            i += 1

print(i)