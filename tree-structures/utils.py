import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def load_seq_from_file(filepath: str) -> list[int]:
    with open(filepath, 'r') as file:
        return list(map(int, file.read().split()))
    
def measure_execution_time(func, *args):
    start = time.time()
    result = func(*args)
    return (time.time() - start) * 1000, result