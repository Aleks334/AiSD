# W = WHITE - 0
# G = GREY - 1 
# B = BLACK - 2
macierz = []
kolor = []
lista_L = []
kolor = [0] * len(macierz)
v = 0 #to jest wierzchołek który teraz będzie sprawdzany 
# zmienianie kolorów
def biali_sasiedzi(v):
  global lista_L
  i = 0 
  kolor[v] = 1
  while i < len(macierz[v]):
    if macierz[v][i] == 1 and kolor[i] == 0:
        kolor[i] = 1
    elif macierz[v][i] == 1 and kolor[i] == 1:
        print("Graf zawiera cykl!")
        exit()
    i = i + 1
  kolor[v] = 2
  lista_L = [v] + lista_L
koncowy = v
while any(k==0 for k in kolor):
  if kolor[v] == 0:
      biali_sasiedzi(v)
  v = v + 1
  if v == len(macierz):
      v = 0
