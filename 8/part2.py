import itertools

with open('8/input') as f:
    points = [[int(d) for d in line.split(",")] for line in f.readlines()]


def connectionDist(p0, p1):
    x0, y0, z0 = points[p0]
    x1, y1, z1 = points[p1]
    x, y, z = x1-x0, y1-y0, z1-z0
    return x*x + y*y + z*z


connections = list(itertools.combinations(range(len(points)), 2))
connections.sort(key=lambda x: connectionDist(*x))

circuits = []
lastConnection = None
for connection in connections:
    if len(circuits) == 1 and len(circuits[-1]) == len(points):
        break

    i0 = [i for i, c in enumerate(circuits) if connection[0] in c]
    i1 = [i for i, c in enumerate(circuits) if connection[1] in c]

    if i0 and i1:
        if i0[0] != i1[0]:
            circuits[i0[0]].extend(circuits.pop(i1[0]))
    elif i0:
        circuits[i0[0]].append(connection[1])
    elif i1:
        circuits[i1[0]].append(connection[0])
    else:
        circuits.append([connection[0], connection[1]])

    lastConnection = connection
    circuits.sort(key=lambda x: len(x))


print(points[lastConnection[0]][0] * points[lastConnection[1]][0])

# 772452514 - yay
