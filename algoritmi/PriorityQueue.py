import Heapsort

# non-increase heap

def heap_maximum(A):
    return A[0]

def heap_extract_max(A, heap_size):
    if heap_size < 1:
        print("Heap is empty")

    max = A[0]
    A[0] = A[heap_size - 1]
    heap_size -= 1
    A.pop()
    Heapsort.max_heapify(A, heap_size, 0)

    return max

def heap_increase_key(A, i, key):
    if key < A[i]:
        print("New key less then current")
    A[i] = key
    while i > 0 and A[Heapsort.parent(i)] < A[i]:
        A[i], A[Heapsort.parent(i)] = A[Heapsort.parent(i)], A[i]
        i = Heapsort.parent(i)

def max_heap_insert(A, key):
    A.append(-1000000)
    heap_increase_key(A, len(A) - 1, key)

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]

    Heapsort.build_max_heap(A, len(A))
    print(A)

    print(heap_maximum(A))

    print(heap_extract_max(A, len(A)), A)

    heap_increase_key(A, 3, 20)
    print(A)

    max_heap_insert(A, 30)
    print(A)
    
