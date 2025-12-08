import itertools

with open('8/input') as f:
    points = [[int(d) for d in line.split(",")] for line in f.readlines()]
totalConnections = 1000


def connectionDist(p0, p1):
    x0, y0, z0 = points[p0]
    x1, y1, z1 = points[p1]
    x, y, z = x1-x0, y1-y0, z1-z0
    return x*x + y*y + z*z


connections = list(itertools.combinations(range(len(points)), 2))
connections.sort(key=lambda x: connectionDist(*x))

circuits = []
completedConnections = 0
for connection in connections:
    if completedConnections >= totalConnections:
        break

    # print(f"{completedConnections + 1}/{totalConnections}", end=': ')
    # print(f"{connection}; {connectionDist(*connection)}", end=': ')
    i0 = [i for i, c in enumerate(circuits) if connection[0] in c]
    i1 = [i for i, c in enumerate(circuits) if connection[1] in c]
    # print(i0, i1, end=', ')

    if i0 and i1:
        if i0[0] != i1[0]:
            # print("both existing circuits", end='')
            circuits[i0[0]].extend(circuits.pop(i1[0]))
        # else:
            # print("invalid connection", end='')
        completedConnections += 1
    elif i0:
        # print(f"circuit {i0[0]}", end='')
        circuits[i0[0]].append(connection[1])
        completedConnections += 1
    elif i1:
        # print(f"circuit {i1[0]}", end='')
        circuits[i1[0]].append(connection[0])
        completedConnections += 1
    else:
        # print("new circuit", end='')
        circuits.append([connection[0], connection[1]])
        completedConnections += 1

    # print()

circuits.sort(key=lambda x: len(x))
# print(circuits)
print(len(circuits[-1]) * len(circuits[-2]) * len(circuits[-3]))

# 1716 - too low
# 163548 - yay
