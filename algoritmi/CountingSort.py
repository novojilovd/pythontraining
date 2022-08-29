def counting_sort(A, k):
    B = [False for i in range(len(A))]
    C = [False for i in range(k + 1)]
    
    for j in range(len(A)):
        C[A[j]] += 1
    
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B


if __name__ == "__main__":
    A = [55, 54, 52, 14, 3, 2, 1, 0]
    print(counting_sort(A, max(A)))
