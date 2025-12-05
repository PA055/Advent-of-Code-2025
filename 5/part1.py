ranges = []
items = []
section1 = True
with open('5/input') as f:
    for line in f.readlines():
        if line.strip() == '':
            section1 = False
            continue

        if section1:
            low, high = line.strip().split('-')
            ranges.append((int(low), int(high)))
        else:
            items.append(int(line.strip()))

print(sum([1 if any(item > low and item < high for low, high in ranges) else 0 for item in items]))
