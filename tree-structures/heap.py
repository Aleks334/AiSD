from utils import Node

def stosowanie(tab, n, pointer):
    son1 = pointer * 2 + 1 
    son2 = pointer * 2 + 2
    sprawdz = pointer
    if son1 < n and tab[son1] > tab[sprawdz]:
        sprawdz = son1
    if son2 < n and tab[son2] > tab[sprawdz]:
        sprawdz = son2
    if sprawdz != pointer:
        tmp1 = tab[sprawdz]
        tmp2 = tab[pointer]
        tab[pointer] = tmp1
        tab[sprawdz] = tmp2
        stosowanie(tab, n, sprawdz)

def kopcowanie(tab):
    n = len(tab)
    pointer = len(tab) // 2 - 1
    while pointer >= 0:
        stosowanie(tab, n, pointer)
        pointer = pointer - 1
    a = n-1
    while a>0:
        tmp3 = tab[a]
        tmp4 = tab[0]
        tab[a] = tmp4
        tab[0] = tmp3
        stosowanie(tab, a, 0)
        a = a - 1

class MinHeap:
    def __init__(self):
        self.root = None

    @staticmethod
    def list_to_tree(array):
        heap = MinHeap()
        if array:
            array_copy = array.copy()
            kopcowanie(array_copy)
            heap.root = array_to_heap(array_copy)
        return heap

def array_to_heap(tab):
    def create_nodes(tab, pointer):
        if pointer >= len(tab):
            return None
        
        node = Node(tab[pointer])
        node.left = create_nodes(tab, 2 * pointer + 1)
        node.right = create_nodes(tab, 2 * pointer + 2)
        return node

    if not tab:
        return None
    return create_nodes(tab, 0)
