import random
from utils import calc_algorithm_exec_time, export_results, get_adjacency_matrix, plot_3d_results, prepare_plot_data
from graph_matrix import get_graph_matrix
from euler_cycle_directed_multigraph import fleury_algorithm as fleury_directed
from euler_cycle_undirected_graph import fleury_algorithm as fleury_undirected
from ahg import hamilton as hamilton_directed
from ahs import hamilton as hamilton_undirected

def generate_vertices_counts(min_n_vertices: int = 10, k: int = 25, count: int = 10) -> list[int]:
    min_n = min_n_vertices
    step = (k - min_n) // (count - 1)
    return [min_n + i * step for i in range(count)]

def generate_undirected_graph(n, saturation_percent):
    max_edges = n * (n - 1) // 2
    target_edges = (max_edges * saturation_percent) // 100
    edge_set = set()

    while len(edge_set) < target_edges:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v:
            edge = tuple(sorted((u, v)))
            edge_set.add(edge)

    edge_list = list(edge_set)
    return n, edge_list

def generate_directed_multigraph(n, saturation_percent):
    max_arcs = n * n # without self-loops it would be n*(n-1)
    target_arcs = (max_arcs * saturation_percent) // 100

    edge_list = []
    while len(edge_list) < target_arcs:
        u = random.randint(1, n)
        v = random.randint(1, n)
        edge_list.append((u, v))

    return n, edge_list

def run_tests():
    print("Starting performance tests...")
    
    saturations = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    vertices_counts = generate_vertices_counts()
    
    undirected_euler_results = {n: {} for n in vertices_counts}
    directed_euler_results = {n: {} for n in vertices_counts}
    undirected_hamilton_results = {n: {} for n in vertices_counts}
    directed_hamilton_results = {n: {} for n in vertices_counts}
    
    print("\nTesting undirected graphs...")
    for n in vertices_counts:
        for saturation in saturations:
            num_v, edges = generate_undirected_graph(n, saturation)
            adj_matrix = get_adjacency_matrix(edges, num_v)
            
            start_vertex = random.randint(0, num_v - 1)
            euler_avg, euler_std = calc_algorithm_exec_time(
                fleury_undirected, 
                [adj_matrix, num_v, start_vertex], 
            )
            undirected_euler_results[n][saturation] = (len(edges), euler_avg, euler_std)
            

            hamilton_avg, hamilton_std = calc_algorithm_exec_time(
                hamilton_undirected, 
                [adj_matrix], 
            )
            undirected_hamilton_results[n][saturation] = (len(edges), hamilton_avg, hamilton_std)
            
            print(f"Undirected - Vertices: {n}, Saturation: {saturation}%, Edges: {len(edges)}")
            print(f"Euler avg time: {euler_avg:.3f} ms (±{euler_std:.3f})")
            print(f"Hamilton avg time: {hamilton_avg:.3f} ms (±{hamilton_std:.3f})")

    

    print("\nTesting directed multigraphs...")
    for n in vertices_counts:
        for saturation in saturations:
            num_v, edges = generate_directed_multigraph(n, saturation)
            graph_matrix = get_graph_matrix(edges, num_v)
            
            start_vertex = random.randint(0, num_v - 1)
            euler_avg, euler_std = calc_algorithm_exec_time(
                fleury_directed, 
                [graph_matrix, num_v, start_vertex], 
            )
            directed_euler_results[n][saturation] = (len(edges), euler_avg, euler_std)
            
            hamilton_avg, hamilton_std = calc_algorithm_exec_time(
                hamilton_directed, 
                [graph_matrix], 
            )
            directed_hamilton_results[n][saturation] = (len(edges), hamilton_avg, hamilton_std)
            
            print(f"Directed - Vertices: {n}, Saturation: {saturation}%, Edges: {len(edges)}")
            print(f"Euler avg time: {euler_avg:.3f} ms (±{euler_std:.3f})")
            print(f"Hamilton avg time: {hamilton_avg:.3f} ms (±{hamilton_std:.3f})")
    
    
    export_results(undirected_euler_results, "undirected_euler_tests")
    export_results(directed_euler_results, "directed_euler_tests")
    export_results(undirected_hamilton_results, "undirected_hamilton_tests")
    export_results(directed_hamilton_results, "directed_hamilton_tests")

    plot_3d_results(
        prepare_plot_data(undirected_hamilton_results), 
        'Hamilton cycle (undirected graph): t=f(n,s)',
        'hamilton_undirected_3d'
    )
    
    plot_3d_results(
        prepare_plot_data(undirected_euler_results),
        'Euler cycle (undirected graph): t=f(n,s)',
        'fleury_undirected_3d'
    )

    plot_3d_results(
        prepare_plot_data(directed_hamilton_results), 
        'Hamilton cycle (directed multigraph): t=f(n,s)',
        'hamilton_directed_3d'
    )
    
    plot_3d_results(
        prepare_plot_data(directed_euler_results),
        'Euler cycle (directed multigraph): t=f(n,s)',
        'fleury_directed_3d'
    )
    
    print("\nTests completed. Results exported to CSV files.")

if __name__ == "__main__":
    run_tests()