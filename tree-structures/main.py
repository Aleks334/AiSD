def menu():
    while True:
        print("\nMenu:")
        print("1. Wyszukaj w drzewie min/maks klucz z ścieżką poszukiwania")
        print("2. Wyszukaj poziom, na którym znajduje się węzeł z podanym kluczem i wypisz wszystkie klucze na tym poziomie")
        print("3. Wypisz wszystkie klucze drzewa malejąco")
        print("4. Wypisz poddrzewo w pre-order dla podanego korzenia, jego wysokosć. Usuń je (post-order)")
        print("5. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "5":
            break
        elif choice == "1":
            return
        elif choice == "2":
            return
        elif choice == "3":
            return
        elif choice == "4":
            return
        else:
            print("Niewłaściwy wybór. Spróbuj ponownie")

if __name__ == "__main__":
    menu()