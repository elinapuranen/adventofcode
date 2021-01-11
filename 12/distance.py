pos = [0, 0]
waypoint = [1, 10]

with open('directions.txt') as f:
    directions = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    direction = 90
    for line in f:
        line = line.strip('\n')
        action = line[0]
        value = int(line[1:])
        
        if action == 'F':
            pos[0] += value * waypoint[0]
            pos[1] += value * waypoint[1]

        if action == 'N':
            waypoint[0] += value
        elif action == 'S':
            waypoint[0] -= value
        elif action == 'E':
            waypoint[1] += value
        elif action == 'W':
            waypoint[1] -= value
        elif action == 'R':
            northSouth = waypoint[0]
            eastWest = waypoint[1]
            while value > 0:
                waypoint[1] = northSouth
                waypoint[0] = -eastWest
                northSouth = waypoint[0]
                eastWest = waypoint[1]
                value -= 90
        elif action == 'L':
            northSouth = waypoint[0]
            eastWest = waypoint[1]
            while value > 0:
                waypoint[1] = -northSouth
                waypoint[0] = eastWest
                northSouth = waypoint[0]
                eastWest = waypoint[1]
                value -= 90

print(abs(pos[0]) + abs(pos[1]))
        