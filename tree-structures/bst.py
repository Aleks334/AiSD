tabwejscie = [10, 5, 15, 3, 7, 12, 18]
def insert(node,data):
  if node is None:
    return [data, None, None]
  if data < node[0]:
    node[1] = insert(node[1],data)
  else:
    node[2] = insert(node[2],data)
  return node
root = None
for value in tabwejscie:
  root = insert(root, value)
print(root)
    
    
