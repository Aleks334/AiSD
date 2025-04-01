tabwejscie = [10, 5, 15, 3, 7, 12, 18]
sortowana = sorted(tabwejscie)
class Node:
  def __init__(self, data):
    self.data=data
    self.left=None
    self.right=None
class Drzewo:
  def __init__(self):
    self.root = None
def budowanie(tab):
  if tab:
    mid = len(tab) // 2
    root = Node(tab[mid])
    root.left = budowanie(tab[:mid])
    root.right = budowanie(tab[mid+1:])
    return root
drzewo = Drzewo()
drzewo.root = budowanie(sortowana)
