from max_heapify import max_heapify

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i, len(A))