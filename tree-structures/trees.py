from bst import Drzewo as BST
from avl import Drzewo as AVL, budowanie
from heap import MinHeap

def min_key_bst(node):
    current = node
    while current.left:
        current = current.left
    return current.key

# Funkcja do znalezienia maksymalnego klucza w drzewie BST
def max_key_bst(node):
    current = node
    while current.right:
        current = current.right
    return current.key
def create_bst(sequence):
    bst = BST()
    for item in sequence:
        bst.insert(item)
    return bst

def create_avl(sequence):
    avl = AVL()
    avl.root = budowanie(sequence)
    return avl

def create_heap(sequence):
    return MinHeap.list_to_tree(sequence)
# Funkcja do znalezienia minimalnego klucza w drzewie BST
def min_key_bst(node):
    current = node
    while current.left:
        current = current.left
    return current.key

# Funkcja do znalezienia maksymalnego klucza w drzewie BST
def max_key_bst(node):
    current = node
    while current.right:
        current = current.right
    return current.key

# Funkcja do znalezienia minimalnego klucza w Min-Heap
def min_key_hmin(node):
    if node is None:
        return None
    return node.key

# Funkcja do znalezienia maksymalnego klucza w Min-Heap
def max_key_hmin(node):
    # Min-Heap nie ma bezpośredniej metody na znalezienie maksymalnego elementu,
    # ponieważ zawsze mamy minimalny element na korzeniu. Możemy to zrobić iteracyjnie.
    if node is None:
        return None

    def find_max(node):
        if node is None:
            return float('-inf')
        left_max = find_max(node.left)
        right_max = find_max(node.right)
        return max(node.key, left_max, right_max)

    return find_max(node)
