import os
import matplotlib.pyplot as plt
import numpy as np
from tests import generate_test_cases, generate_test_case, run_algorithm_test
from brute_force import knapsack_brute_force
from dynamic import knapsack_dynamic
from greedy import knapsack_greedy

# Configuration
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

FIGURE_SIZE = (12, 8)
DPI = 300
ALGORITHMS = [
    ("algorytm siłowy", knapsack_brute_force),
    ("algorytm programowania dynamicznego", knapsack_dynamic),
    ("algorytm zachłanny", knapsack_greedy)
]

TESTS_NUM = 15 # doesn't affect the 3d graph

def save_plot(filename: str, tight: bool = True):
    """Save plot to output directory with high quality settings"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    if tight:
        plt.tight_layout()
    plt.savefig(filepath, dpi=DPI, bbox_inches='tight')
    plt.close()

def plot_time_vs_n(constant_capacity: int = 30):
    """
    Generate logarithmic plot of execution time vs number of items
    for all algorithms with error bars
    """
    test_cases = generate_test_cases(tests_num=TESTS_NUM, 
                                   constant_param='capacity', 
                                   constant_value=constant_capacity)
    
    plt.figure(figsize=FIGURE_SIZE)
    for algo_name, algo_func in ALGORITHMS:
        ns, times, errors = [], [], []
        
        for n, max_w, max_v, cap in test_cases:
            items, _ = generate_test_case(n, max_w, max_v, cap)
            _, _, _, avg_time, std_dev = run_algorithm_test(algo_func, items, cap)
            ns.append(n)
            times.append(avg_time)
            errors.append(std_dev)
        
        plt.errorbar(ns, times, yerr=errors, label=algo_name, 
                    marker='o', capsize=5, markersize=8)
    
    plt.yscale('log')
    plt.xlabel('Liczba przedmiotów (n)')
    plt.ylabel('Średni czas wykonania [ms]')
    plt.title(f'Wykres t=f(n), przy stałej pojemności plecaka b={constant_capacity})')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    save_plot('time_vs_n.png')

def plot_time_vs_capacity(constant_n: int = 10):
    """
    Generate individual plots of execution time vs knapsack capacity
    for each algorithm
    """
    test_cases = generate_test_cases(tests_num=TESTS_NUM, 
                                   constant_param='n', 
                                   constant_value=constant_n)
    
    for algo_name, algo_func in ALGORITHMS:
        plt.figure(figsize=FIGURE_SIZE)
        capacities, times, errors = [], [], []
        
        for n, max_w, max_v, cap in test_cases:
            items, _ = generate_test_case(n, max_w, max_v, cap)
            _, _, _, avg_time, std_dev = run_algorithm_test(algo_func, items, cap)
            capacities.append(cap)
            times.append(avg_time)
            errors.append(std_dev)
        
        plt.errorbar(capacities, times, yerr=errors, 
                    marker='o', capsize=5, markersize=8, 
                    color='blue', ecolor='gray')
        plt.xlabel('Pojemność plecaka (b)')
        plt.ylabel('Średni czas wykonania [ms]')
        plt.title(f'Wykres t=f(b) dla: {algo_name}, przy stałej liczbie przedmiotów n={constant_n}')
        plt.grid(True, alpha=0.2)
        save_plot(f'time_vs_capacity_{algo_name.lower().replace(" ", "_")}.png')

def plot_3d_time():
    """
    Generate 3D surface plots showing execution time as a function
    of both number of items and knapsack capacity
    """
    n_range = np.arange(5, 25, 5)
    b_range = np.arange(10, 60, 10)
    X, Y = np.meshgrid(b_range, n_range)
    
    for algo_name, algo_func in ALGORITHMS:
        times = np.zeros((len(n_range), len(b_range)))
        errors = np.zeros((len(n_range), len(b_range)))
        
        for i, n in enumerate(n_range):
            for j, b in enumerate(b_range):
                items, _ = generate_test_case(n, b*2, b*2, b)
                _, _, _, avg_time, std_dev = run_algorithm_test(algo_func, items, b)
                times[i,j] = avg_time
                errors[i,j] = std_dev
        
        fig = plt.figure(figsize=FIGURE_SIZE)
        ax = fig.add_subplot(111, projection='3d')
        
        surf = ax.plot_surface(X, Y, times, cmap='viridis', 
                             antialiased=True, alpha=0.8)
        
        for i in range(len(n_range)):
            for j in range(len(b_range)):
                ax.plot([X[i,j], X[i,j]], [Y[i,j], Y[i,j]], 
                       [times[i,j]-errors[i,j], times[i,j]+errors[i,j]], 
                       color='red', alpha=0.3)
        
        ax.set_xlabel('Pojemność plecaka (b)')
        ax.set_ylabel('Liczba przedmiotów (n)')
        ax.set_zlabel('Średni czas wykonania [ms]')
        ax.set_title(f'Wykres t=f(n,b) dla: \n{algo_name}')
        
        fig.colorbar(surf, label='Czas [ms]')
        save_plot(f'time_3d_{algo_name.lower().replace(" ", "_")}.png', tight=False)

def generate_all_plots():
    print(f"Generating plots...")
    
    print("1. Generating time vs n plot...")
    plot_time_vs_n()
    
    print("2. Generating time vs capacity plots...")
    plot_time_vs_capacity()
    
    print("3. Generating 3D plots...")
    plot_3d_time()
    
    print("All plots have been generated successfully!")

if __name__ == "__main__":
    generate_all_plots()