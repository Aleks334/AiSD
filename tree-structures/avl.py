from utils import Node

tabwejscie = [15, 7, 23, 3, 11, 19, 29, 1, 5, 9, 13, 17, 21, 27, 31]

class Drzewo:
  def __init__(self):
    self.root = None

def budowanie(tab):
  if tab:
    ascTab = sorted(tab)
    mid = len(ascTab) // 2
    root = Node(ascTab[mid])
    root.left = budowanie(ascTab[:mid])
    root.right = budowanie(ascTab[mid+1:])
    return root
  
drzewo = Drzewo()
drzewo.root = budowanie(tabwejscie)
