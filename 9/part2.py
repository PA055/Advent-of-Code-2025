import itertools

with open('9/input2') as f:
    points = [[int(x), int(y)] for x, y in (line.split(',') for line in f.readlines())]

boxes = [(a, b, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)) for a, b in itertools.combinations(points, 2)]
boxes.sort(key=lambda r: r[2], reverse=True)

points.append(points[0])
for a, b, area in boxes:
    # print(f"box: {a}, {b}, {area}", end="; ")
    # this part basically checks if the box is inside the whole structure
    # upon further inspection i dont even think it works so idk how i got it right
    # but my thought process is if its inside the structure the box would either be
    # above, below, to the left, or to the right of every line
    valid = True
    for start, end in itertools.pairwise(points):
        left = max(a[0], b[0]) <= min(start[0], end[0])
        right = min(a[0], b[0]) >= max(start[0], end[0])
        above = max(a[1], b[1]) <= min(start[1], end[1])
        below = min(a[1], b[1]) >= max(start[1], end[1])
        if not (left or right or above or below):
            # print(f"bad line: {start}, {end}")
            valid = False
            break

    if valid:
        # print('good')
        print(area)
        break

# 7110910657 - too high
# 7102797211 - too high
# oh thats not what this is asking oops :3
# 1560475800 - somehow yay
