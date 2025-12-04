with open('4/input') as f:
    maze = [[True if c == '@' else False for c in line] for line in f.readlines()]

maze = [[False for i in range(len(maze[0]) + 2)]] + [[False] + line + [False] for line in maze] + [[False for i in range(len(maze[0]) + 2)]]

accessable = 0
for y in range(1, len(maze) - 1):
    for x in range(1, len(maze[y]) - 1):
        if maze[y][x]:
            count = -1
            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    if maze[i][j]:
                        count += 1
            if count < 4:
                accessable += 1

print(accessable)
