# Task1

import numpy as np
A = np.random.rand(200,10)
B = A - np.mean(A, axis = 0)

print(B)