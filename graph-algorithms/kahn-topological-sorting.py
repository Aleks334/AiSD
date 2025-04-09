# input
initVerticesNum, initEdgesNum = list(map(int, input().split()))
initGraph = [] # list of edges in graph

for i in range(initEdgesNum):
    v,e = input().split()
    initGraph.append((v,e))

# utility functions
def findIndependentVertex(graph) -> int | tuple[int, int]:
    """ Returns vertex (or 2 vertices if only those left) in graph which has in-degree equal to 0: in-deg(v)=0. """
    vertices  = getAllVertices(graph)

    if len(vertices) == 2:
        return (vertices[0], vertices[1])

    inDegOfVertices = { v: 0 for v in vertices }

    for (_inV, v) in graph:
        inDegOfVertices[v] += 1

    independentV = None
    for (v, inDeg) in inDegOfVertices.items():
        if inDeg == 0:
            independentV = v
            break

    return independentV

def getAllVertices(graph):
    """ Retrieves unique vertices from edges in graph. """
    vertices = []
    for (v1, v2) in graph:
        if not v1 in vertices:
            vertices.append(v1)
        if not v2 in vertices:
            vertices.append(v2)

    return vertices

def removeVertex(graph, vertex):
    """ Removes vertex (only independent) from graph with edge. """

    newGraph = [] 
    for edge in graph:
        if not edge[0] == vertex:
            newGraph.append(edge)

    return newGraph

# Kahn's algorithm - topological sorting
result = []
currGraph = initGraph
while not len(getAllVertices(currGraph)) == 0:
    independentV = findIndependentVertex(currGraph)

    if not independentV:
        print("independent vertex doesn't exist!")

    newGraph = None

    if isinstance(independentV, tuple):
        result.extend(independentV)
        newGraph = removeVertex(currGraph, independentV[0])
    else: 
        result.append(independentV)
        newGraph = removeVertex(currGraph, independentV)
    
    currGraph = newGraph
    
print(f"Graph: {initGraph} \ntopologically sorted using Kahn's algorithm: {result}")