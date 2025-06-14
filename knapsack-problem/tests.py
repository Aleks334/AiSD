import random
import statistics
from brute_force import knapsack_brute_force
from dynamic import knapsack_dynamic
from greedy import knapsack_greedy
from utils import run_with_timer

def generate_test_case(n: int, max_size: int, max_value: int, capacity: int) -> tuple[list[tuple[int, int]], int]:
    items = []
    for _ in range(n):
        size = random.randint(1, max_size)
        value = random.randint(1, max_value)
        items.append((size, value))
    return items, capacity

def generate_test_cases(tests_num: int = 1,
                       constant_param: str = None, constant_value: int = None) -> list[tuple[int, int, int, int]]:
    """
    Generates test cases with optional constant parameter.
    
    Args:
        tests_num: number of test sets to generate
        constant_param: Which parameter to keep constant ('n', 'weight', 'value', 'capacity', None)
        constant_value: Value for the constant parameter
    
    Returns:
        List of tuples (n, max_weight, max_value, capacity)
    """
    WEIGHT_MULTIPLIER = 2  
    VALUE_MULTIPLIER = 2   
    CAPACITY_MULTIPLIER = 3  

    test_cases = []
    for i in range(1, tests_num + 1):
        n = constant_value if constant_param == 'n' else i
        max_weight = constant_value if constant_param == 'weight' else i * WEIGHT_MULTIPLIER
        max_value = constant_value if constant_param == 'value' else i * VALUE_MULTIPLIER
        capacity = constant_value if constant_param == 'capacity' else i * CAPACITY_MULTIPLIER
        
        items, cap = generate_test_case(n, max_weight, max_value, capacity)
        test_cases.append((len(items), max_weight, max_value, cap))
    
    return test_cases

def run_algorithm_test(algo_func, items: list[tuple[int, int]], capacity: int, 
                      num_measurements: int = 10) -> tuple[list[int], int, int, float, float]:
    """
    Run algorithm multiple times and calculate average execution time and standard deviation.
    """

    times = []
    result = None
    
    for _ in range(num_measurements):
        result, execution_time = run_with_timer(algo_func, items, capacity)
        times.append(execution_time)
    
    selected, total_weight, total_value = result
    avg_time = statistics.mean(times)
    std_dev = statistics.stdev(times) if len(times) > 1 else 0
    
    return selected, total_weight, total_value, avg_time, std_dev

def run_all_tests():
    test_cases = generate_test_cases(tests_num=15)
    non_optimal_count = 0
    total_cases = len(test_cases)

    for n, max_weight, max_value, capacity in test_cases:
        print(f"\n=== Test dla {n} przedmiotów ===")
        items, cap = generate_test_case(n, max_weight, max_value, capacity)
        
        print(f"Pojemność plecaka: {cap}")
        print(f"Przedmioty (waga, wartość):")
        for i, (s, v) in enumerate(items, 1):
            print(f"Przedmiot {i}: ({s}, {v})")

        # brute force 
        selected, weight, bf_value, bf_time, bf_std = run_algorithm_test(knapsack_brute_force, items, cap)
        print("\nSiłowy (brutalny):")
        print(f"Wybrane przedmioty: {selected}")
        print(f"Całkowity waga: {weight}")
        print(f"Całkowita wartość: {bf_value}")
        print(f"Średni czas wykonania: {bf_time:.4f} ± {bf_std:.4f} ms")
        
        # optimal solution
        _, _, optimal_value, dp_time, dp_std = run_algorithm_test(knapsack_dynamic, items, cap)
        print("\nDynamiczny (optymalny):")
        print(f"Całkowita wartość: {optimal_value}")
        print(f"Średni czas wykonania: {dp_time:.4f} ± {dp_std:.4f} ms")
        
        # suboptimal solution
        selected, weight, greedy_value, greedy_time, greedy_std = run_algorithm_test(knapsack_greedy, items, cap)
        print("\nZachłanny:")
        print(f"Wybrane przedmioty: {selected}")
        print(f"Całkowity waga: {weight}")
        print(f"Całkowita wartość: {greedy_value}")
        print(f"Średni czas wykonania: {greedy_time:.4f} ± {greedy_std:.4f} ms")
        
        if greedy_value < optimal_value:
            non_optimal_count += 1
            print("\nTo rozwiązanie zachłanne nie jest optymalne!")
            print(f"Różnica wartości: {optimal_value - greedy_value}")
    
    non_optimal_percentage = (non_optimal_count / total_cases) * 100
    print("\n=== Statystyki ===")
    print(f"Liczba wszystkich instancji: {total_cases}")
    print(f"Liczba nieooptymalnych rozwiązań: {non_optimal_count}")
    print(f"Procent nieooptymalnych rozwiązań: {non_optimal_percentage:.2f}%")


if __name__ == "__main__":
    run_all_tests()