from bst import Drzewo as BST
from avl import Drzewo as AVL, budowanie
from heap import MinHeap, kopcowanie, array_to_heap

def create_bst(sequence):
    bst = BST()
    for item in sequence:
        bst.insert(item)
    return bst

def create_avl(sequence):
    avl = AVL()
    sorted_seq = sorted(sequence)
    avl.root = budowanie(sorted_seq)
    return avl

def create_heap(sequence):
    return MinHeap.list_to_tree(sequence)