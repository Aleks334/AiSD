import sys, time

arrStr = input("Podaj n-elementowy ciąg liczb naturalnych (elementy oddzielone spacjami), n<=10\n")
unsortedArr = list(map(int, arrStr.split()))

if len(unsortedArr) > 10:
    print("Ciąg powinien mieć n<=10 elementów!")
    sys.exit(1)

if len(unsortedArr) == 0:
    print("Ciąg ma zero elementów!")
    sys.exit(1)


def mergeSort(arr, numOfMerges):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
 
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergeSort(left, numOfMerges), mergeSort(right, numOfMerges), numOfMerges)

def merge(left, right, numOfMerges):
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

    numOfMerges[0] += 1
    return sortedList

mergeCount = [0]

startTime = time.time()
sortedArr = mergeSort(unsortedArr, mergeCount)
endTime = time.time()

executionTime = (endTime - startTime) * 1000

print(f"Execution Time: {executionTime:.3f} ms")
print(f"Ciąg wejściowy: {unsortedArr}", end="\n")
print(f"Ciąg wyjściowy: {sortedArr}", end="\n")
print(f"Liczba scaleń: {mergeCount[0]}", end="\n")
