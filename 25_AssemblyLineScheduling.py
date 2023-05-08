def AssemblyLineScheduling(a, t, e, x, n):
    f1 = [0] * n    # f1[i] represents the minimum time to leave station i in line 1
    f2 = [0] * n    # f2[i] represents the minimum time to leave station i in line 2

    s1 = [0] * n    # s1[i] represents the station number in line 1
    s2 = [0] * n     # s2[i] represents the station number in line 2

    f1[0] = e[0] + a[0][0]      # time taken to leave first station in line 1
    s1[0] = 1

    f2[0] = e[1] + a[1][0]      # time taken to leave first station in line 2
    s2[0] = 2

    # choose the minimum time to reach station i in line 1 or 2
    for i in range(1, n):
        if f1[i - 1] + a[0][i] <= f2[i - 1] + t[1][i] + a[0][i]:
            f1[i] = f1[i - 1] + a[0][i]
            s1[i] = 1
        else:
            f1[i] = f2[i - 1] + t[1][i] + a[0][i]
            s1[i] = 2

        if f2[i - 1] + a[1][i] <= f1[i - 1] + t[0][i] + a[1][i]:
            f2[i] = f2[i - 1] + a[1][i]
            s2[i] = 2
        else:
            f2[i] = f1[i - 1] + t[0][i] + a[1][i]
            s2[i] = 1

    # choose the minimum time to exit the assembly line
    if f1[n - 1] + x[0] <= f2[n - 1] + x[1]:
        time = f1[n - 1] + x[0]
        station = 1
    else:
        time = f2[n - 1] + x[1]
        station = 2

    print("Minimum Time: ", time)

    # print the stations in reverse order
    print("Stations Traversed(In reverse order):", station, end=' ')
    i = station - 1
    for j in range(n - 1, 0, -1):
        if i == 0:
            print(s1[j], end=' ')
        else:
            print(s2[j], end=' ')
        i = s1[j - 1] - 1 if s1[j - 1] == i else s2[j - 1] - 1
    print("\nStation", station, "is the starting station")


n = 4                               # number of stations
a = [[4, 5, 3, 2], [2, 10, 1, 4]]   # time taken at each station
t = [[0, 7, 4, 5], [0, 9, 2, 8]]    # time taken to switch lines
e = [10, 12]                        # time taken to enter lines 1 & 2
x = [18, 7]                         # time taken to exit lines 1 & 2

if __name__ == '__main__':
    AssemblyLineScheduling(a, t, e, x, n)
