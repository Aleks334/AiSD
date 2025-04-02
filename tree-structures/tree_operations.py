from collections import deque

class Node: 
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node | None = None
        self.right: Node | None = None

def min_key(root: Node | list[int]) -> tuple[int, list[int]]:
    """
        Computes min key in BST, AVL or Hmin tree.\n
        **Input:** root node or list of keys (Hmin). **Output:** min key, path to that key.
    """
    min = 0
    path: list[int]= [] 
    currNode: Node = root

    # min heap is stored in a list
    if isinstance(root, list):
         return (root[0], root[0])

    while currNode:
        path.append(currNode.key)
        min = currNode.key
        currNode = currNode.left
    
    return (min, path)

def max_key_bst(root: Node) -> tuple[int, list[int]]:
    """
        Computes max key in BST, AVL. \n
        **Input:** root node or list of keys (Hmin). **Output:** max key, path to that key.
    """
    path: list[int]= [] 
    max = 0
    currNode: Node = root

    while currNode:
        path.append(currNode.key)
        max = currNode.key
        currNode = currNode.right
    
    return (max, path)

def max_key_hmin(root: Node) -> tuple[int, list[int]]:
    """
        Calculates max key in min heap that is presented as complete binary tree structure.\n
        **Input:** root node of Hmin. **Output:** max key, path to it
    """ 
    max = root.key
    path = []
    queue = deque([(root, [])]) # queue element as (curr node, path to it)

    while queue:
        node, path = queue.pop()
        path.append(node.key)

        if node.key > max:
            max, path = node.key, path.copy()

        if node.left:
            queue.appendleft((node.left, path.copy()))
        if node.right:
            queue.appendleft((node.right, path.copy()))
    
    return (max, path)

def lvl_order_iteration(root: Node, searchedKey: int) -> tuple[int, list[int]]:
    """
        Computes lvl of searched key for BST, AVL or Hmin tree and all keys on that level.\n
        If desired key is not found then returns (-1, []).  \n
        **Input:** root node, desired key. **Output:** lvl of that key, keys on that lvl.
    """
    if not root:
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

def reverse_in_order(root: Node):
    """
        Prints all keys of BST, AVL tree in descending order using in-order traversing method (reversed).\n
        **Input:** root node of the tree. **Output:** None.
    """
    if not root:
        return

    reverse_in_order(root.right)
    print(root.key)
    reverse_in_order(root.left)

# TODO: function for printing descending keys of min heap

def get_node_bst(root: Node, key: int) -> Node | None:
    """
        Attempts to find a node for given key in the BST (AVL) tree.\n
        **Input:** root of the tree, searched key. **Output:** node for key in tree or None if it doesn't exist
    """
    if not root:
        return None
    
    if root.key == key:
        return root
    
    if key < root.key:
        return get_node_bst(root.left, key)
    else:
        return get_node_bst(root.right, key)
    
def get_node_hmin(root: Node, key: int) -> Node | None:
     """
        Attempts to find a node for given key in min heap (binary tree) using iterative BFS.\n
        **Input:** root of the tree, searched key. **Output:** node for key in tree or None if it doesn't exist
     """
     if not root:
         return None
     
     queue = deque([root])
     while queue:
         node = queue.pop()
         if node.key == key:
             return node
         
         if node.left:
             queue.appendleft(node.left)
         if node.right:
             queue.appendleft(node.right)
    
     return None

def pre_order(root: Node):
    if not root:
        return

    print(root.key)
    pre_order(root.left)
    pre_order(root.right)
    return

def bin_tree_height(root: Node) -> int:
    """
        Computes height of binary tree (BST, AVL, Hmin).\n
        **Input:** root node. **Output:** height of tree or -1 if given root doesn't exist.
    """
    if not root:
        return -1
    
    leftH = bin_tree_height(root.left)
    rightH = bin_tree_height(root.right)

    return max(leftH, rightH) + 1

def remove_post_order(root: Node):
    if not root:
        return None
    
    root.left = remove_post_order(root.left)
    root.right = remove_post_order(root.right)

    del root
    return None

def task_4(root: Node, subTreeRootKey: int):
    subTreeRoot: Node | None = None
    subTreeRoot = get_node_bst(root, subTreeRootKey)
    pre_order(subTreeRoot)
    h = bin_tree_height(subTreeRoot)
    print(f"height: {h}")
    remove_post_order(subTreeRoot)