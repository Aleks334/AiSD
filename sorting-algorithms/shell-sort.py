import sys, time

arrStr = input("Podaj n-elementowy ciąg liczb naturalnych (elementy oddzielone spacjami), n<=10\n")
array = list(map(int, arrStr.split()))

if len(array) > 10:
    print("Ciąg powinien mieć n<=10 elementów!")
    sys.exit(1)

if len(array) == 0:
    print("Ciąg ma zero elementów!")
    sys.exit(1)

def shellSort(arr):
    # Hibbard's sequence
    gap = 1
    while gap < len(arr):
        gap = 2 * gap + 1 

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] < temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

print(f"Ciąg wejściowy: {array}", end="\n")

startTime = time.time()
shellSort(array)
endTime = time.time()

executionTime = (endTime - startTime) * 1000

print(f"Execution Time: {executionTime:.3f} ms")
print(f"Ciąg wyjściowy: {array}", end="\n")
