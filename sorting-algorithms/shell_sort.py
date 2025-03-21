import sys, time
import data_generator as gen

def hibbardSequence(n):
    gaps = []
    gap = 1

    while gap < n:
        gaps.append(gap)
        gap = 2 * gap + 1 

    return gaps

def shellSort(arr):
    gaps = hibbardSequence(len(arr))    

    for gap in reversed(gaps):
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] < temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        print(f"Wartość przyrostu w iteracji to: {gap}")

def main():
    arrStr = input("Podaj n-elementowy ciąg liczb naturalnych (elementy oddzielone spacjami), n<=10\n")
    array = list(map(int, arrStr.split()))

    if len(array) > 10:
        print("Ciąg powinien mieć n<=10 elementów!")
        sys.exit(1)

    if len(array) == 0:
        print("Ciąg ma zero elementów!")
        sys.exit(1)

    print(f"Ciąg wejściowy: {array}")
    print("------------------------")

    startTime = time.time()
    shellSort(array)
    endTime = time.time()

    executionTime = (endTime - startTime) * 1000

    print("------------------------")
    print(f"Czas wykonania: {executionTime:.3f} ms")
    print(f"Ciąg wyjściowy: {array}")

def test():
    gen.defaultTest("shell stort", shellSort, False, shouldDrawGraph=False, minN=1000, maxN=10_000)

if __name__ == "__main__":
    print("1 - wpisz dane ręcznie, 2 - uruchom test z wygenerowanymi danymi")
    code = int(input())

    if code == 1:
        main()
    elif code == 2:
        test()
    else:
        print("Podano nieprawidłową liczbę.")
