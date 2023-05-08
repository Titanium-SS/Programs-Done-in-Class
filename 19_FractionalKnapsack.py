class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def FractionalKnapsack(W, arr):
    # Sorting items as profit/weight = pi/wi in non-increasing order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    solution = 0.0  # Initially Profit is Zero

    for item in arr:
        if item.weight <= W:
            solution += item.profit
            W -= item.weight
            print("Added item with profit of (", item.profit, ") with weight (", item.weight,
                  ") and remaining capacity in Knapsack is ", W)
            print("Profit till now: ", solution)
            print()

        else:
            solution += item.profit * W / item.weight
            print("Added item with profit of (", item.profit, ") with weight (", item.weight,
                  ") and remaining capacity in Knapsack is ", 0, "\nBasically added part of the item with profit of (",
                  item.profit * W / item.weight, ") with weight (", W, ")")
            print("Profit till now: ", solution)
            print()
            break

    return solution


if __name__ == "__main__":
    W = 25

    # arr = [Item(25, 18), Item(24, 15), Item(15, 10)]
    arr = [Item(15, 10), Item(10, 8), Item(8, 9), Item(16, 20), Item(15, 5), Item(30, 20), Item(15, 15)]

    optimal_solution = FractionalKnapsack(W, arr)
    print("Hence maximum profit is: ", optimal_solution)
