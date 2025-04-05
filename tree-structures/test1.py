import time
import random
import matplotlib.pyplot as plt
from balans import Drzewo  # Drzewo AVL, BST będzie zaimplementowane w tym samym module
from data_generator import generate_sequences
from utils import measure_execution_time
import trees as t  # Jeżeli masz inne drzewo BST/MinHeap

# Funkcja do mierzenia czasu
def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return (end_time - start_time) * 1000, result  # Zwraca czas w milisekundach

# Funkcja do testowania wszystkich operacji na różnych drzewach
def test_all_operations(sequence):
    # Pomiar czasu dla BST
    bst_time, bst = measure_execution_time(t.create_bst, sequence)
    
    # Pomiar czasu dla AVL
    avl_time, avl = measure_execution_time(t.create_avl, sequence)
    
    # Pomiar czasu dla Min-Heap
    heap_time, heap = measure_execution_time(t.create_heap, sequence)

    print(f"Results for sequence: {sequence}")
    print(f"BST creation time: {bst_time:.6f} ms")
    print(f"AVL creation time: {avl_time:.6f} ms")
    print(f"Min-Heap creation time: {heap_time:.6f} ms")
    
    # Pomiar czasu dla wyszukiwania minimum i maximum w każdym drzewie
    bst_min_time, bst_min = measure_execution_time(t.min_key_bst, bst.root)
    bst_max_time, bst_max = measure_execution_time(t.max_key_bst, bst.root)
    
    avl_min_time, avl_min = measure_execution_time(t.min_key_bst, avl.root)  # AVL traktujemy jak BST pod względem minimalnego
    avl_max_time, avl_max = measure_execution_time(t.max_key_bst, avl.root)
    
    heap_min_time, heap_min = measure_execution_time(t.min_key_hmin, heap.root)
    heap_max_time, heap_max = measure_execution_time(t.max_key_hmin, heap.root)
    
    print(f"BST min key: {bst_min}, max key: {bst_max} (search times: min={bst_min_time:.6f} ms, max={bst_max_time:.6f} ms)")
    print(f"AVL min key: {avl_min}, max key: {avl_max} (search times: min={avl_min_time:.6f} ms, max={avl_max_time:.6f} ms)")
    print(f"Min-Heap min key: {heap_min}, max key: {heap_max} (search times: min={heap_min_time:.6f} ms, max={heap_max_time:.6f} ms)")
    
    return bst_time, avl_time, heap_time

# Funkcja do generowania wykresów
def plot_execution_times(times, label):
    sizes = [size for size in range(1000, 10001, 1000)]
    plt.plot(sizes, times['BST'], label=f"BST {label}")
    plt.plot(sizes, times['AVL'], label=f"AVL {label}")
    plt.plot(sizes, times['Heap'], label=f"Min-Heap {label}")
    plt.xlabel("Number of Elements")
    plt.ylabel("Execution Time (ms)")
    plt.legend()
    plt.title("Tree Construction and Min/Max Search Times")
    plt.show()

# Funkcja główna do testów
def run_tests():
    # Zbierz dane
    times_creation = {'BST': [], 'AVL': [], 'Heap': []}
    times_search = {'BST': [], 'AVL': [], 'Heap': []}

    # Testowanie na różnych długościach sekwencji
    for size in range(1000, 10001, 1000):
        print(f"\nRunning tests for sequence size {size}")
        
        # Generowanie sekwencji losowych
        sequence = generate_sequences(size)["random"][0]
        
        # Testowanie wszystkich drzew
        bst_time, avl_time, heap_time = test_all_operations(sequence)
        
        # Zbieranie czasów
        times_creation['BST'].append(bst_time)
        times_creation['AVL'].append(avl_time)
        times_creation['Heap'].append(heap_time)
        
    # Tworzymy wykresy dla wyników
    plot_execution_times(times_creation, "Creation Time")
    
if __name__ == "__main__":
    run_tests()
