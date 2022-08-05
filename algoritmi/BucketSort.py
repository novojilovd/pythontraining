import InsertionSort

def bucket_sort(A):
    n = len(A)
    B = [[] for i in range(n)]

    for i in range(n):
        B[int(n * A[i])].append(A[i])
    
    A.clear()

    for i in range(n):
        InsertionSort.insertion_sort(B[i])
        if B[i]:
            A.extend(B[i])
        
if __name__ == "__main__":
    A = [0.54, 0.21, 0.11]
    bucket_sort(A)
    print(id(A))
