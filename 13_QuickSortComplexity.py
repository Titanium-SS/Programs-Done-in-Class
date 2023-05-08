import random
import time
import matplotlib.pyplot as plt
import math


###########################################
# Quick Sort
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):

        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


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
    quick_sort(arr, 0, elements - 1)
    end = time.perf_counter_ns()

    times.append(end - start)
    y_axis.append(sum(times))
    x_axis.append(elements)
    elements = elements + 100

slope = 0.2
x_sq = [(slope * elements ** 2) for elements in x_axis]
x_log = [(slope * elements * (math.log10(elements))) for elements in x_axis]
plt.title("Time Complexity of QUICK SORT")
plt.plot(x_axis, x_sq, "-k", label="O(n^2)")
plt.plot(x_axis, x_log, ":g", label="Quick Sort Best Case = O(n*log(n))")
plt.plot(x_axis, y_axis, "--r", label="Quick Sort Worst Case")
plt.legend(loc="upper left")
plt.xlabel("n (Number of elements)")
plt.ylabel("Time (seconds)")
plt.show()