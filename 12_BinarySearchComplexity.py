import random
import time
import matplotlib.pyplot as plt
import math


#################################################
# Binary Search
def binary_search(array, val):
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if array[mid] < val:
            low = mid + 1

        elif array[mid] > val:
            high = mid - 1

        else:
            return mid
    return -1


#################################################
# Worst Case
elements = 1000
minimum = 1000000
maximum = 9999999
x_axis = []
y_axis = []

x = int(input("Enter the number to be searched: "))

while elements <= 10000:
    times = []
    arr = random.sample(range(minimum, maximum), elements)
    arr.sort()

    start = time.perf_counter_ns()
    binary_search(arr, x)
    end = time.perf_counter_ns()

    times.append(end - start)
    y_axis.append(sum(times))
    x_axis.append(elements)
    elements = elements * 10
#################################################
# Best Case
elements = 1000
y_axisB = []

while elements <= 10000:
    timesB = []
    arr = random.sample(range(minimum, maximum), elements)
    arr.sort()

    middle = int(len(arr) / 2)

    start = time.perf_counter_ns()
    binary_search(arr, arr[middle])
    end = time.perf_counter_ns()

    timesB.append(end - start)
    y_axisB.append(sum(timesB))
    elements = elements * 10
#################################################

slope = 1000
x_sq = [(slope * (math.log10(elements))) for elements in x_axis]
plt.title("Time Complexity of BINARY SEARCH")
plt.plot(x_axis, x_sq, ":b", label="O(log(n))")
plt.plot(x_axis, y_axis, "-r", label="Binary Search Worst Case")
plt.plot(x_axis, y_axisB, "--g", label="Binary Search Best Case")
plt.legend(loc="upper left")
plt.xlabel("n (Number of elements)")
plt.ylabel("Time (seconds)")
plt.show()
