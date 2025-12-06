import numpy as np
import functools
import operator

with open('6/input') as f:
    inp = np.array([line.strip().split() for line in f.readlines()]).T

print(sum([functools.reduce(operator.mul if col[-1] == '*' else operator.add, [int(i) for i in col[:-1]]) for col in inp]))
