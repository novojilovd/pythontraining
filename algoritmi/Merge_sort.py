def merge(A, p, q, r):
    nL = q - p
    nR = r - q
    L = []
    R = []

    for i in range(nL):
        L.append(A[p + i])
    for j in range(nR):
        R.append(A[q + j])

    L.append(1000000)
    R.append(1000000)
    
    i = 0
    j = 0

    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p ,r):
    if p < r:
        q = (p + r) // 2
        print(q)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == '__main__':
    A = [1,3,4,2,6,8,2,3,4,5,6,8]
    merge_sort(A, 0, len(A))
    print(A)
