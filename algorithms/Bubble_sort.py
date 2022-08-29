def bubble_sort(A):
    for i in range(0, len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

if __name__ == "__main__":
    A = [9,8,7,6,5,4,3,2,1]
    bubble_sort(A)
    print(A)
