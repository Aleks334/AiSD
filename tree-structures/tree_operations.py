from collections import deque

class Node: 
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node | None = None
        self.right: Node | None = None

# example bin tree for tests
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)
root.right.right.right = Node(90)

def get_min_key(root: Node | list[int]) -> tuple[int, list[int]]:
    """Returns min key for BST, AVL or Hmin tree. Input: root node or list of keys (Hmin). Output: (min key, path to that key)"""
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
    """
        Returns max key for BST, AVL or Hmin tree. \n
        **Input:** root node or list of keys (Hmin). **Output:** max key, path to that key.
    """
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

def lvl_order_iteration(root: Node, searchedKey: int) -> tuple[int, list[int]]:
    """
        Returns lvl of searched key for BST, AVL or Hmin tree and all keys on that level. \n
        If desired key is not found then returns (-1, []).  \n
        **Input:** root node, searched key. **Output:** lvl of that key, keys on that lvl.
    """
    if root is None:
        return (-1, [])

    queue = deque[Node]()
    queue.appendleft(root)
    currLvl = 0
    searchedKeyLvl = -1
    currLvlNodes: list[int] = []

    while queue:
        currLvlNodes.clear()
        lvlLen = len(queue)
        
        for _ in range(0, lvlLen):
            node = queue.pop()
            currLvlNodes.append(node.key)

            if node.key == searchedKey:
                searchedKeyLvl = currLvl

            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        
        if searchedKeyLvl != -1:
            return (searchedKeyLvl, currLvlNodes)
        currLvl += 1

    return (-1, [])
