with open('7/input') as f:
    line = f.readline()
    width = len(line)
    beams = {line.index('S'): 1}
    splitters = [[i for i, c in enumerate(line.strip()) if c == '^'] for line in f.readlines()]

for line in splitters:
    for splitter in line:
        if splitter in beams.keys():
            count = beams.pop(splitter)
            beams[splitter + 1] = beams.get(splitter + 1, 0) + count
            beams[splitter - 1] = beams.get(splitter - 1, 0) + count

print(sum(beams.values()))
