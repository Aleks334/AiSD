tabwejscie = [10, 5, 15, 3, 7, 12, 18]
class Node:
    def __init__(self, key):
      self.key=key
      self.left=None
      self.right=None
      self.height=1

class Drzewo:
    def __init__(self):
        self.root = None

    def wysokosc(self, node):
        if not node:
            return 0
        return node.height

    def balans(self, node):
        if not node:
            return 0
        return self.wysokosc(node.left) - self.wysokosc(node.right)

    def prawo(self, node):
        if not node or not node.left:
            return node
            
        x = node.left
        t = x.right
        x.right = node
        node.left = t
        
        node.height = 1 + max(self.wysokosc(node.left), self.wysokosc(node.right))
        x.height = 1 + max(self.wysokosc(x.left), self.wysokosc(x.right))
        
        return x

    def lewo(self, node):
        if not node or not node.right:
            return node
            
        x = node.right
        t = x.left
        x.left = node
        node.right = t
        
        node.height = 1 + max(self.wysokosc(node.left), self.wysokosc(node.right))
        x.height = 1 + max(self.wysokosc(x.left), self.wysokosc(x.right))
        
        return x

    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.wysokosc(node.left), self.wysokosc(node.right))
        balans = self.balans(node)

        if balans > 1 and key < node.left.key:
            return self.prawo(node)

        if balans < -1 and key > node.right.key:
            return self.lewo(node)

        if balans > 1 and key > node.left.key:
            node.left = self.lewo(node.left)
            return self.prawo(node)

        if balans < -1 and key < node.right.key:
            node.right = self.prawo(node.right)
            return self.lewo(node)

        return node

    def add(self, key):
        self.root = self.insert(self.root, key)

drzewo = Drzewo()
x = 0
while x<len(tabwejscie):
  drzewo.add(tabwejscie[x])
  x=x+1
