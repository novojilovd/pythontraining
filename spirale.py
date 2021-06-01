N = int(input("Write how big matrix: \n"))
n = 0
m = 0
a = [i+1 for i in range(N**2)]
b = [[0] * N for i in range(N)]
while m < N:
    
    for i in range(m, N):
        b[m][i] = a[n]
        n += 1

    m += 1

    for i in range(m, N):
        b[i][N-1] = a[n]
        n += 1

    for i in range(m, N):
        b[N-1][N-1-i] = a[n]
        n += 1

    for i in range(m, N-1):
        b[N-1-i][m-1] = a[n]
        n += 1
    
    N -= 1

for part in b[::]:
    print(part)
