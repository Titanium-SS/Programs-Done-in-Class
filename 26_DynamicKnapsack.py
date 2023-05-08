def KnapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    table = []
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
                table.append(K[i][w])
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
                table.append(K[i][w])
            else:
                K[i][w] = K[i - 1][w]
                table.append(K[i][w])

    # Printing The Table Array so formed

    size = len(table)
    line = []
    print("The Intermediate Solution Table so formed is: ")
    for i in range(0, (W + 1) * (n + 1), W + 1):
        line.append(i)

    for j in range(0, size):
        for k in range(0, (n + 1)):
            if j == line[k]:
                print()
        print(table[j], end="\t\t")

    return K[n][W]


if __name__ == '__main__':
    profit = [10, 40, 30, 50]
    weight = [5, 4, 6, 3]
    W = 10
    n = len(profit)
    print("\n\nFinal Profit is: ", KnapSack(W, weight, profit, n))
