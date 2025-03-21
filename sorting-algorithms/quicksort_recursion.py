import data_generator as gen
import sys

sys.setrecursionlimit(10_000)

tab = []
print("Ile liczb chcesz wprowadzić: ")
x = int(input())

def podzial(tab, p, r):
    pivot = tab[r]
    i = p
    j = r
    while True:
        while i <= r and tab[i] > pivot:
            i = i + 1
        while j >= p and tab[j] < pivot:
            j = j - 1
        if i <= j:
            tmp1 = tab[i]
            tmp2 = tab[j]
            tab[i] = tmp2
            tab[j] = tmp1
            j = j - 1
            i = i + 1
        else:
            return j
        
def sortowanie(tab, p, r):
    if p<r:
        q = podzial(tab, p, r)
        sortowanie(tab, p, q )
        sortowanie(tab, q+1, r)

def quickSortRekurencyjny(arr):
    p = 0
    r = len(arr) - 1

    sortowanie(arr, p, r)

if x < 0:
    x = 0
elif x>10:
    x = 10
if x == 0:
    gen.smallTest("quick sort rekurencyjny", quickSortRekurencyjny)
else:
    #tu normalny kod do wprowadzania
    while x>0:
        a = int(input())
        tab.append(a)
        x=x-1
p = 0
r = len(tab)-1

sortowanie(tab, p, r)

print(tab)
