def lcs_length(x, y, m, n):
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]
    d = [["" for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                d[i][j] = "↖️"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                d[i][j] = "⬆️"
            else:
                c[i][j] = c[i][j - 1]
                d[i][j] = "⬅️"

    return c, d


def print_lcs(x, d, m, n):
    if m == 0 or n == 0:
        return
    if d[m][n] == "↖️":
        print_lcs(x, d, m - 1, n - 1)
        print(x[m - 1], end="")
    elif d[m][n] == "⬆️":
        print_lcs(x, d, m - 1, n)
    else:
        print_lcs(x, d, m, n - 1)


a = "AAYUSH"
b = "AYESHA"
# a = "SHAILENDRASINGH"
# b = "ANUSHKASEHRAWAT"

c, d = lcs_length(a, b, len(a), len(b))
print("1st string is", a)
print("2nd string is", b)
print("LCS is: ", end="")
print_lcs(a, d, len(a), len(b))
print("\nwith length = ", c[len(a)][len(b)])
print("The optimal solution table is: ")
for i in c:
    print(i)

print()

print("The optimal entry table is: ")
for j in d:
    print(j)


