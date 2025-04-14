def read_graph_from_file(filename):
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


if __name__ == "__main__":
    filename = 'file.txt'
    num_vertices, num_edges, edges = read_graph_from_file(filename)

    print(f"Liczba wierzchołków: {num_vertices}")
    print(f"Liczba krawędzi: {num_edges}")
    print(f"Krawędzie grafu: {edges}")