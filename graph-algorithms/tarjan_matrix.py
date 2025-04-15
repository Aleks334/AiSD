class TarjanAdjacencyMatrix:
    def __init__(self, adjacency_matrix: list[list[int]]):
        self.graph = adjacency_matrix
        self.colors = [0] * len(adjacency_matrix)  # White=0, Gray=1, Black=2
        self.result = []

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
    
    def sort(self) -> list[int] | None:
        for v in range(len(self.graph)):
            if self.colors[v] == 0:
                if not self.dfs(v):
                    return None
            
        return self.result
