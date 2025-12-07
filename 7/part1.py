with open('7/input') as f:
    beams = set([f.readline().index('S')])
    splitters = [[i for i, c in enumerate(line.strip()) if c == '^'] for line in f.readlines()]

splitCount = 0
for line in splitters:
    for splitter in line:
        if splitter in beams:
            beams.remove(splitter)
            beams.add(splitter + 1)
            beams.add(splitter - 1)
            splitCount += 1

print(splitCount)
