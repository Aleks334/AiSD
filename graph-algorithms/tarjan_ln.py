class TarjanSuccessorList:
    def __init__(self, successor_list: dict[int, list[int]]):
        self.graph = successor_list
        self.colors = {v: 0 for v in successor_list.keys()}  # White=0, Gray=1, Black=2
        self.result = []


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
            
    def sort(self) -> list[int] | None:
        for v in self.graph.keys():
            if self.colors[v] == 0:
                if not self.dfs(v):
                    return None
                        
        return self.result