import itertools

with open('9/input') as f:
    tiles = [[int(x) for x in line.split(',')] for line in f.readlines()]

rectangles = [(abs(tiles[j][0] - tiles[i][0]) + 1, abs(tiles[j][1] - tiles[i][1]) + 1, tiles[i], tiles[j]) for i, j in itertools.combinations(range(len(tiles)), 2)]
rectangles.sort(key=lambda x: x[0] * x[1], reverse=True)
print(rectangles[0][0] * rectangles[0][1])

# 4774739298 - too low
# 4774877510 - yippee
