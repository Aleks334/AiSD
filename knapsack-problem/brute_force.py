def knapsack_brute_force(items, capacity):
    n = len(items)
    best_value = 0
    best_combination = []
    best_weight = 0

    for i in range(1 << n):  # 2^n
        current_weight = 0
        current_value = 0
        current_combination = []
        selected_items_indices = []

        for j in range(n):
            if (i >> j) & 1:  
                current_weight += items[j][0]
                current_value += items[j][1]
                current_combination.append(items[j])
                selected_items_indices.append(j + 1) 

        if current_weight <= capacity and current_value > best_value:
            best_value = current_value
            best_combination = selected_items_indices
            best_weight = current_weight

    return best_combination, best_weight, best_value