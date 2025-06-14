import time


DEFAULT_INPUT_FILE_NAME = "dane.txt"

def load_data_from_keyboard():
    try:
        first_line = input("Podaj liczbę przedmiotów oraz pojemność plecaka (oddzielone spacją): ")
        n_str, capacity_str = first_line.strip().split()
        n = int(n_str)
        
        capacity = int(capacity_str)
        if n <= 0:
            raise ValueError("Liczba przedmiotów musi być liczbą naturalną większą od 0.")
        if capacity <= 0:
            raise ValueError("Pojemność musi być liczbą naturalną większą od 0.")
        
        items = []
        for i in range(n):
            line = input(f"Podaj rozmiar i wartość przedmiotu {i+1} (oddzielone spacją): ")
            weight, value = map(int, line.strip().split())
            if weight <= 0 or value <= 0:
                raise ValueError("Rozmiar i wartość muszą być liczbami naturalnymi większymi od 0.")
            items.append((weight, value))
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
            first_line = f.readline()
            n_str, capacity_str = first_line.strip().split()
            n = int(n_str)
            capacity = int(capacity_str)
            if n <= 0:
                raise ValueError("Liczba przedmiotów musi być liczbą naturalną większą od 0.")
            if capacity <= 0:
                raise ValueError("Pojemność musi być liczbą naturalną większą od 0.")

            items = []
            for _ in range(n):
                line = f.readline()
                if not line:
                    raise ValueError("Brak danych dla wszystkich przedmiotów.")
                weight, value = map(int, line.strip().split())
                if weight <= 0 or value <= 0:
                    raise ValueError("Rozmiar i wartość muszą być liczbami naturalnymi większymi od 0.")
                items.append((weight, value))
            return items, capacity

    except Exception as e:
        print(f"Podano nieprawidłowy format danych: {e}")
        return None, None
    

def run_with_timer(func, *args):
    """
    Measures function execution time in milliseconds.
    """
    start_time = time.perf_counter()
    result = func(*args)
    execution_time = (time.perf_counter() - start_time) * 1000
    return result, execution_time