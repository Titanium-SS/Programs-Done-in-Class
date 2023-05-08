def matrix_chain_multiplication(arr, n):
    m = [[0] * n for i in range(n)]
    s = [[0] * n for i in range(n - 1)]
    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + arr[i - 1] * arr[k] * arr[j]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[1][n - 1], m, s


arr = [30, 35, 15, 5, 10, 20, 25]
n = len(arr)


finalcost, costmatrix, S = matrix_chain_multiplication(arr, n)

print("\nThe matrices so formed are of the following dimensions: ")
for i in range(n - 1):
    print(arr[i], "*", arr[i + 1], end="    ")

print("\n\nThe Cost Matrix: ")
for k in costmatrix:
    print(k)

print("\nThe State Matrix: ")
for k in S:
    print(k)

print(f"\nThe minimum no. of Scalar multiplications are : {finalcost}")
