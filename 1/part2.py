with open('1/input') as f:
    strrotations = [r.strip() for r in f.readlines()]
rotations = [(-1 if r[0].lower() == 'l' else 1) * int(r[1:]) for r in strrotations]

dial = 50
passwd = 0
for rotation in rotations:
    for i in range(abs(rotation)):
        if rotation > 0:
            dial += 1
        else:
            dial -= 1

        dial = dial % 100
        if dial < 0:
            dial += 100

        if dial == 0:
            passwd += 1

print(passwd)
