import matplotlib.pyplot as plt
import numpy as np
import os
from utils import measure_execution_time
import trees as t
from tree_operations import max_key_bst, max_key_hmin, tree_with_balance
from data_generator import generate_sequences

import sys
sys.setrecursionlimit(100_000)

OUTPUT_PATH = "tree-structures/output"

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

def measure_tree_operations(sequence: list[int]) -> dict[str, tuple[float, float]]:
    results = {}
    
    bst_create_time, bst = measure_execution_time(t.create_bst, sequence)
    bst_max_time, _ = measure_execution_time(max_key_bst, bst.root)
    results["BST"] = (bst_create_time, bst_max_time)
    
    avl_create_time, avl = measure_execution_time(t.create_avl, sequence)
    avl_max_time, _ = measure_execution_time(max_key_bst, avl.root)
    results["AVL"] = (avl_create_time, avl_max_time)
    
    heap_create_time, heap = measure_execution_time(t.create_heap, sequence)
    heap_max_time, _ = measure_execution_time(max_key_hmin, heap.root)
    results["MinHeap"] = (heap_create_time, heap_max_time)
    
    return results

def measure_balance_time(sequence: list[int]) -> float:
    balance_time, _ = measure_execution_time(tree_with_balance, sequence)
    return balance_time

def create_graph(sizes, data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    for label, values in data.items():
        plt.plot(sizes, values, marker='o', label=label)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{OUTPUT_PATH}/{filename}")
    plt.close()

def plot_tree_operation_graphs(sizes, random_results, sorted_results):
    create_graph(
        sizes,
        {tree: [result[0] for result in results] for tree, results in random_results.items()},
        "Czas tworzenia drzewa (ciąg losowy)",
        "Liczba elementów ciągu (n)",
        "Czas (ms)",
        "creation_time_random.png"
    )
    
    create_graph(
        sizes,
        {tree: [result[1] for result in results] for tree, results in random_results.items()},
        "Wyszukiwanie maksimum (ciąg losowy)",
        "Liczba elementów ciągu (n)",
        "Czas (ms)",
        "max_key_time_random.png"
    )

    create_graph(
        sizes,
        {tree: [result[0] for result in results] for tree, results in sorted_results.items()},
        "Czas tworzenia drzewa (ciąg rosnący)",
        "Liczba elementów ciągu (n)",
        "Czas (ms)",
        "creation_time_sorted.png"
    )
    
    create_graph(
        sizes,
        {tree: [result[1] for result in results] for tree, results in sorted_results.items()},
        "Wyszukiwanie maksimum (ciąg rosnący)",
        "Liczba elementów ciągu (n)",
        "Czas (ms)",
        "max_search_time_sorted.png"
    )

def plot_balance_time_graph(sizes, random_balance_times, sorted_balance_times):
    create_graph(
        sizes,
        {"ciąg losowy": random_balance_times, "ciąg rosnący": sorted_balance_times},
        "Czas równoważenia BST",
        "Liczba elementów ciągu (n)",
        "Czas (ms)",
        "balance_time.png"
    )

def generate_graphs(min_n: int = 1000, max_n: int = 50_000, num_points: int = 20):
    sizes = np.linspace(min_n, max_n, num_points, dtype=int)
    tree_types = ["BST", "AVL", "MinHeap"]
    random_results = {t: [] for t in tree_types}
    sorted_results = {t: [] for t in tree_types}
    random_balance_times = []
    sorted_balance_times = []
    
    for n in sizes:
        sequences = generate_sequences(n)
        for seq_type, seq in [("random", sequences["random"][0]), 
                            ("ascending", sequences["ascending"][0])]:
            results = measure_tree_operations(seq)
            target_dict = random_results if seq_type == "random" else sorted_results
            for tree_type in tree_types:
                target_dict[tree_type].append(results[tree_type])
            
            balance_time = measure_balance_time(seq)
            if seq_type == "random":
                random_balance_times.append(balance_time)
            else:
                sorted_balance_times.append(balance_time)
    
    plot_tree_operation_graphs(sizes, random_results, sorted_results)
    plot_balance_time_graph(sizes, random_balance_times, sorted_balance_times)

if __name__ == "__main__":
    generate_graphs()
