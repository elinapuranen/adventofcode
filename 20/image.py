tiles = {}

with open('tiles.txt') as f:
    key = 0
    value = []
    for line in f:
        if line == '\n':
            tiles[key] = value
            value = []
        elif line.strip('\n').split(' ')[0] == 'Tile':
            line = line.strip('\n').split(' ')
            key = line[1].strip(':')
        else:
            line = line.strip('\n')
            value.append(line)

def getEdges(tile):
    up = tile[0]
    down = tile[len(tile)-1]
    left = ''
    right = ''
    for u in tile:
        left += u[0]
        right += u[len(u)-1]
    return up, down, left, right

memory = {}
matches = {}

for tile in tiles:
    id = tile
    matches[id] = 0
    edges = getEdges(tiles[tile])
    for edge in edges:
        pair = None
        if edge in memory:
            pair = memory[edge]
        else:
            reverse = edge[::-1]
            if reverse in memory:
                pair = memory[reverse]
                edge = reverse
        if pair is not None:
            matches[pair] = matches[pair] + 1
            matches[id] = matches[id] + 1
            memory[edge] = [pair, id]
        else:
            memory[edge] = id

sum = 1
corners = []
for id in matches:
    if matches[id] == 2:
        corners.append(id)
        sum *= int(id)
    
print(sum)

# DEFINITELY not my code but could not get the part 2 working using the means I know.

# import math

# def tohash(array, reverse=False):
#     if reverse:
#         array = list(array)
#         array.reverse()  
#     return int(''.join(map(str, array)), 2)

# class Tile:
#     def __init__(self, data):
#         self.id = int(data[0][5:9])
#         self.grid = [[int(c == '#') for c in line] for line in data[1:]]
#         self.hashsides()

#     def hashsides(self):
#         self.sides = {}
#         self.sides['top'] = tohash(self.grid[0])
#         self.sides['top_r'] = tohash(self.grid[0], reverse=True)
#         self.sides['right'] = tohash(map(lambda l: l[-1], self.grid))
#         self.sides['right_r'] = tohash(map(lambda l: l[-1], self.grid), reverse=True)
#         self.sides['bottom'] = tohash(self.grid[-1])
#         self.sides['bottom_r'] = tohash(self.grid[-1], reverse=True)
#         self.sides['left'] = tohash(map(lambda l: l[0], self.grid))
#         self.sides['left_r'] = tohash(map(lambda l: l[0], self.grid), reverse=True)

#     def countMatchingSides(self, alltiles):
#         counts = {'top': 0, 'right': 0, 'bottom': 0, 'left': 0}
#         for tile in alltiles:
#             if tile != self:
#                 for side in self.sides:
#                     if self.sides[side] in tile.sides.values():
#                         counts[side.split('_')[0]] += 1
#         return list(counts.values()).count(0)

#     def collectPossibleNeighbours(self, alltiles):
#         self.neighbours = {'top': set(), 'right': set(), 'bottom': set(), 'left': set()}
#         for tile in alltiles:
#             if tile != self:
#                 for side in self.sides:
#                     if self.sides[side] in tile.sides.values():
#                         self.neighbours[side.split('_')[0]].add(tile.id)
#         return self.neighbours

#     def nb(self, side):
#         for nb in self.neighbours[side]:
#             return nb

#     def rotate(self):
#         self.grid = [[l[x] for l in self.grid][::-1] for x in range(len(self.grid[0]))]
#         self.hashsides()
#         old_top = self.neighbours['top']
#         self.neighbours['top'] = self.neighbours['left']
#         self.neighbours['left'] = self.neighbours['bottom']
#         self.neighbours['bottom'] = self.neighbours['right']
#         self.neighbours['right'] = old_top

#     def flip(self):
#         self.grid = self.grid[::-1]
#         self.hashsides()
#         old_top = self.neighbours['top']
#         self.neighbours['top'] = self.neighbours['bottom']
#         self.neighbours['bottom'] = old_top

#     def hflip(self):
#         self.grid = [row[::-1] for row in self.grid]
#         self.hashsides()
#         old_left = self.neighbours['left']
#         self.neighbours['left'] = self.neighbours['right']
#         self.neighbours['right'] = old_left

#     def row(self, r, dropborder=False):
#         if dropborder:
#             return ''.join('#' if c else '.' for c in self.grid[r][1:-2])
#         else:
#             return ''.join('#' if c else '.' for c in self.grid[r])


# def printrow(tiles):
#     for i in range(10):
#         print(' '.join(t.row(i) for t in tiles))


# def rowtostring(tiles):
#     return '\n'.join(''.join(t.row(i, True) for t in tiles) for i in range(1, 9))


# def combineIntoRow(tiles):
#     row = []
#     size = len(tiles[0].grid)
#     for l in range(1, size-1):
#         row.append([])
#         for t in tiles:
#             row[l-1].extend(t.grid[l][1:size-1])
#     return row


# with open('tiles.txt') as f:
#     tiles = [Tile(t.splitlines()) for t in f.read().strip().split('\n\n')]
#     alltiles = {tile.id: tile for tile in tiles}
#     corners = [tile.id for tile in tiles if tile.countMatchingSides(tiles) == 2]
#     print(f'Part 1: {math.prod(corners)}')

#     neighbours = [tile.collectPossibleNeighbours(tiles) for tile in tiles]

#     imageArray = []

#     rows = [[alltiles[corners[0]]]]
#     while not (rows[0][0].neighbours['right'] and rows[0][0].neighbours['bottom']):
#         rows[0][0].rotate()

#     while rows[0][-1].neighbours['right']:
#         for next in rows[0][-1].neighbours['right']:
#             break
#         next = alltiles[next]
#         while next.nb('left') != rows[0][-1].id:
#             next.rotate()
#         if next.sides['left'] != rows[0][-1].sides['right']:
#             next.flip()
#         rows[0].append(next)
#     imageArray.extend(combineIntoRow(rows[0]))

#     for y in range(1, len(rows[0])):
#         rows.append([alltiles[rows[y - 1][0].nb('bottom')]])
#         while not rows[y][0].nb('top') == rows[y-1][0].id:
#             rows[y][0].rotate()
#         if rows[y][0].sides['top'] != rows[y - 1][0].sides['bottom']:
#             rows[y][0].hflip()

#         while rows[y][-1].neighbours['right']:
#             for next in rows[y][-1].neighbours['right']:
#                 break
#             next = alltiles[next]
#             while next.nb('left') != rows[y][-1].id:
#                 next.rotate()
#             if next.sides['left'] != rows[y][-1].sides['right']:
#                 next.flip()
#             rows[y].append(next)

#         imageArray.extend(combineIntoRow(rows[y]))

#     a = imageArray
#     for i in range(8):  
#         monster = False
#         for y in range(len(a)-2):
#             for x in range(len(a[0]) - 19):
#                 first = a[y][x + 18]
#                 second = a[y + 1][x] and a[y + 1][x + 5] and a[y + 1][x + 6] and a[y + 1][x +
#                                                                                           11] and a[y + 1][x + 12] and a[y + 1][x + 17] and a[y + 1][x + 18] and a[y + 1][x + 19]
#                 third = a[y + 2][x + 1] and a[y + 2][x + 4] and a[y + 2][x + 7] and a[y + 2][x + 10] and a[y + 2][x + 13] and a[y + 2][x + 16]
#                 if first and second and third:
#                     monster = True
#                     a[y][x + 18] = 2
#                     a[y + 1][x] = a[y + 1][x + 5] = a[y + 1][x + 6] = a[y + 1][x + 11] = a[y + 1][x + 12] = a[y + 1][x + 17] = a[y + 1][x + 18] = a[y + 1][x + 19] = 2
#                     a[y + 2][x + 1] = a[y + 2][x + 4] = a[y + 2][x + 7] = a[y + 2][x + 10] = a[y + 2][x + 13] = a[y + 2][x + 16] = 2
#         if monster:
#             print(f'Iteration {i}: found a monster!')
#             break
#         else:
#             a = [[l[x] for l in a][::-1] for x in range(len(a[0]))]
#             if i == 4:
#                 a.reverse()

#     print(f'Part 2: {sum(1 for line in a for cell in line if cell == 1)}')