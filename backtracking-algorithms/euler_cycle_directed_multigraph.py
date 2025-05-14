import random
from utils import read_graph_from_file
from graph_matrix import get_graph_matrix

def read_input():
    print("Enter number of vertices and edges in 1. row, then list of edges:")
    num_vertices, num_edges = map(int, input().split())
    edges = []

    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u,v))

    return num_vertices, num_edges, edges

def has_eulerian_cycle(graph_matrix: list[list[int]], n: int) -> bool:
    for i in range(n):
        out_degree = 0
        in_degree = 0
        
        for j in range(n):
            if graph_matrix[i][j] >= 0 and graph_matrix[i][j] <= n:
                out_degree += 1
            if graph_matrix[i][j] >= n + 1 and graph_matrix[j][i] <= 2*n:
                in_degree += 1
        
        if in_degree != out_degree:
            return False
    return True

def dfs_reachable_vertices(graph_matrix: list[list[int]], start: int, visited: list[bool]) -> int:
    visited[start] = True
    count = 1
    
    for v in range(len(graph_matrix)):
        # Check if there's a successor edge
        if 0 <= graph_matrix[start][v] <= len(graph_matrix) and not visited[v]:
            count += dfs_reachable_vertices(graph_matrix, v, visited)
    return count


def is_strongly_connected(graph_matrix, n: int) -> bool:
    for start in range(n):
        visited = [False] * n
        count = dfs_reachable_vertices(graph_matrix, start, visited)
        if count != n:
            return False
    return True


def fleury_algorithm(graph_matrix: list[list[int]], n: int, start_vertex: int) -> list[int]:
    """
    - if value > 0 and <= n: successor edge
    - if value > n and <= 2n: predecessor edge
    - if value > 2n: both directions exist
    - if value < 0: no edge
    """
    path = []
    matrix_copy = [row[:] for row in graph_matrix]
    
    def visit(u: int):
        for v in range(n):
            if matrix_copy[u][v] >= 0 and matrix_copy[u][v] <= n:
                matrix_copy[u][v] = -1  # Remove edge
                visit(v)
        path.append(u)
    
    visit(start_vertex)
    return [v + 1 for v in reversed(path)]

def main():
    print("\nDirected Multigraph Euler Cycle Finder")
    print("Choose input method:")
    print("1. Keyboard input")
    print("2. File input")
    choice = input("Your choice: ")

    if choice == "1":
        num_vertices, _, edges = read_input()
        graph_matrix = get_graph_matrix(edges, num_vertices)
    elif choice == "2":
        num_vertices, _, edges = read_graph_from_file()
        graph_matrix = get_graph_matrix(edges, num_vertices)
    else:
        print("Invalid choice")
        return

    if not has_eulerian_cycle(graph_matrix, num_vertices) or not is_strongly_connected(graph_matrix, num_vertices):
        print("\nGraph does not have an Euler cycle.")
        return

    # print("\nGraph matrix:")
    # for row in graph_matrix:
    #     print(row)

    print("\nEuler cycle:")
    start_vertex = random.randrange(num_vertices)
    cycle = fleury_algorithm(graph_matrix, num_vertices, start_vertex)
    print(" -> ".join(map(str, cycle)))

if __name__ == "__main__":
    main()