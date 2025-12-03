with open('3/input') as f:
    banks = [l.strip() for l in f.readlines()]

total = 0
for bnk in banks:
    left = max(*((i, int(b)) for i, b in enumerate(bnk[:-1])), key=lambda x: x[1])
    right = max(*(b for b in bnk[left[0] + 1:]), key=lambda x: int(x))

    joltage = int(str(left[1]) + str(right))
    total += joltage

print(total)

# 16115 - i was being dumb lmao
# 17166 - yay :3
