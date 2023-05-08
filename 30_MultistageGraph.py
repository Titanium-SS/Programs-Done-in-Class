import math
def BGraph(C, n, k):
    bcost = [math.inf for i in range(n)]
    bcost[0] = 0
    d = [-1 for i in range(n)]

    for j in range(1, n):
        for r in range(j - 1, -1, -1):
            if bcost[j] > C[r][j] + bcost[r]:
                bcost[j] = C[r][j] + bcost[r]
                d[j] = r

    p = [0 for i in range(k)]
    p[0] = 0
    p[k - 1] = n - 1
    for j in range(k - 2, 0, -1):
        p[j] = d[p[j + 1]]
    return p


n = 12
k = 5
matrix = [[math.inf for i in range(n)] for j in range(n)]

matrix[0][1] = 9; matrix[0][2] = 7; matrix[0][3] = 3;
matrix[0][4] = 2; matrix[1][5] = 4; matrix[1][6] = 2;
matrix[1][7] = 1; matrix[2][5] = 2; matrix[2][6] = 7;
matrix[3][7] = 11; matrix[4][6] = 11; matrix[4][7] = 8;
matrix[5][8] = 6; matrix[5][9] = 5; matrix[6][8] = 4;
matrix[6][9] = 3; matrix[7][9] = 5; matrix[7][10] = 6;
matrix[8][11] = 4; matrix[9][11] = 2; matrix[10][11] = 5

p = BGraph(matrix, n, k)

print("The nodes selected for reaching the destination from source")
print("with minimum cost are: ")


t = len(p)
for i in range(t-1):
    print(p[i], end=" --> ")
print(p[t-1])
