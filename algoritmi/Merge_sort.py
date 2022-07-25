def merge_while(A, p, q, r):
    nL = q - p + 1
    nR = r - q

    L = [True for i in range(nL + 1)]
    R = [True for i in range(nR + 1)]

    for i in range(0, nL):
        L[i] = A[p + i]
    for j in range(0, nR):
        R[j] = A[q + 1 + j]

    i = 0
    j = 0
    k = p
 
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
 
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
 
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1
    
def merge_for(A, p, q, r):
    nL = q - p + 1
    nR = r - q

    L = [True for i in range(nL + 1)]
    R = [True for i in range(nR + 1)]

    for i in range(0, nL):
        L[i] = A[p + i]
    for j in range(0, nR):
        R[j] = A[q + 1 + j]

    L[nL] = 1000000
    R[nR] = 1000000
 
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
 
        q = p + (r-p) // 2
 
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge_for(A, p, q, r)

if __name__ == '__main__':
    A = [1,3,4,-2,2,6,8,2,3,4,5,6,8]
    merge_sort(A, 0, len(A) - 1)
    print(A)
