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
n = 0
while n <= len(waga):
    i = 0
    tmp = []
    while i <= pojemnosc:
        tmp.append(0)
        i = i + 1
    tab.append(tmp)
    n = n + 1
i = 1
while i <= len(waga):
    j = 0
    while j <= pojemnosc:
        tab[i][j] = tab[i-1][j]
        if waga[i-1] <= j:
            tab[i][j] = max(
                tab[i][j],
                tab[i-1][j - waga[i-1]] + wartosc[i-1]
            )
        j = j + 1
    i = i + 1
i = len(waga)
j = pojemnosc
while i > 0 and j > 0:
    if tab[i][j] != tab[i-1][j]:
        przedmioty.append(i-1)
        j -= waga[i-1]
    i -= 1
przedmioty.reverse()
print("Wybrane przedmioty:", przedmioty)
i = 0
wartosctab = []
wagatab = []
sumawaga = 0
sumawartosc = 0
while i<len(przedmioty):
    wartosctab.append(wartosc[przedmioty[i]])
    wagatab.append(waga[przedmioty[i]])
    sumawartosc = sumawartosc + wartosc[przedmioty[i]]
    sumawaga = sumawaga + waga[przedmioty[i]]
    i = i + 1
print("Wartość: ", wartosctab)
print("Waga: ", wagatab)
print("Suma wartość", sumawartosc)
print("Suma wagi: ", sumawaga)
print()