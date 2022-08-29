A = [[1,2,3],[2,3,4],[4,5,6]]
B = [[1,2,3],[2,3,4],[4,5,6]]
C = [[True for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        C[i][j] = 0
        for k in range(3):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

print(C)
        
