def create_cycles_list(edges: list[tuple[int, int]], num_vertices: int) -> dict[int, list[int]]:
    cycles = {v: [] for v in range(1, num_vertices + 1)}
    
    edge_set = set(edges)
    for u, v in edges:
        # self-loops
        if u == v and v not in cycles[u]:
            cycles[u].append(v)
        # two-vertex cycles
        elif (v, u) in edge_set and v not in cycles[u]:
            cycles[u].append(v)
            cycles[v].append(u)
    
    return cycles

def create_successor_list(edges: list[tuple[int, int]], cycles: dict[int, list[int]],  num_vertices: int) -> dict[int, list[int]]:
    successors = {v: [] for v in range(1, num_vertices + 1)}
    
    for u, v in edges:
        if v not in cycles[u]:
            successors[u].append(v)
    
    return successors

def create_predecessor_list(edges: list[tuple[int, int]], cycles: dict[int, list[int]], num_vertices: int) -> dict[int, list[int]]:
    predecessors = {v: [] for v in range(1, num_vertices + 1)}
    
    for u, v in edges:
        if u not in cycles[v]: 
            predecessors[v].append(u)
    
    return predecessors


def create_no_incidences_list(edges: list[tuple[int, int]], cycles: dict[int, list[int]], num_vertices: int) -> dict[int, list[int]]:
    no_incidences = {v: [i for i in range(1, num_vertices + 1) if i not in cycles[v]] 
                    for v in range(1, num_vertices + 1)}
    
    for u, v in edges:
        if v in no_incidences[u] and v not in cycles[u]:
            no_incidences[u].remove(v)
        if u in no_incidences[v] and u not in cycles[v]:
            no_incidences[v].remove(u)
    
    return no_incidences

def get_graph_matrix(edges: list[tuple[int, int]], num_vertices: int) -> list[list[int]]:
    """ Creates a graph matrix for directed multigraph. """
    # Init with -1
    matrix = [[-1] * (num_vertices + 4) for _ in range(num_vertices)]
    
    cycles = create_cycles_list(edges, num_vertices)
    successors = create_successor_list(edges,cycles, num_vertices)
    predecessors = create_predecessor_list(edges,cycles, num_vertices)
    no_incidences = create_no_incidences_list(edges,cycles, num_vertices)
    
    # step 1.
    for i in range(num_vertices):
        vertex_i = i + 1
        k = 0
        matrix[i][num_vertices] = successors[vertex_i][0] if successors[vertex_i] else 0
        for j in range(num_vertices):
            vertex_j = j + 1 

            if vertex_j in successors[vertex_i]:
                k += 1
                matrix[i][j] = successors[vertex_i][k] if k < len(successors[vertex_i]) else successors[vertex_i][-1]              
            
    # step 2.
    for i in range(num_vertices):
        vertex_i = i + 1
        k = 0
        matrix[i][num_vertices + 1] = predecessors[vertex_i][0] if predecessors[vertex_i] else 0
        for j in range(num_vertices):
            vertex_j = j + 1

            if vertex_j in predecessors[vertex_i]:
                k += 1
                matrix[i][j] = (predecessors[vertex_i][k] if k < len(predecessors[vertex_i]) else predecessors[vertex_i][-1]) + num_vertices

    # step 3.
    for i in range(num_vertices):
        vertex_i = i + 1
        k = 0
        matrix[i][num_vertices + 2] = no_incidences[vertex_i][0] if no_incidences[vertex_i] else 0
        for j in range(num_vertices):
            vertex_j = j + 1

            if vertex_j in no_incidences[vertex_i]:
                k += 1
                matrix[i][j] = (no_incidences[vertex_i][k] if k < len(no_incidences[vertex_i]) else no_incidences[vertex_i][-1]) * -1

    # step 4.
    for i in range(num_vertices):
        vertex_i = i + 1
        k = 0
        matrix[i][num_vertices + 3] = cycles[vertex_i][0] if cycles[vertex_i] else 0
        for j in range(num_vertices):
            vertex_j = j + 1
            i_to_j = vertex_j in cycles[vertex_i]
            j_to_i = vertex_i in cycles[vertex_j]

            if i_to_j and j_to_i:
                k += 1
                matrix[i][j] = (cycles[vertex_i][k] if k < len(cycles[vertex_i]) else cycles[vertex_i][-1]) + 2 * num_vertices
           
    return matrix

#print(get_graph_matrix1([(1,2),(3,1),(4,3),(5,1),(2,4),(3,2),(5,4),(2,5)], 5))