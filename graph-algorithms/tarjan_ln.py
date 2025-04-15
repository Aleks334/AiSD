# W = WHITE - 0
# G = GREY - 1 
# B = BLACK - 2
lista = [
    [1],  # Wierzchołek 0 ma krawędź do 1
    [2],  # Wierzchołek 1 ma krawędź do 2
    []    # Wierzchołek 2 nie ma sąsiadów
]
kolor = []
lista_L = []
kolor = [0] * len(lista)
v = 0 #to jest wierzchołek który teraz będzie sprawdzany 
# zmienianie kolorów
def biali_sasiedzi(v):
  global lista_L
  i = 0 
  kolor[v] = 1
  while i < len(lista[v]):
    somsiad = lista[v][i]
    if kolor[somsiad] == 0:
        biali_sasiedzi(somsiad)
    elif kolor[somsiad] == 1:
        print("Graf nie jest acykliczny")
        exit()
    i = i + 1
  kolor[v] = 2
  lista_L = [v] + lista_L
koncowy = v
while any(k==0 for k in kolor):
  if kolor[v] == 0:
      biali_sasiedzi(v)
  v = v + 1
  if v == len(lista):
      v = 0
print(lista_L)
