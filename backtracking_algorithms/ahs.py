G = []
with open("graf.txt", "r") as file:
    for line in file:
        G.append(list(map(int, line.strip().split())))
def hamilton(G):
    n = len(G)
    path = [0]
    visited = [False]*n
    visited[0] = True
    def DFS(u):
        if len(path) == n:
            return G[u][0] == 1
        v = 0
        while v<n:
            if G[u][v] != 0 and not visited[v]:
               visited[v] = True
               path.append(v)
               if DFS(v):
                    return True
               path.pop()
               visited[v] = False
            v = v + 1
        return False
    if DFS(0):
        return path + [0]
    else:
        return None
wynik = hamilton(G)
if wynik:
    print("Występuje cykl hamilton:", wynik)
else:
    print("Graf nie ma cykly hamilton")

