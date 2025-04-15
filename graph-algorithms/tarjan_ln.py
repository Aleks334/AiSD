# W = WHITE - 0
# G = GREY - 1 
# B = BLACK - 2
lista = []
kolor = []
lista_L = []
v = 0 #to jest wierzchołek który teraz będzie sprawdzany 
# zmienianie kolorów
def biali_sasiedzi(v):
  global lista_L
  i = 0 
  kolor[v] = 1
  while i < len(lista[v]):
    if kolor[lista[v][i]] == 0:
      kolor[lista[v][i]] = 1 
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
  
