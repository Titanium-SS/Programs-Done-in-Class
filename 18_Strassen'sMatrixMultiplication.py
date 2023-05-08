import time
import matplotlib.pyplot as plt
import numpy as np
#############################################


def strassen(x, y):
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

    p = strassen(A11 + A22, B11 + B22)
    q = strassen(A21 + A22, B11)
    r = strassen(A11, B12 - B22)
    s = strassen(A22, B21 - B11)
    t = strassen(A11 + A22, B22)
    u = strassen(A21 - A11, B11 + B12)
    v = strassen(A12 - A22, B21 + B22)

    result = np.zeros((2 * m, 2 * m), dtype=np.int32)

    result[:m, :m] = p + s - t + v
    result[:m, m:] = r + t
    result[m:, :m] = q + s
    result[m:, m:] = p + r - q + u

    return result[: n, : n]


#############################################
x_axis = []
y_axis = []

for i in range(1, 10):
    times = []
    matrix1 = np.random.randint(9, size=(i, i))
    matrix2 = np.random.randint(9, size=(i, i))

    print(matrix1)
    print(matrix2)

    start = time.perf_counter_ns()
    strassen(matrix1, matrix2)
    end = time.perf_counter_ns()

    print(strassen(matrix1, matrix2))
    print()

    times.append(end - start)
    y_axis.append(sum(times))
    x_axis.append(i)
    i += 1

#################################################
slope = 20000
x_main = [slope * (i ** 2.8074) for i in x_axis]
plt.title("Time Complexity for Strassen's Matrix Multiplication")
plt.plot(x_axis, x_main, ":b", label="8T(N/2) + O(N^2) = O(N^2.8074)")
plt.plot(x_axis, y_axis, "-r", label="Strassen's Method")
plt.legend(loc="upper left")
plt.xlabel("n (Number of elements)")
plt.ylabel("Time (seconds)")
plt.show()
