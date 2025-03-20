import data_generator as gen

def stosowanie(tab, n, pointer):
    son1 = pointer * 2 + 1 
    son2 = pointer * 2 + 2
    sprawdz = pointer
    if son1<n and tab[son1] > tab[sprawdz]:
        sprawdz = son1
    if son2<n and tab[son2] > tab[sprawdz]:
        sprawdz = son2
    if sprawdz != pointer:
        tmp1 = tab[sprawdz]
        tmp2 = tab[pointer]
        tab[pointer] = tmp1
        tab[sprawdz] = tmp2
        stosowanie(tab, n, sprawdz)

def kopcowanie(tab):
    n = len(tab)
    pointer = len(tab) // 2 - 1
    while pointer >= 0:
        stosowanie(tab, n, pointer)
        pointer = pointer - 1
    a = n-1
    while a>0:
        tmp3 = tab[a]
        tmp4 = tab[0]
        tab[a] = tmp4
        tab[0] = tmp3
        stosowanie(tab, a, 0)
        a = a - 1

tab = []
print("Ile liczb chcesz wprowadzić: ")
x = int(input())
if x < 0:
    x = 0
elif x>10:
    x = 10

if x == 0:
    gen.defaultTest("heap sort", kopcowanie, False, 5000, 25_000)
else:
    #tu normalny kod do wprowadzania
    while x>0:
        a = int(input())
        tab.append(a)
        x=x-1
        
kopcowanie(tab)
print(list(reversed(tab)))