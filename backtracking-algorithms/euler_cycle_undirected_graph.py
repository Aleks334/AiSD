import random
from utils import read_graph_from_file, get_adjacency_matrix

def read_input():
    print("Enter number of vertices and edges in 1. row, then list of edges:")
    num_vertices, num_edges = map(int, input().split())
    edges = []

    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u,v))

    return num_vertices, num_edges, edges


def has_eulerian_cycle(adj_matrix, n):
    for i in range(n):
        degree = sum(adj_matrix[i])
        if degree % 2 != 0:
            return False
    return True


def dfs_reachable_vertices(adj_matrix, u, visited):
    visited[u] = True
    count = 1
    for v in range(len(adj_matrix)):
        if adj_matrix[u][v] > 0 and not visited[v]:
            count += dfs_reachable_vertices(adj_matrix, v, visited)
    return count


def is_next_edge_valid(adj_matrix, u, v):
    if adj_matrix[u][v] == 0:
        return False

    total_edges = sum(adj_matrix[u])
    if total_edges == 1:
        return True 

    visited = [False] * len(adj_matrix)
    v_count1 = dfs_reachable_vertices(adj_matrix, u, visited)

    # Remove edge, check if (u,v) is not a bridge
    adj_matrix[u][v] -= 1
    adj_matrix[v][u] -= 1
    visited = [False] * len(adj_matrix)
    v_count2 = dfs_reachable_vertices(adj_matrix, u, visited)

    # Restore edge
    adj_matrix[u][v] += 1
    adj_matrix[v][u] += 1

    return v_count1 == v_count2


def fleury_algorithm(adj_matrix, n, start_vertex):
    """ start vertex is 0-indexed. """
    path = []

    def visit(u):
        for v in range(n):
            if adj_matrix[u][v] > 0 and is_next_edge_valid(adj_matrix, u, v):
                #print(f"Traversing edge: {u+1} -> {v+1}") 
                adj_matrix[u][v] -= 1
                adj_matrix[v][u] -= 1
                visit(v)
        path.append(u)

    visit(start_vertex)
    return [v + 1 for v in reversed(path)] 


def main():
    print("\nChoose input method:")
    print("1. Keyboard input")
    print("2. File input")
    choice = input("Your choice: ")

    if choice == "1":
            num_vertices, _, edges = read_input()
            adj_matrix = get_adjacency_matrix(edges, num_vertices)
    elif choice == "2":
            num_vertices, _, edges = read_graph_from_file()
            adj_matrix = get_adjacency_matrix(edges, num_vertices)
    else:
            print("Invalid choice")
            return

    # print("\nAdjacency Matrix:")
    # for row in adj_matrix:
    #     print(' '.join(map(str, row)))

    if not has_eulerian_cycle(adj_matrix, num_vertices):
        print("\nGraph does not have an Euler cycle.")
    else:
        print("\nEuler cycle:")
        start_vertex = random.randrange(num_vertices)
        cycle = fleury_algorithm(adj_matrix, num_vertices, start_vertex)
        print(" -> ".join(map(str, cycle)))


if __name__ == "__main__":
    main()