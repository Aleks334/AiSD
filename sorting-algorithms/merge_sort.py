import sys, time
import data_generator as gen

mergeCount = 0 # global

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
 
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    global mergeCount
    sortedList = []
    l,r = 0,0

    while l < len(left) and r < len(right):
        # sort descending
        if left[l] >= right[r]:
            sortedList.append(left[l])
            l += 1
        else:
            sortedList.append(right[r])
            r += 1

    sortedList.extend(left[l:])
    sortedList.extend(right[r:])

    mergeCount += 1
    return sortedList

def main():
    arrStr = input("Podaj n-elementowy ciąg liczb naturalnych (elementy oddzielone spacjami), n<=10\n")
    unsortedArr = list(map(int, arrStr.split()))

    if len(unsortedArr) > 10:
        print("Ciąg powinien mieć n<=10 elementów!")
        sys.exit(1)

    if len(unsortedArr) == 0:
        print("Ciąg ma zero elementów!")
        sys.exit(1)

    startTime = time.time()
    sortedArr = mergeSort(unsortedArr)
    endTime = time.time()

    executionTime = (endTime - startTime) * 1000

    print(f"Czas wykonania: {executionTime:.3f} ms")
    print(f"Ciąg wejściowy: {unsortedArr}")
    print(f"Ciąg wyjściowy: {sortedArr}")
    print(f"Liczba scaleń: {mergeCount}")

def test():
    gen.defaultTest("merge sort", mergeSort, shouldDrawGraph=False, minN=500, maxN=5000)
    print(f"Liczba scaleń: {mergeCount}")

if __name__ == "__main__":
    print("1 - wpisz dane ręcznie, 2 - uruchom test z wygenerowanymi danymi")
    code = int(input())

    if code == 1:
        main()
    elif code == 2:
        test()
    else:
        print("Podano nieprawidłową liczbę.")
