from bst import Drzewo as BST
from avl import Drzewo as AVL, budowanie
from heap import MinHeap

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