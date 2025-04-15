from data_generator import generate_n_values, generate_dag
from utils import measure_execution_time, export_to_csv
from graph_representations import get_successor_list, get_adjacency_matrix
from kahn_topological_sorting import KahnSuccessorList, KahnAdjacencyMatrix
from tarjan_ln import TarjanSuccessorList
from tarjan_matrix import TarjanAdjacencyMatrix

def test_algorithm(vertices_nums, algorithm_class, representation_type, name):
    execution_times = []
    edge_counts = []
    
    for n in vertices_nums:
        num_vertices, edges = generate_dag(n)
        
        if representation_type == "successor_list":
            graph_repr = get_successor_list(edges, num_vertices)
        elif representation_type == "adjacency_matrix":
            graph_repr = get_adjacency_matrix(edges, num_vertices)
        
        algorithm = algorithm_class(graph_repr)
        time, _ = measure_execution_time(algorithm.sort)
        
        execution_times.append(time)
        edge_counts.append(len(edges))
        
        print(f"{name} - Vertices: {n}, Edges: {len(edges)}, Time: {time:.6f} ms")
    
    return execution_times, edge_counts

def run_performance_tests():
    print("Starting performance tests...")
    
    vertices_nums = generate_n_values()
    
    test_cases = [
        (KahnSuccessorList, "successor_list", "kahn_successor_list", "Kahn Successor List"),
        (KahnAdjacencyMatrix, "adjacency_matrix", "kahn_adjacency_matrix", "Kahn Adjacency Matrix"),
        (TarjanSuccessorList, "successor_list", "tarjan_successor_list", "Tarjan Successor List"),
        (TarjanAdjacencyMatrix, "adjacency_matrix", "tarjan_adjacency_matrix", "Tarjan Adjacency Matrix")
    ]
    
    for algorithm_class, repr_type, file_name, display_name in test_cases:
        print(f"\nTesting {display_name}...")
        times, edges = test_algorithm(vertices_nums, algorithm_class, repr_type, display_name)
        export_to_csv(file_name, vertices_nums, times, edges)

    print("\nTests completed. Results exported to CSV files")

if __name__ == "__main__":
    run_performance_tests()
