from bst import Drzewo as BST
from avl import Drzewo as AVL, budowanie
from heap import kopcowanie, array_to_heap

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
    sequence_copy = sequence.copy()
    kopcowanie(sequence_copy)
    min_heap = array_to_heap(sequence_copy)
    return min_heap