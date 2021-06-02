N = int(input("Write how big matrix: \n"))
n = 0
m = 0

if (N % 2): 
    k = (N // 2) + 1
    check = False
else:   
    k = N // 2
    check = True

a = [i+1 for i in range(N**2)]
b = [[0] * N for i in range(N)]

for j in range(k):
    print(m,' ',N)
    for i in range(m, N):
        b[m][i] = a[n]
        n += 1

    for name in b[::]:
        print(name)
    print('\n')

    if (j+1) == k and not check: break

    for i in range(m + 1, N):
        b[i][N-1] = a[n]
        n += 1

    for name in b[::]:
        print(name)
    print('\n')

    for i in range(m + 1, N):
        if m > 0 and (N-2) == m:
            b[N-1][N-i] = a[n]
        else: 
            b[N-1][N-1-i] = a[n]
        n += 1

    for name in b[::]:
        print(name)
    print('\n')

    if (j+1) == k and check: break
    
    for i in range(m + 1, N - 1):
        b[N-1-i][m] = a[n]
        n += 1

    for name in b[::]:
        print(name)
    print('\n')

    m += 1
    N -= 1
for name in b[::]:
    print(name)
