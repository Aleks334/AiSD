from utils import load_data_from_keyboard, load_data_from_file

def knapsack_dynamic(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = items[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
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

def main():
    print("Wybierz metodę wczytywania danych:")
    print("1. Z klawiatury")
    print("2. Z pliku tekstowego")

    choice = input("Wybór (1/2): ")

    items = None
    capacity = None

    if choice == '1':
        items, capacity = load_data_from_keyboard()
    elif choice == '2':
        items, capacity = load_data_from_file()
    else:
        print("Nieprawidłowy wybór.")
        return

    if items is None or capacity is None:
        return

    print("\n--- Rozwiązanie algorytmem dynamicznym ---")
    selected_items_indices, total_weight, total_value = knapsack_dynamic(items, capacity)

    print(f"Wybrane przedmioty (indeksy): {selected_items_indices}")
    print(f"Sumaryczny rozmiar: {total_weight}")
    print(f"Sumaryczna wartość: {total_value}")


if __name__ == "__main__":
    main()