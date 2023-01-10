import time
import math

t0 = time.time()

size = 100000000
A = list(range(size))
B = list(range(size))
for i in range(size):
    B[i] = math.tan(A[i])

t1 = time.time()
print(t1 - t0)
