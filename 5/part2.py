ranges = []
with open('5/input2') as f:
    for line in f.readlines():
        if line.strip() == '':
            break
        low, high = line.strip().split('-')
        ranges.append((int(low), int(high)))

count = 0
# this one line makes it O(n log n), otherwise it would be O(n) 💔
ranges.sort()
llow, lhigh = 0, 0
for low, high in ranges:
    if low <= lhigh:
        count += max(0, high - lhigh)
        if high > lhigh:
            llow, lhigh = low, high
    else:
        count += high - low + 1
        llow, lhigh = low, high

print(count)

#         1 1    1
# 2 4 67890 2    7
# |   |
#   |     |
#      | |
#           |    |

# 396598484549799 - too high
# 385341111254897 - too high
# 380721900078540 - too high
# 352716206375547 - yay
