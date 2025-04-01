from collections import deque

class Node: 
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node | None = None
        self.right: Node | None = None

# example BST tree for tests
bst_root = Node(50)
bst_root.left = Node(30)
bst_root.right = Node(70)
bst_root.left.left = Node(20)
bst_root.left.right = Node(40)
bst_root.right.left = Node(60)
bst_root.right.right = Node(80)
bst_root.right.right.right = Node(90)

# example binary tree for tests
bin_root = Node(4)
bin_root.left = Node(2)
bin_root.right = Node(8)
bin_root.left.left = Node(1)
bin_root.left.right = Node(3)
bin_root.right.left = Node(6)
bin_root.right.right = Node(9)
bin_root.right.left.left = Node(5)
bin_root.right.left.right = Node(7)


def get_min_key(root: Node | list[int]) -> tuple[int, list[int]]:
    """
        Computes min key in BST, AVL or Hmin tree.\n
        **Input:** root node or list of keys (Hmin). **Output:** min key, path to that key.
    """
    min = 0
    visitedNodes: list[int]= [] 
    currNode: Node = root

    # min heap is stored in a list
    if isinstance(root, list):
         return (root[0], root[0])

    while currNode:
        visitedNodes.append(currNode.key)
        min = currNode.key
        currNode = currNode.left
    
    return (min, visitedNodes)

def get_max_key(root: Node | list[int]) -> tuple[int, list[int]]:
    """
        Computes max key in BST, AVL or Hmin tree. \n
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
         return (max, visitedNodes) # BUG: lists leaf nodes not path to max key

    while currNode:
        visitedNodes.append(currNode.key)
        max = currNode.key
        currNode = currNode.right
    
    return (max, visitedNodes)

def lvl_order_iteration(root: Node, searchedKey: int) -> tuple[int, list[int]]:
    """
        Computes lvl of searched key for BST, AVL or Hmin tree and all keys on that level. \n
        If desired key is not found then returns (-1, []).  \n
        **Input:** root node, searched key. **Output:** lvl of that key, keys on that lvl.
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


# ----------------------------------------------------------------------

def getNode(root: Node, key: int) -> Node | None:
    """
        Tries to find node for given key in the BST tree.\n
        **Input:** root of the tree, searched key. **Output:** node for key in tree if exists
    """
    if not root:
        return None
    
    if root.key == key:
        return root
    
    if key < root.key:
        return getNode(root.left, key)
    else:
        return getNode(root.right, key)


def task_4(root: Node, subTreeRootKey: int):

    subTreeRoot: Node | None = None
    subTreeRoot = getNode(root, subTreeRootKey)
    pre_order(subTreeRoot)
    h = bin_tree_height(subTreeRoot)
    print(f"height: {h}")
    remove_post_order(subTreeRoot)

def pre_order(root: Node):
    if not root:
        return

    print(root.key)
    pre_order(root.left)
    pre_order(root.right)
    return

def bin_tree_height(root: Node) -> int:
    """
        Gets height of binary tree.\n
        **Input:** root node. **Output:** height of tree or -1 if given node doesn't exist.
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