from tests import run_all_tests
from utils import load_numbers_from_file, measure_execution_time
from data_generator import generate_sequences
import trees as t
from tree_operations import bin_tree_height, get_node_bst, get_node_hmin, max_key_bst, lvl_order_iteration, max_key_hmin, min_key, pre_order, remove_post_order, reverse_in_order

def menu():
    while True:
        print("\nMenu:")
        print("1. Wyszukaj w drzewie min/maks klucz z ścieżką poszukiwania")
        print("2. Wyszukaj poziom, na którym znajduje się węzeł z podanym kluczem i wypisz wszystkie klucze na tym poziomie") 
        print("3. Wypisz wszystkie klucze drzewa malejąco")
        print("4. Wypisz poddrzewo w pre-order dla podanego korzenia, jego wysokosć. Usuń je (post-order)")
        print("5. Uruchom testy")
        print("6. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "6":
            break
        elif choice == "5":
            run_all_tests()

        elif choice in ["1", "2", "3", "4"]:
            input_type = input("Wybierz źródło danych (1: plik, 2: generator): ")
            sequence = []

            if input_type == "1":
                filename = "file.txt"
                sequence = load_numbers_from_file(filename)
            else:
                k = int(input("Podaj rozmiar sekwencji: "))
                sequence = generate_sequences(k)["random"][0]
            
            bst_root = t.create_bst(sequence)
            avl_root = t.create_avl(sequence)
            heap_root = t.create_heap(sequence)
            
            print("-" * 20)
            print("Wyniki dla BST:")
            if choice == "1":
                time1, (min, path1) = measure_execution_time(min_key, bst_root.root)
                time2, (max, path2) = measure_execution_time(max_key_bst, bst_root.root)
                
                print(f"Min key: {min}, Path: {path1}. Time: {time1} ms")
                print(f"Max key: {max}, Path: {path2}. Time: {time2} ms")
            
            elif choice == "2":
                key = int(input("Podaj klucz do wyszukania: "))
                time, (lvl, keysOnLvl) = measure_execution_time(lvl_order_iteration, bst_root.root, key)
                if lvl != -1:
                    print(f"Level: {lvl}, Keys on that level: {keysOnLvl}. Time: {time} ms")
                else:
                    print("Klucz nie znaleziony")
            
            elif choice == "3":
                print("Elementy w porządku malejącym:")
                time = measure_execution_time(reverse_in_order, bst_root.root)
                print(f"Time: {time} ms")
            
            elif choice == "4":
                key = int(input("Podaj klucz korzenia poddrzewa: "))
                subTreeRoot = get_node_bst(bst_root.root, key)
                if subTreeRoot:
                    print("Pre-order:")
                    time = measure_execution_time(pre_order, subTreeRoot)
                    print(f"Time: {time} ms")

                    h = bin_tree_height(subTreeRoot)
                    print(f"Height: {h}")
                    time = measure_execution_time(remove_post_order, subTreeRoot)
                    print(f"Time: {time} ms")
                else:
                    print("Klucz nie znaleziony")

        else:
            print("Niewłaściwy wybór. Spróbuj ponownie")


if __name__ == "__main__":
    menu()