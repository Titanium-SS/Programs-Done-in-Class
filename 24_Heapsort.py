import matplotlib.pyplot as plt
import random
import sys
import timeit
import math
from build_max_heap import build_max_heap
from max_heapify import max_heapify

sys.setrecursionlimit(5000)


def heapsort(A):
    heap_size = len(A)
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size = heap_size - 1
        max_heapify(A, 0, heap_size)



# Code for plotting:
MIN_LEN = 50
MAX_LEN = 10000
STEP = 50
ITER = 1
x_axis = list(range(MIN_LEN, MAX_LEN + 1, STEP))
avg_case = []
fig, axs = plt.subplots(1, figsize=(6, 5))


def measure(arr):
    t = timeit.Timer(lambda: heapsort(arr))
    res = t.timeit(ITER) * 1000
    return res / ITER


# region Avg Case
for i in x_axis:
    time_taken = measure(list(random.sample(range(i), i)))
    avg_case.append(time_taken)

c = 0
for n, t in zip(x_axis, avg_case):
    c = (c + t / (n * math.log(n)))/2

x_log_x = [(c * (x * math.log(x))) for x in x_axis]
axs.plot(x_axis, avg_case, "-b", label="Heap Sort(Average Case)")
axs.plot(x_axis, x_log_x, "--r", label="O($nlog(n)$)")
axs.legend(loc="upper left")
axs.set_xlabel("n (Number of elements)")
axs.set_ylabel("Time (Milliseconds)")
# endregion

# Save image
fig.savefig('heapsort.png', dpi=300)

# And Show it in new window
plt.show()
