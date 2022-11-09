import time
import math
import numpy


size = 10000000
A = numpy.arange(size)
B = numpy.arange(size)
t0 = time.time()
for i in range(size):
    B[i] = math.tan(A[i])

t1 = time.time()
print(t1 - t0)
