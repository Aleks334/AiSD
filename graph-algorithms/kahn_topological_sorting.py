class KahnEdgesList:
    def __init__(self, edges):
        self.graph = edges

    def get_all_vertices(self, graph) -> list[int]:
        """ Retrieves unique vertices from edges in graph. """
        if not graph:
            return []
        
        vertices = set()
        for v1, v2 in graph:
            vertices.add(v1)
            vertices.add(v2)
        return sorted(vertices)
    
    def find_independent_vertex(self, graph) -> int | tuple[int, int] | None:
        """ Returns vertex (or 2 vertices if only those left) in graph which has in-degree equal to 0: in-deg(v)=0. """
        vertices  = self.get_all_vertices(graph)

        if len(vertices) == 2:
            return (vertices[0], vertices[1])

        in_deg = { v: 0 for v in vertices }

        for _, v in graph:
            in_deg[v] += 1

        independentV = None
        for (v, in_deg_val) in in_deg.items():
            if in_deg_val == 0:
                independentV = v
                break

        return independentV
    
    def remove_vertex(self, graph, vertex):
        """ Returns edges which predecessor is not vertex it is looking for """
        return [edge for edge in graph if edge[0] != vertex]
    
    def sort(self):
        """ Kahn's algorithm - topological sorting """
        result = []
        curr_graph = self.graph.copy()

        while self.get_all_vertices(curr_graph):
            independentV = self.find_independent_vertex(curr_graph)

            if not independentV:
                print("Can't find next independent vertex which means that graph has a cycle. Sorting topologically is impossible.")
                return []

            if isinstance(independentV, tuple):
                result.extend(independentV)
                curr_graph = self.remove_vertex(curr_graph, independentV[0])
            else: 
                result.append(independentV)
                curr_graph = self.remove_vertex(curr_graph, independentV)
                        
        return result

class KahnSuccessorList:
    def __init__(self, successors_dict):
        self.graph = successors_dict

    def get_all_vertices(self, graph) -> list[int]:
        """ Retrieves unique vertices from successors list in graph. """
        if not graph:
            return []
        
        return list(graph.keys())
    
    def find_independent_vertex(self, graph) -> int | None:
        """ Returns vertex in graph which has in-degree equal to 0: in-deg(v)=0. """
        vertices  = self.get_all_vertices(graph)
        in_deg = { v: 0 for v in vertices }

        for vertex in vertices:
            for _, successors in graph.items():
                if vertex in successors:
                    in_deg[vertex] += 1

        independentV = None
        for (v, in_deg_val) in in_deg.items():
            if in_deg_val == 0:
                independentV = v
                break

        return independentV
    
    def remove_vertex(self, graph, vertex):
        """ Returns successors for all vertices except for vertex from argument.  """
        altered_graph = graph.copy()
        altered_graph.pop(vertex)
        return altered_graph
    
    def sort(self):
        """ Kahn's algorithm - topological sorting """
        result = []
        curr_graph = self.graph.copy()

        while self.get_all_vertices(curr_graph):
            independentV = self.find_independent_vertex(curr_graph)

            if not independentV:
                print("Can't find next independent vertex which means that graph has a cycle. Sorting topologically is impossible.")
                return []

            result.append(independentV)
            curr_graph = self.remove_vertex(curr_graph, independentV)
                        
        return result

class KahnAdjacencyMatrix:
    def __init__(self, adjacency_matrix):
        self.graph = adjacency_matrix
        self.removed_vertices = set()

    def get_all_vertices(self, graph) -> list[int]:
        """ Retrieves unique vertices from adjacency matrix. """
        if not graph:
            return []
        
        vertices = []
        for i, _ in enumerate(graph):
            if (i + 1) not in self.removed_vertices:
                vertices.append(i + 1)
                
        return vertices
    
    def find_independent_vertex(self, graph) -> int | None:
        """ Returns vertex in graph which has in-deg(v) = 0. """
        vertices  = self.get_all_vertices(graph)
        in_deg = { v: 0 for v in vertices }

        for vertex in vertices:
            for vertices_row in graph:
                if vertices_row[vertex - 1] == 1:
                    in_deg[vertex] += 1      

        independentV = None
        for (v, in_deg_val) in in_deg.items():
            if in_deg_val == 0:
                independentV = v
                break

        return independentV
    
    def remove_vertex(self, graph, vertex):
        """ Removes all edges related to the vertex. """
        self.removed_vertices.add(vertex)
        altered_graph = [row[:] for row in graph]

        altered_graph[vertex - 1] = [None] * len(altered_graph)   
        for row in altered_graph:
            row[vertex - 1] = None

        return altered_graph
    
    def sort(self):
        """ Kahn's algorithm - topological sorting """
        result = []
        curr_graph = [row[:] for row in self.graph]

        while self.get_all_vertices(curr_graph):
            independentV = self.find_independent_vertex(curr_graph)

            if not independentV:
                print("Can't find next independent vertex which means that graph has a cycle. Sorting topologically is impossible.")
                return []

            result.append(independentV)
            curr_graph = self.remove_vertex(curr_graph, independentV)

        return result

if __name__ == "__main__":
    # input
    initVerticesNum, initEdgesNum = list(map(int, input().split()))
    edgesList = []

    for i in range(initEdgesNum):
        v,e = map(int, input().split())
        edgesList.append((v,e))

    kahn = KahnEdgesList(edgesList)
    sorted_graph = kahn.sort()

    if sorted_graph:
        print(f"Graph: {edgesList} \ntopologically sorted using Kahn's algorithm: {sorted_graph}")