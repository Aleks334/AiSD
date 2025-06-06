from euler_cycle_directed_multigraph import fleury_algorithm as fleury_directed, has_eulerian_cycle as has_eulerian_directed, is_strongly_connected
from euler_cycle_undirected_graph import fleury_algorithm as fleury_undirected, has_eulerian_cycle as has_eulerian_undirected
from ahg import hamilton as hamilton_directed
from ahs import hamilton as hamilton_undirected
from utils import read_graph_from_file, get_adjacency_matrix
from graph_matrix import get_graph_matrix

def read_input():
    print("Enter number of vertices and edges in 1. row, then list of edges:")
    num_vertices, num_edges = map(int, input().split())
    edges = []

    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u,v))

    return num_vertices, num_edges, edges

def menu():
    while True:
        print("\nGraph Algorithm Menu:")
        print("1. Find Euler Cycle")
        print("2. Find Hamilton Cycle")
        print("3. Exit")
        
        choice = input("\nChoose option: ")

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid option. Try again.")
            continue

        print("\nChoose graph representation:")
        print("1. Adjacency Matrix (undirected)")
        print("2. Graph Matrix (directed multigraph)")
        repr_choice = input("Choose option: ")

        if repr_choice not in ["1", "2"]:
            print("Invalid option. Try again.")
            continue

        print("\nChoose data source:")
        print("1. Read from file")
        print("2. Enter manually")
        data_choice = input("Choose option: ")

        if data_choice == "1":
            num_vertices, _, edges = read_graph_from_file()
        elif data_choice == "2":
            num_vertices, _, edges = read_input()
        else:
            print("Invalid option. Try again.")
            continue

        if choice == "1":
            if repr_choice == "1":
                adj_matrix = get_adjacency_matrix(edges, num_vertices)

                if not has_eulerian_undirected(adj_matrix, num_vertices):
                    print("\nGraph does not have an Euler cycle.")
                else:
                    cycle = fleury_undirected(adj_matrix, num_vertices, 0)
                    print("\nFound Euler cycle:")
                    print(" -> ".join(map(str, cycle)))

            else:
                graph_matrix = get_graph_matrix(edges, num_vertices)

                if not has_eulerian_directed(graph_matrix, num_vertices) or not is_strongly_connected(graph_matrix, num_vertices):
                    print("\nGraph does not have an Euler cycle.")
                else:
                    cycle = fleury_directed(graph_matrix, num_vertices, 0)
                    print("\nFound Euler cycle:")
                    print(" -> ".join(map(str, cycle)))

        else:
            if repr_choice == "1":
                adj_matrix = get_adjacency_matrix(edges, num_vertices)
                cycle = hamilton_undirected(adj_matrix)
            else:
                graph_matrix = get_graph_matrix(edges, num_vertices)
                cycle = hamilton_directed(graph_matrix)
            
            if cycle:
                print("\nFound Hamilton cycle:")
                print(" -> ".join(map(str, [x + 1 for x in cycle])))
            else:
                print("\nNo Hamilton cycle exists in this graph.")

if __name__ == "__main__":
    menu()