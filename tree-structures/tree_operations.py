def get_min_key(root: Node | list[int]) -> tuple[int, list[int]]:
    min = 0
    visitedNodes: list[int]= [] 
    currNode: Node = root

    # min heap is stored in a list
    if isinstance(root, list):
         return (root[0], root[0])

    while currNode is not None:
        visitedNodes.append(currNode.key)
        if min > currNode.key:
            min = currNode.key

        currNode = currNode.left
    
    return (min, visitedNodes)
    

def get_max_key(root: Node | list[int]) -> tuple[int, list[int]]:
    visitedNodes: list[int]= [] 
    max = 0
    currNode: Node = root
    
    if isinstance(root, list):  # min heap is stored in a list
         n = len(root)
        
         for i in range(n // 2, n): # checks only leaf nodes
             visitedNodes.append(root[i])
             if max < root[i]: 
                 max = root[i]
         return (max, visitedNodes)

    while currNode is not None:
        visitedNodes.append(currNode.key)
        if max < currNode.key: 
            max = currNode.key

        currNode = currNode.right
    
    return (max, visitedNodes)