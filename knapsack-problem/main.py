from utils import load_data_from_keyboard, load_data_from_file
from brute_force import knapsack_brute_force
from dynamic import knapsack_dynamic
from greedy import knapsack_greedy

def choose_data_mode():
    print("Wybierz metodę wczytywania danych:")
    print("1. Z klawiatury")
    print("2. Z pliku tekstowego")
    print("0. Powrót do menu głównego")
    choice = input("Wybierz (1/2/0): ")
    
    if choice == '1':
        return load_data_from_keyboard()
    elif choice == '2':
        return load_data_from_file()
    elif choice == '0':
        return None, None
    else:
        print("Nieprawidłowy wybór.")
        return None, None

def main():
    while True:
        print("\n--- MENU PROGRAMU ---")
        print("Wybierz algorytm:")
        print("1. Siłowy")
        print("2. Dynamiczny")
        print("3. Zachłanny")
        print("0. Wyjście")
        algo_choice = input("Wybierz (1/2/3/0): ")

        if algo_choice == '0':
            print("Zakończono działanie programu.")
            break

        items, capacity = choose_data_mode()
        if items is None or capacity is None:
            continue

        if algo_choice == '1':
            print("\n--- Rozwiązanie algorytmem siłowym ---")
            selected_items_indices, total_weight, total_value = knapsack_brute_force(items, capacity)
        elif algo_choice == '2':
            print("\n--- Rozwiązanie algorytmem dynamicznym ---")
            selected_items_indices, total_weight, total_value = knapsack_dynamic(items, capacity)
        elif algo_choice == '3':
            print("\n--- Rozwiązanie algorytmem zachłannym ---")
            selected_items_indices, total_weight, total_value = knapsack_greedy(items, capacity)
        else:
            print("Nieprawidłowy wybór algorytmu.")
            continue

        print(f"Wybrane przedmioty (indeksy od 1): {selected_items_indices}")
        print(f"Sumaryczny rozmiar: {total_weight}")
        print(f"Sumaryczna wartość: {total_value}")

if __name__ == "__main__":
    main()