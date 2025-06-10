waga = []
wartosc = []
pojemnosc = 5
tab = []
przedmioty = []
iloscprzedmiotow = 0
plik = open('dane.txt', 'r')
wczytywanie = []
linianr = 0
for linia in plik:
    x = linia.split()
    if linianr == 0:
        iloscprzedmiotow = int(x[0])
        pojemnosc = int(x[1])
    else:
        waga.append(int(x[0]))
        wartosc.append(int(x[1]))
    linianr = linianr + 1
plik.close()
print(waga)
print(wartosc)
oplacalnosc = []
i = 0
while i < len(waga):
    op = wartosc[i]/waga[i]
    tmp = []
    tmp.append(op)
    tmp.append(i)
    oplacalnosc.append(tmp)
    i = i + 1
print(oplacalnosc)
print()
oplacalnosc = sorted(oplacalnosc)
i = 0
costam = 0
sumawaga = 0
sumawartosc = 0
wagi = []
wartosci = []

while i < len(oplacalnosc):
    idsprawdzane = oplacalnosc[i][1]
    if costam + waga[idsprawdzane] <= pojemnosc:
        costam = costam + waga[idsprawdzane]
        sumawaga = sumawaga + waga[idsprawdzane]
        sumawartosc = sumawartosc + wartosc[idsprawdzane]
        wagi.append(waga[idsprawdzane])
        wartosci.append(wartosc[idsprawdzane])
    i = i + 1
print("Tablica wag elementów: ",wagi)
print("Tablica wartosci elementów: ",wartosci)
print("Łączna suma waga: ",sumawaga)
print("Łączna suma wartosci: ",sumawartosc)
print()

