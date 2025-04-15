from data_generator import generate_n_values, generate_dag
from utils import measure_execution_time, export_to_csv
from graph_representations import get_successor_list, get_adjacency_matrix
from kahn_topological_sorting import KahnSuccessorList, KahnAdjacencyMatrix
from tarjan_ln import TarjanSuccessorList
from tarjan_matrix import TarjanAdjacencyMatrix

def test_kahn_successor_list(vertices_nums, saturation=0.5):
    execution_times = []
    edge_counts = []
    
    for n in vertices_nums:
        num_vertices, edges = generate_dag(n, saturation)
        successor_list = get_successor_list(edges, num_vertices)
        
        kahn = KahnSuccessorList(successor_list)
        time, _ = measure_execution_time(kahn.sort)
        
        execution_times.append(time)
        edge_counts.append(len(edges))
        
        print(f"Successor List - Vertices: {n}, Edges: {len(edges)}, Time: {time:.6f} ms")
    
    return execution_times, edge_counts

def test_kahn_adjacency_matrix(vertices_nums, saturation=0.5):
    execution_times = []
    edge_counts = []
    
    for n in vertices_nums:
        num_vertices, edges = generate_dag(n, saturation)
        adj_matrix = get_adjacency_matrix(edges, num_vertices)
        
        kahn = KahnAdjacencyMatrix(adj_matrix)
        time, _ = measure_execution_time(kahn.sort)
        
        execution_times.append(time)
        edge_counts.append(len(edges))
        
        print(f"Adjacency Matrix - Vertices: {n}, Edges: {len(edges)}, Time: {time:.6f} ms")
    
    return execution_times, edge_counts

def test_tarjan_successor_list(vertices_nums, saturation=0.5):
    execution_times = []
    edge_counts = []
    
    for n in vertices_nums:
        num_vertices, edges = generate_dag(n, saturation)
        successor_list = get_successor_list(edges, num_vertices)
        
        tarjan = TarjanSuccessorList(successor_list)
        time, _ = measure_execution_time(tarjan.sort)
        
        execution_times.append(time)
        edge_counts.append(len(edges))
        
        print(f"Tarjan successor list - Vertices: {n}, Edges: {len(edges)}, Time: {time:.6f} ms")
    
    return execution_times, edge_counts

def test_tarjan_adjacency_matrix(vertices_nums, saturation=0.5):
    execution_times = []
    edge_counts = []
    
    for n in vertices_nums:
        num_vertices, edges = generate_dag(n, saturation)
        adjacency_matrix = get_adjacency_matrix(edges, num_vertices)
        
        tarjan = TarjanAdjacencyMatrix(adjacency_matrix)
        time, _ = measure_execution_time(tarjan.sort)
        
        execution_times.append(time)
        edge_counts.append(len(edges))
        
        print(f"Tarjan adjency matrix - Vertices: {n}, Edges: {len(edges)}, Time: {time:.6f} ms")
    
    return execution_times, edge_counts

def run_performance_tests():
    print("Starting performance tests...")
    
    vertices_nums = generate_n_values(start=10, k=100, count=10)
    saturation = 0.5
    
    print("\nTesting Kahn's algorithm with Successor List...")
    sl_times, sl_edges = test_kahn_successor_list(vertices_nums, saturation)
    export_to_csv("kahn_successor_list", vertices_nums, sl_times, sl_edges)
    
    print("\nTesting Kahn's algorithm with Adjacency Matrix...")
    am_times, am_edges = test_kahn_adjacency_matrix(vertices_nums, saturation)
    export_to_csv("kahn_adjacency_matrix", vertices_nums, am_times, am_edges)
    
    print("\nTesting Tarjan's algorithm with Successor List...")
    tl_times, tl_edges = test_tarjan_successor_list(vertices_nums, saturation)
    export_to_csv("tarjan_successor_list", vertices_nums, tl_times, tl_edges)
    
    print("\nTesting Tarjan's algorithm with Adjacency Matrix...")
    tm_times, tm_edges = test_tarjan_adjacency_matrix(vertices_nums, saturation)
    export_to_csv("tarjan_adjacency_matrix", vertices_nums, tm_times, tm_edges)

    print("\nTests completed. Results exported to CSV files")

if __name__ == "__main__":
    run_performance_tests()