import random
import time
import matplotlib.pyplot as plt
import math
import numpy as np
#############################################


def DAC(x, y):
    if x.size == 1 or y.size == 1:
        return x * y

    n = x.shape[0]

    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode='constant')
        y = np.pad(y, (0, 1), mode='constant')

    m = int(np.ceil(n / 2))

    A11 = x[:m, :m]
    A12 = x[:m, m:]
    A21 = x[m:, :m]
    A22 = x[m:, m:]
    B11 = y[:m, :m]
    B12 = y[:m, m:]
    B21 = y[m:, :m]
    B22 = y[m:, m:]

    a = DAC(A11, B11)
    b = DAC(A12, B21)
    C11 = a + b

    c = DAC(A11, B12)
    d = DAC(A12, B22)
    C12 = c + d

    e = DAC(A21, B11)
    f = DAC(A22, B21)
    C21 = e + f

    g = DAC(A21, B12)
    h = DAC(A22, B22)
    C22 = g + h

    result = np.zeros((2 * m, 2 * m), dtype=np.int32)

    result[:m, :m] = a[:m, :m] + b[:m, :m]
    result[:m, m:] = c[:m, :m] + d[:m, :m]
    result[m:, :m] = e[:m, :m] + f[:m, :m]
    result[m:, m:] = g[:m, :m] + h[:m, :m]

    return result[: n, : n]


#############################################
x_axis = []
y_axisDAC = []

for i in range(1, 25):
    times = []
    matrix1 = np.random.randint(5, size=(i, i))
    matrix2 = np.random.randint(5, size=(i, i))

    start = time.perf_counter_ns()
    DAC(matrix1, matrix2)
    end = time.perf_counter_ns()

    times.append(end - start)
    y_axisDAC.append(sum(times))
    x_axis.append(i)
    i += 1

#################################################
slope = 20000
x_main = [slope * (i ** 2.8074) for i in x_axis]
plt.title("Time Complexity for DAC Matrix Multiplication")
plt.plot(x_axis, x_main, ":b", label="8T(N/2) + O(N^2)")
plt.plot(x_axis, y_axisDAC, "-r", label="DAC Method")
plt.legend(loc="upper left")
plt.xlabel("n (Number of elements)")
plt.ylabel("Time (seconds)")
plt.show()
