import time

def load_numbers_from_file(filename: str) -> list[int]:
    with open(filename, 'r') as file:
        return list(map(int, file.read().split()))
    

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} ms")
    return result