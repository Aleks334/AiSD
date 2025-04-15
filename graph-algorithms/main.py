from kahn_topological_sorting import KahnSuccessorList, KahnAdjacencyMatrix
from data_generator import generate_dag
from utils import read_graph_from_file
from graph_representations import get_successor_list, get_adjacency_matrix
from tarjan_ln import TarjanSuccessorList
from tarjan_matrix import TarjanAdjacencyMatrix

def menu():
    while True:
        print("\nMenu:")
        print("1. Run Kahn's algorithm with Successor List")
        print("2. Run Kahn's algorithm with Adjacency Matrix")
        print("3. Run Tarjan's algorithm with Successor List")
        print("4. Run Tarjan's algorithm with Adjacency Matrix")
        print("5. Exit")

        choice = input("\nChoose option: ")

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid option. Try again.")
            continue

        print("\nChoose data source:")
        print("1. Read from file")
        print("2. Generate random DAG")
        data_choice = input("Choose option: ")

        if data_choice == "1":
            num_vertices, _, edges = read_graph_from_file()
        elif data_choice == "2":
            n = int(input("Enter number of vertices: "))
            num_vertices, edges = generate_dag(n)
        else:
            print("Invalid option. Try again.")
            continue

        if choice == "1":
            successor_list = get_successor_list(edges, num_vertices)
            kahn = KahnSuccessorList(successor_list)
            result = kahn.sort()
            
            if result: 
                print("\nResults for Successor List representation:")
                print(f"Successor list: {successor_list}")
                print(f"Topological order: {result}")

        elif choice == "2":
            adj_matrix = get_adjacency_matrix(edges, num_vertices)
            kahn = KahnAdjacencyMatrix(adj_matrix)
            result = kahn.sort()
            
            if result: 
                print("\nResults for Adjacency Matrix representation:")
                print("Adjacency matrix:")
                for row in adj_matrix:
                    print(row)
                print(f"Topological order: {result}")
        elif choice == "3":
            successor_list = get_successor_list(edges, num_vertices)
            tarjan = TarjanSuccessorList(successor_list)
            result = tarjan.sort()
            
            if result:
                print("\nResults for Tarjan Successor List:")
                print(f"Successor list: {successor_list}")
                print(f"Topological order: {result}")
        elif choice == "4":
            adj_matrix = get_adjacency_matrix(edges, num_vertices)
            tarjan = TarjanAdjacencyMatrix(adj_matrix)
            result = tarjan.sort()
            
            if result:
                print("\nResults for Tarjan Adjacency Matrix:")
                print("Adjacency matrix:")
                for row in adj_matrix:
                    print(row)
                print(f"Topological order: {result}")

if __name__ == "__main__":
    menu()