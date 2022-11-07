import time
import math
import numpy

t0 = time.time()

size = 10000000
A = numpy.arange(size)
B = numpy.arange(size)
for i in range(size):
    B[i] = math.tan(A[i])

t1 = time.time()
print(t1 - t0)
