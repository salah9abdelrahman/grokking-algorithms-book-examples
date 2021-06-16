# o(n + c) where n is number of items and c is capacity
def solve_knapsack(weights, profits, capacity):
    n = len(weights)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    grid = [[0 for _ in range(capacity)] for _ in range(n)]
    # first row
    for c in range(capacity):
        if weights[0] <= capacity:
            grid[0][c] = profits[0]

    for i in range(1, n):
        for j in range(capacity):
            # profit1 the last max value for this capacity
            profit1 = grid[i-1][j]
            # profit2 this item and the max value for the remaining capacity if any
            profit2 = 0
            if weights[i] <= j + 1:
                profit2 = profits[i]
                remainingCapacity = j + 1 - weights[i]
                if remainingCapacity > 0:
                    profit2 += grid[i - 1][remainingCapacity - 1]
            grid[i][j] = max(profit1, profit2)
    print(grid)
    return grid[-1][-1]


def main():
    weights = [1, 4, 3]
    profits = [1500, 3000, 2000]
    capacity = 4
    print(solve_knapsack(weights, profits, capacity))

    # add iphone
    weights.append(1)
    profits.append(2000)
    print(solve_knapsack(weights, profits, capacity))


if __name__ == '__main__':
    main()
