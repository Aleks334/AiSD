def knapsack_greedy(items, capacity):
    indexed_items = [(i + 1, weight, value, value / weight) for i, (weight, value) in enumerate(items)]
    indexed_items.sort(key=lambda x: x[3], reverse=True)

    total_weight = 0
    total_value = 0
    selected_indices = []

    for idx, weight, value, _ in indexed_items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            selected_indices.append(idx)

    return selected_indices, total_weight, total_value