def counting_sort(A, B, k):
    C = [False for i in range(k + 1)]
    
    for j in range(len(A)):
        C[A[j]] += 1
    
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

if __name__ == "__main__":
    A = [5,5,5,4,3,2,1,0]
    B = [False for i in range(len(A))]
    counting_sort(A, B, max(A))
    print(B)    
