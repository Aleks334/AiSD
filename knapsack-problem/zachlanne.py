from utils import load_data_from_keyboard, load_data_from_file

def knapsack_greedy(items, capacity):
    indexed_items = [(i + 1, w, v, v / w) for i, (w, v) in enumerate(items)]
    indexed_items.sort(key=lambda x: x[3], reverse=True)

    total_weight = 0
    total_value = 0
    selected_indices = []

    for idx, w, v, _ in indexed_items:
        if total_weight + w <= capacity:
            total_weight += w
            total_value += v
            selected_indices.append(idx)

    return selected_indices, total_weight, total_value

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

    print("\n--- Rozwiązanie algorytmem zachłannym ---")
    selected_items_indices, total_weight, total_value = knapsack_greedy(items, capacity)

    print(f"Wybrane przedmioty (indeksy): {selected_items_indices}")
    print(f"Sumaryczny rozmiar: {total_weight}")
    print(f"Sumaryczna wartość: {total_value}")


if __name__ == "__main__":
    main()
