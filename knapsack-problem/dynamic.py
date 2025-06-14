def knapsack_dynamic(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for c in range(capacity + 1):
            if weight <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - weight] + value)
            else:
                dp[i][c] = dp[i - 1][c]

    selected = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            selected.append(i)
            c -= items[i - 1][0]
    selected.reverse()
    total_weight = sum(items[i - 1][0] for i in selected)
    total_value = sum(items[i - 1][1] for i in selected)

    return selected, total_weight, total_value