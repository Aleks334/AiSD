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

def load_data_from_keyboard():
    while True:
        try:
            n_str, b_str = input("Podaj liczbę przedmiotów i pojemność plecaka (oddzielone spacją): ").split()
            n = int(n_str)
            b = int(b_str)
            break
        except ValueError:
            print("Nieprawidłowy format.")

    items = []
    print(f"Podaj rozmiar i wartość dla {n} przedmiotów (np. '3 7'):")
    for i in range(n):
        while True:
            try:
                r_str, w_str = input(f"Przedmiot {i + 1}: ").split()
                r = int(r_str)
                w = int(w_str)
                items.append((r, w))
                break
            except ValueError:
                print("Nieprawidłowy format.")
    return items, b

def load_data_from_file(filename="dane.txt"):
    """
    Format pliku:
    pierwszy wiersz: liczba przedmiotów, pojemność plecaka
    kolejne wiersze: rozmiar przedmiotu, wartość przedmiotu
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        n, b = map(int, lines[0].split())
        items = []
        for i in range(1, n + 1):
            r, w = map(int, lines[i].split())
            items.append((r, w))
        return items, b
    except FileNotFoundError:
        print(f"Błąd: Plik '{filename}' nie został znaleziony.")
        return None, None
    except ValueError:
        print(f"Błąd: Nieprawidłowy format danych w pliku '{filename}'.")
        return None, None

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

    print("\n--- Rozwiązanie algorytmem siłowym ---")
    selected_items_indices, total_weight, total_value = knapsack_brute_force(items, capacity)

    print(f"Wybrane przedmioty (indeksy): {selected_items_indices}")
    print(f"Sumaryczny rozmiar: {total_weight}")
    print(f"Sumaryczna wartość: {total_value}")

if __name__ == "__main__":
    main()