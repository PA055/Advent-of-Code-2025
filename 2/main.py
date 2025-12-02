with open('2/input') as f:
    ranges = [(int(min), int(max)) for min, max in map(lambda x: x.split('-'), f.read().split(','))]

answer = 0
for sml, big in ranges:
    for j in range(sml, big + 1):
        s = str(j)
        for i in range(1, len(s)):
            if len(s) % i != 0:
                continue
            if s[:i] * (len(s) // i) == s:
                answer += j
                break

print(answer)
