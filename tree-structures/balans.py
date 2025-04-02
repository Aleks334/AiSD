tabwejscie = [10, 5, 15, 3, 7, 12, 18]
class Node:
    def __init__(self, data):
      self.data=data
      self.left=None
      self.right=None
      self.height=1
class Drzewo:
  def __init__(self):
    self.root=None
  def wysokosc(self, node):
      return node.height if node else 0
  def balans(self, node):
      return self.wysokosc(node.left)-self.wysokosc(node.right) if node else 0
  def prawo(self, node):
      x = node.left
      t = x.right
      x.right = node
      node.left = t
      node.height = 1 + max(self.wysokosc(node.left), self.wysokosc(node.right))
      x.height = 1 + max(self.wysokosc(x.left), self.wysokosc(x.right))
      return x
  def lewo(self, node):
      x = node.right
      t = x.left
      x.left = node
      node.right = t
      node.height = 1 + max(self.wysokosc(node.left), self.wysokosc(node.right))
      x.height = 1 + max(self.wysokosc(x.left), self.wysokosc(x.right))
      return x      
  def insert(self, node, data):
    if not node:
      return Node(data)

    if data < node.data:
      node.left = self.insert(node.left, data)
    else:
      node.right = self.insert(node.right, data)
    node.height = 1 + max(self.wysokosc(node.left), self.wysokosc(node.right))
    balans1 = self.balans(node)
    if balans1 > 1:
      if data < node.left.data:
        return self.prawo(node)
      else:
        node.left = self.lewo(node.left)
        return self.prawo(node)
    if balans1 < -1:
      if data > node.right.data:
        return self.lewo(node)
      else:
        node.right = self.prawo(node.right)
        return self.lewo(node)
    return node
  def add(self, data):
    self.root = self.insert(self.root, data)
drzewo = Drzewo()
x = 0
while x<len(tabwejscie):
  drzewo.add(tabwejscie[x])
  x=x+1
