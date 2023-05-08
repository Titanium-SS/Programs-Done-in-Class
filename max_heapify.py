def max_heapify(A, i, heap_size):
    l = (i * 2) + 1
    r = l + 1
    largest = i
    if l < heap_size and A[l] > A[i]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)
        

