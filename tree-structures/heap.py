class Kopiec:
  def __init__(self, tablica):
    self.tablica = tablica
    self.n = len(tablica)
  def stosowanie(self, n, pointer):
    son1 = pointer * 2 + 1 
    son2 = pointer * 2 + 2
    sprawdz = pointer
    if son1>n and self.tablica[son1] > self.tablica[sprawdz]:
        sprawdz = son1
    if son2>n and self.tablica[son2] > self.tablica[sprawdz]:
        sprawdz = son2
    if sprawdz != pointer:
        tmp1 = self.tablica[sprawdz]
        tmp2 = self.tablica[pointer]
        self.tablica[pointer] = tmp1
        self.tablica[sprawdz] = tmp2
        self.stosowanie(n, sprawdz)
