DEFAULT_INPUT_FILE_NAME = "dane.txt"

def load_data_from_keyboard():
    try:
        n = int(input("Podaj liczbę przedmiotów: "))
        if n <= 0:
            raise ValueError("Liczba przedmiotów musi być liczbą naturalną.")
        
        capacity = int(input("Podaj pojemność plecaka: "))
        if capacity <= 0:
            raise ValueError("Pojemność musi być liczbą naturalną.")
        
        items = []
        for i in range(n):
            w = int(input(f"Podaj wagę przedmiotu {i+1}: "))
            v = int(input(f"Podaj wartość przedmiotu {i+1}: "))
            if w <= 0 or v <= 0:
                raise ValueError("Waga i wartość muszą być liczbami naturalnymi.")
            items.append((w, v))
            
        return items, capacity
    except Exception as e:
        print(f"Podano nieprawidłowy format danych: {e}")
        return None, None


def load_data_from_file(filename=DEFAULT_INPUT_FILE_NAME):
    """
    Format pliku:
    pierwszy wiersz: liczba przedmiotów, pojemność plecaka
    kolejne wiersze: rozmiar przedmiotu, wartość przedmiotu
    """
    try:
        with open(filename, "r") as f:
            n = int(f.readline())
            if n <= 0:
                raise ValueError("Liczba przedmiotów musi być liczbą naturalną.")
            
            capacity = int(f.readline())
            if capacity <= 0:
                raise ValueError("Pojemność musi być liczbą naturalną.")
            
            items = []
            for i in range(n):
                line = f.readline()
                if not line:
                    raise ValueError("Brak danych dla wszystkich przedmiotów.")
                w, v = map(int, line.strip().split())
                if w <= 0 or v <= 0:
                    raise ValueError("Waga i wartość muszą być liczbami naturalnymi.")
                items.append((w, v))
            return items, capacity
        
    except Exception as e:
        print(f"Podano nieprawidłowy format danych: {e}")
        return None, None