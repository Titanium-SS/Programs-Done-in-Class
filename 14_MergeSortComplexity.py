import random
import time
import matplotlib.pyplot as plt
import math


###########################################
def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = array[l + i]

    for j in range(0, n2):
        R[j] = array[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def mergeSort(array, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(array, l, m)
        mergeSort(array, m + 1, r)
        merge(array, l, m, r)


############################################
elements = 1000
minimum = 1000000
maximum = 9999999
x_axis = []
y_axis = []

while elements <= 10000:
    times = []
    arr = random.sample(range(minimum, maximum), elements)

    start = time.perf_counter_ns()
    mergeSort(arr, 0, elements - 1)
    end = time.perf_counter_ns()

    times.append(end - start)
    y_axis.append(sum(times))
    x_axis.append(elements)
    elements = elements + 100
#################################################
slope = 800

x_log = [(slope * elements * (math.log10(elements))) for elements in x_axis]
plt.title("Time Complexity of MERGE SORT")
plt.plot(x_axis, x_log, ":b", label="O(n*log(n))")
plt.plot(x_axis, y_axis, "-r", label="Merge Sort")
plt.legend(loc="upper left")
plt.xlabel("n (Number of elements)")
plt.ylabel("Time (seconds)")
plt.show()
