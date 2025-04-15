import time
import csv
import os

def read_graph_from_file(filename="file.txt"):
    edges = []
    num_vertices = 0
    num_edges = 0
    
    with open(f"graph-algorithms/{filename}", 'r') as file:
        first_line = file.readline().strip().split()
        num_vertices = int(first_line[0])  
        num_edges = int(first_line[1])
        
        for line in file:
            edge = list(map(int, line.strip().split()))
            if len(edge) == 2:
                edges.append(tuple(edge))
    
    return num_vertices, num_edges, edges

def measure_execution_time(func, *args):
    start = time.time()
    result = func(*args)
    return (time.time() - start) * 1000, result

def export_to_csv(algorithm_name, vertices_nums, times, edge_counts):
    OUTPUT_DIR = "graph-algorithms/output"
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    filepath = f"{OUTPUT_DIR}/{algorithm_name}_performance.csv"
    
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Vertices', 'Edges', 'Time (ms)'])
        for n, edges, time in zip(vertices_nums, edge_counts, times):
            writer.writerow([n, edges, f"{time:.6f}"])

if __name__ == "__main__":
    num_vertices, num_edges, edges = read_graph_from_file()

    print(f"Vertices number: {num_vertices}")
    print(f"Edges number: {num_edges}")
    print(f"Edges list (directed graph): {edges}")