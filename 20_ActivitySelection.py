def ActivitySelection(arr, n):
    selected = []
    Activity.sort(key=lambda x: x[1])   # Sort jobs according to finish time
    i = 0                               # The first activity always gets selected
    selected.append(arr[i])

    for j in range(1, n):

        '''If this activity has start time greater than or
            equal to the finish time of previously selected
            activity, then it is selected'''

        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
    return selected


if __name__ == '__main__':
    Activity = [[7, 10], [8, 11], [9, 15], [10, 25], [16, 19]]
    n = len(Activity)

    selected = ActivitySelection(Activity, n)
    print("Following activities are selected :")
    print(selected[0], end="")
    for i in range(1, len(selected)):
        print()
        print(selected[i], end="")


"""
    [[  0,   0,   0,   0,   0,   0,   0,   0],
    [ 300,   0,   0,   0,   0,   0,   0,   0],
    [ 100, 800,   0,   0,   0,   0,   0,   0],
    [   0,   0,1200,   0,   0,   0,   0,   0],
    [   0,   0,   0,1500,   0, 250,   0,   0],
    [   0,   0,   0,1000,   0,   0, 900,1400],
    [   0,   0,   0,   0,   0,   0,   0,1000],
    [   0,   0,   0,   0,   0,   0,   0,   0]]
"""