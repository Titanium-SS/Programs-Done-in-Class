import random
import time
import matplotlib.pyplot as plt
import math


###########################################
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    size = high - low + 1
    stack = [0] * size
    top = -1
    top += 1
    stack[top] = low
    top -= 1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[high]
        top -= 1

        p = partition(array, low, high)

        if p - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1

        if p + 1 < high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high


############################################
# Worst Case
elements = 100
minimum = 1000000
maximum = 9999999
x_axis = []
y_axis = []

while elements <= 10000:
    times = []
    arr = random.sample(range(minimum, maximum), elements)

    start = time.perf_counter_ns()
    quickSort(arr, 0, elements - 1)
    end = time.perf_counter_ns()

    times.append(end - start)
    y_axis.append(sum(times))
    x_axis.append(elements)
    elements = elements + 100

slope = 0.5
x_log = [(slope * elements * (math.log(elements))) for elements in x_axis]
plt.title("Time Complexity of QUICK SORT")
plt.plot(x_axis, x_log, ":g", label="O(n*log(n))")
plt.plot(x_axis, y_axis, "--r", label="Iterative Quick Sort")
plt.legend(loc="upper left")
plt.xlabel("n (Number of elements)")
plt.ylabel("Time (seconds)")
plt.show()
