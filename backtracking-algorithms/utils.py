import csv
import os
import time

import numpy as np
import matplotlib.pyplot as plt

def read_graph_from_file(filename="file.txt"):
    edges = []
    num_vertices = 0
    num_edges = 0
    
    with open(f"backtracking-algorithms/{filename}", 'r') as file:
        first_line = file.readline().strip().split()
        num_vertices = int(first_line[0])  
        num_edges = int(first_line[1])
        
        for line in file:
            edge = list(map(int, line.strip().split()))
            if len(edge) == 2:
                edges.append(tuple(edge))
    
    return num_vertices, num_edges, edges

def get_adjacency_matrix(edges, num_vertices):
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    for (u, v) in edges:
        u -= 1
        v -= 1
        matrix[u][v] = 1
        matrix[v][u] = 1

    return matrix

def measure_execution_time(func, *args) -> float:
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return round((end_time - start_time) * 1000, 3)

def export_results(results: dict, filename: str):
    OUTPUT_DIR = "backtracking-algorithms/output"
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    filepath = f"{OUTPUT_DIR}/{filename}.csv"
    
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Vertices', 'Saturation', 'Edges', 'Avg Time (ms)', 'Std Deviation (ms)'])
         
        for n in results:
            for saturation in results[n]:
                edges, avg_time, std_dev = results[n][saturation]
                writer.writerow([n, saturation, edges, f"{avg_time:.3f}", f"{std_dev:.3f}"])

def plot_3d_results(results: dict, title: str, filename: str):
    OUTPUT_DIR = "backtracking-algorithms/output"

    vertices = sorted(list(results.keys()))
    saturations = sorted(list(results[vertices[0]].keys()))
    
    X, Y = np.meshgrid(vertices, saturations)
    
    Z = np.zeros((len(saturations), len(vertices)))
    for i, s in enumerate(saturations):
        for j, v in enumerate(vertices):
            Z[i][j] = results[v][s][1]  # [1] because results store (edges, time)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(X, Y, Z, cmap='viridis')
    
    ax.set_xlabel('Number of vertices (n)')
    ax.set_ylabel('Saturation (%)')
    ax.set_zlabel('Execution time (ms)')
    ax.set_title(title)
    plt.colorbar(surf)
    
    plt.savefig(f'{OUTPUT_DIR}/{filename}.png')
    plt.close()

def calc_algorithm_exec_time(func, args, num_runs=10) -> tuple[list[float], list[float]]:
    times = []
    for _ in range(num_runs):
        time = measure_execution_time(func, *args)
        times.append(time)
    return np.mean(times), np.std(times)

def prepare_plot_data(results: dict) -> dict:
    """
    Transforms results dictionary to format required by plot_3d_results.
    Excludes standard deviation.
    """
    plot_data = {}
    for n in results:
        plot_data[n] = {}
        for s in results[n]:
            edges, avg_time, _ = results[n][s]
            plot_data[n][s] = (edges, avg_time)
    return plot_data