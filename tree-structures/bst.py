tabwejscie = [10, 5, 15, 3, 7, 12, 18]
class Node:
    def __init__(self, data):
      self.data=data
      self.left=None
      self.right=None
class Drzewo:
  def __init__(self):
    self.root=None
  def insert(self, data):
    if self.root is None:
      self.root=Node(data)
      print("Root: " + str(self.root.data))
    else:
      self._insert_costam(data, self.root)
  def _insert_costam(self, data, node):
    if data<node.data:
      if node.left is None:
        node.left=Node(data)
        print("Od " + str(node.data) + " lewy: " + str(node.left.data))
      else:
        self._insert_costam(data, node.left)
    else:
      if node.right is None:
        node.right=Node(data)
        print("Od " + str(node.data) + " prawy: " + str(node.right.data))
      else:
        self._insert_costam(data, node.right)
drzewo = Drzewo()
x = 0
while x<len(tabwejscie):
  drzewo.insert(tabwejscie[x])
  x=x+1
