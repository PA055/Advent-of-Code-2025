with open('3/input') as f:
    banks = [l.strip() for l in f.readlines()]

total = 0
for bnk in banks:
    joltage = ''
    left = -1
    for j in range(12, 0, -1):
        b = 0
        for i, n in enumerate(bnk):
            if i <= left or i > len(bnk) - j:
                continue
            if int(n) > b:
                b = int(n)
                left = i
        joltage += str(b)

    total += int(joltage)

print(total)

# 168965004509739 - too low
# 169077317650774 - yay :3
