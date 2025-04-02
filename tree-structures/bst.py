from utils import Node

tabwejscie = [10, 5, 15, 3, 7, 12, 18]

class Drzewo:
  def __init__(self):
    self.root=None
  def insert(self, key):
    if self.root is None:
      self.root=Node(key)
     # print("Root: " + str(self.root.key))
    else:
      self._insert_costam(key, self.root)
  def _insert_costam(self, key, node):
    if key<node.key:
      if node.left is None:
        node.left=Node(key)
     #   print("Od " + str(node.key) + " lewy: " + str(node.left.key))
      else:
        self._insert_costam(key, node.left)
    else:
      if node.right is None:
        node.right=Node(key)
      #  print("Od " + str(node.key) + " prawy: " + str(node.right.key))
      else:
        self._insert_costam(key, node.right)
drzewo = Drzewo()
x = 0
while x<len(tabwejscie):
  drzewo.insert(tabwejscie[x])
  x=x+1
