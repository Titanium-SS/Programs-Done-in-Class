def SumOfSubsets(x, w, m, s, k, r):
    x[k] = 1

    if s + w[k] == m:
        print(x[0:k + 1])

    elif s + w[k] + w[k + 1] <= m:
        SumOfSubsets(x, w, m, s + w[k], k + 1, r - w[k])

    if (s + r - w[k] >= m) and (s + w[k + 1] <= m):
        x[k] = 0
        SumOfSubsets(x, w, m, s, k + 1, r - w[k])


weights = [6, 4, 2, 1, 5, 7]
weights.sort()
print("The sorted list: ", weights)

# m = required sum = 11
# r = sum of all the elements in list given = 25

print("The solution subsets are: \n")
setx = [0] * len(weights)
SumOfSubsets(setx, weights, 11, 0, 0, 25)
