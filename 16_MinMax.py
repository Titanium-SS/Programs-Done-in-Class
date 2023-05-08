import random
import time
import matplotlib.pyplot as plt
###########################################


def MinMax(array, low, high):
    if low == high:
        return array[low], array[high]

    elif low == high-1:
        if array[low] < array[high]:
            minimum = array[low]
            maximum = array[high]
        else:
            minimum = array[high]
            maximum = array[low]

        return minimum, maximum

    else:
        mid = (low+high)//2

        Lmin, Lmax = MinMax(array, low, mid)
        Rmin, Rmax = MinMax(array, mid+1, high)

    if Lmin < Rmin:
        minimum = Lmin
    else:
        minimum = Rmin

    if Lmax < Rmax:
        maximum = Rmax
    else:
        maximum = Lmax

    return minimum, maximum 


elements = 10
MINIMUM = 1000
MAXIMUM = 9999999
x_axis = []
y_axis = []

while elements <= 1000000:
    times = []
    array = random.sample(range(MINIMUM, MAXIMUM), elements)
    low = 0
    high = len(array) - 1

    start = time.perf_counter_ns()
    minimum, maximum = MinMax(array, low, high)
    end = time.perf_counter_ns()

    """
    print("The minimum value in the array is ", minimum)
    print("The maximum value in the array is ", maximum)
    print()
    """

    times.append(end - start)
    y_axis.append(sum(times))
    x_axis.append(elements)
    elements = elements * 10
#################################################


slope = 250
x_n = [slope * elements for elements in x_axis]
plt.title("Time Complexity of MinMax Algorithm")
plt.plot(x_axis, x_n, ":b", label="O(n)")
plt.plot(x_axis, y_axis, "-r", label="MINMAX")
plt.legend(loc="upper left")
plt.xlabel("n (Number of elements)")
plt.ylabel("Time (seconds)")
plt.show()