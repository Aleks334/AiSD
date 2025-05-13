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