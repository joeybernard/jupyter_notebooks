import time
import math
from numba import jit

@jit
def arr(size):
	A = list(range(size))
	B = list(range(size))
	for i in range(size):
    		B[i] = math.tan(A[i])

t0 = time.time()
arr(100000000)
t1 = time.time()
print(t1 - t0)
