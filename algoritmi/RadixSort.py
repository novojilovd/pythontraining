def radix_sort(A):
    reg = 1
    while max(A) / reg > 1:
        B = [False for i in range(len(A))]
        C = [False for i in range(11)]
   
        for j in range(len(A)):
            C[(A[j] // reg) % 10] += 1
             
        for i in range(1, 11):
            C[i] = C[i] + C[i - 1]
            
        for j in range(len(A) - 1, -1, -1):
            B[C[(A[j] // reg) % 10] - 1] = A[j]
            C[(A[j] // reg) % 10] -= 1
          
        for i in range(len(A)):
            A[i] = B[i]
           
        reg *= 10

if __name__ == "__main__":
    A = [55, 54, 52, 14, 3, 2, 1, 0]
    radix_sort(A)
    print(A)

