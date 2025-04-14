def get_successor_list(edges, verticesNum):
    successorList = { v: [] for v in range(1, verticesNum + 1) }

    for vertex in range(1, verticesNum + 1):
        successorListForVertex = []
        for (v1, v2) in edges:
            if v1 == vertex:
                successorListForVertex.append(v2)
        successorList[vertex].extend(sorted(successorListForVertex))

    return successorList