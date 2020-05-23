import numpy as np


a = np.zeros((4, 6), dtype=int)

a[1][1] = 1
a[1][2] = 1
a[1][3] = 1


a[2][1] = 1
a[2][2] = 1
a[2][3] = 1

result = a.sum(axis=1)

print(np.count_nonzero(result == 3))
# print(a.sum(axis=1).count_nonzero(3))
