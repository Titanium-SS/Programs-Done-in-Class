import random
import time
import matplotlib.pyplot as plt


#################################################
# Insertion Sort
def insertion_sort(array):
    if (n := len(array)) <= 1:
        return
    for i in range(1, n):

        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


#################################################
# Worst Case
elements = 100
minimum = 1000000
maximum = 9999999
x_axis = []
y_axis = []

while elements <= 1000:
    times = []
    arr = random.sample(range(minimum, maximum), elements)
    arr.reverse()
    start = time.perf_counter_ns()
    insertion_sort(arr)
    end = time.perf_counter_ns()
    times.append(end - start)
    y_axis.append(sum(times))
    x_axis.append(elements)
    elements = elements + 100


#################################################
# Best Case
elements = 100
y_axisB = []

while elements <= 1000:
    timesB = []
    arr = random.sample(range(minimum, maximum), elements)

    insertion_sort(arr)

    start = time.perf_counter_ns()
    insertion_sort(arr)
    end = time.perf_counter_ns()

    timesB.append(end - start)
    y_axisB.append(sum(timesB))
    elements = elements + 100


#################################################
# Average Case
def half_sort(array, n):
    arr1 = array[:n // 2]
    arr2 = array[n // 2:]
    arr1.sort()
    arr2.sort(reverse=True)
    return arr1 + arr2


elements = 100
y_axisA = []

while elements <= 1000:
    timesA = []
    arr = random.sample(range(minimum, maximum), elements)

    half_sort(arr, elements)

    start = time.perf_counter_ns()
    insertion_sort(arr)
    end = time.perf_counter_ns()

    timesA.append(end - start)
    y_axisA.append(sum(timesA))
    elements = elements + 100


#################################################
slope = 40
x_sq = [(slope * (elements ** 2)) for elements in x_axis]
plt.title("Time Complexity of INSERTION SORT")
plt.plot(x_axis, x_sq, ":k", label="O(x^2)")
plt.plot(x_axis, y_axis, "-r", label="Insertion Sort(Worst Case)")
plt.plot(x_axis, y_axisA, "-.b", label="Insertion Sort(Average Case)")
plt.plot(x_axis, y_axisB, "--g", label="Insertion Sort(Best Case)")
plt.legend(loc="upper left")
plt.xlabel("n (Number of elements)")
plt.ylabel("Time (seconds)")
plt.show()
