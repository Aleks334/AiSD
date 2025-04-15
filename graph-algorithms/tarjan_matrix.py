class TarjanAdjacencyMatrix:
    def __init__(self, adjacency_matrix: list[list[int]]):
        self.graph = adjacency_matrix
        self.colors = [0] * len(adjacency_matrix)  # White=0, Gray=1, Black=2
        self.result = []

    def find_in_deg_0(self) -> int | None:
        n = len(self.graph)
        in_deg = [0] * n
        
        for i in range(n):
            for j in range(n):
                if self.graph[i][j] == 1:
                    in_deg[j] += 1

        for i in range(n):
            if in_deg[i] == 0:
                return i + 1
        return None

    def dfs(self, v: int) -> bool:
        self.colors[v] = 1  # Grey
        
        for i in range(len(self.graph[v])):
            if self.graph[v][i] == 1:
                if self.colors[i] == 0:  # White
                  if not self.dfs(i):
                      return False
                elif self.colors[i] == 1:  # Grey
                    print(f"Cycle detected!")
                    return False 
                    
        self.colors[v] = 2  # Black
        self.result = [v + 1] + self.result
        return True
    
    def sort(self, start_vertex: int = None) -> list[int] | None:
        if start_vertex is None:
            start_vertex = self.find_in_deg_0()
                  
        if start_vertex is not None:
            v = start_vertex - 1 
            if v < 0 or v >= len(self.graph):
                print(f"Vertex {start_vertex} not found in graph!")
                return None
            if self.colors[v] == 0:
                if not self.dfs(v):
                    return None

        for v in range(len(self.graph)):
            if self.colors[v] == 0:
                if not self.dfs(v):
                    return None
            
        return self.result
