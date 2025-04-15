import random

def generate_n_values(start=100, k=1500, count=15):
    step = (k - start) // (count - 1)
    return [start + i * step for i in range(count)]

def generate_dag(n, saturation=0.5):
    """Generates a DAG with n nodes and edge saturation.
    Returns: num of vertices, num of edges, edge list in (vertices are from 1)."""
    
    # n(n-1) arcs (edges) in full directed graph divided by 2 to avoid cycles.
    edges_num = n * (n - 1) // 2
    target_edges_num = int(saturation * edges_num)

    possible_edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    selected_edges = random.sample(possible_edges, target_edges_num)

    edges_list = [(u + 1, v + 1) for u, v in selected_edges]

    return n, edges_list

def main():
    generated_vertices_num = generate_n_values()

    for n in generated_vertices_num:
         n, edges = generate_dag(n)
         print(f"Generated DAG with n={n}, edges={len(edges)}, edges list: {edges}")

if __name__ == "__main__":
    main()