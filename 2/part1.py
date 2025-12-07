with open('2/input') as f:
    ranges = [(int(min), int(max)) for min, max in map(lambda x: x.split('-'), f.read().split(','))]

answer = 0
for sml, big in ranges:
    for j in range(sml, big + 1):
        s = str(j)
        if s[:len(s) // 2] * 2 == s:
            answer += j

print(answer)
