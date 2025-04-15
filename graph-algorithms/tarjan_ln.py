class TarjanSuccessorList:
    def __init__(self, successor_list: dict[int, list[int]]):
        self.graph = successor_list
        self.colors = {v: 0 for v in successor_list.keys()}  # White=0, Gray=1, Black=2
        self.result = []

    def find_in_deg_0(self) -> int | None:
        in_deg = {v: 0 for v in self.graph.keys()}
        
        for vertex in self.graph:
            for successor in self.graph[vertex]:
                in_deg[successor] += 1

        for v, deg in in_deg.items():
            if deg == 0:
                return v
        return None

    def dfs(self, v: int) -> bool:
        self.colors[v] = 1  # Grey
        
        for neighbor in self.graph[v]:
            if self.colors[neighbor] == 0:  # White
                if not self.dfs(neighbor):
                    return False
            elif self.colors[neighbor] == 1:  # Grey
                print("Cycle detected!")
                return False
                
        self.colors[v] = 2  # Black
        self.result = [v] + self.result
        return True
            
    def sort(self, start_vertex: int = None) -> list[int] | None:
        if start_vertex is None:
                    start_vertex = self.find_in_deg_0()
                    
        if start_vertex is not None:
            if start_vertex not in self.graph:
                print(f"Vertex {start_vertex} not found in graph!")
                return None
            if self.colors[start_vertex] == 0:
                if not self.dfs(start_vertex):
                    return None
                        
        for v in self.graph.keys():
            if self.colors[v] == 0:
                if not self.dfs(v):
                    return None
                        
        return self.result