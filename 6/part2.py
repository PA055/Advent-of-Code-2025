import numpy as np

with open('6/input') as f:
    lines = f.readlines()
    numbers = np.array([list(line[:-1]) for line in lines[:-1]]).T
    operations = lines[-1].split()

operandArray = []
operands = []
for col in numbers:
    if all(i == ' ' for i in col):
        operandArray.append(operands)
        operands = []
        continue
    operands.append(int(''.join(col)))
operandArray.append(operands)

total = 0
for operands, operator in zip(operandArray, operations):
    result = 1 if operator == '*' else 0
    for v in operands:
        if operator == '*':
            result *= v
        else:
            result += v
    total += result
    # print(f' {operator} '.join(str(o) for o in operands), '=', result)

print(total)

# 10442199702583 - too low
# 10442199710797 - yay
