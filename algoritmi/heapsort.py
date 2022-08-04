def parent(i):
    return i // 2

def left(i):
    return 2 * i + 1
    
def right(i):
    return 2 * i + 2

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    
    if (l < heap_size) and (A[l] > A[i]):
        largest = l
    else:
        largest = i
    
    if (r < heap_size) and (A[r] > A[largest]):
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range (len(A) // 2 - 1, -1, -1):
        max_heapify(A, i)

def heapsort(A):
    global heap_size

    build_max_heap(A)

    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0)

if __name__ == '__main__':
    A = [6,5,4,5,6,7,3,2,1]
    heap_size = len(A)
    heapsort(A)
    print(A)
