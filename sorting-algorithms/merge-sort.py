import sys, time

# input
arrStr = input("Podaj n-elementowy ciąg liczb naturalnych (elementy oddzielone spacjami), n<=10\n")
unsortedList = list(map(int, arrStr.split()))

if len(unsortedList) > 10:
    print("Ciąg powinien mieć n<=10 elementów!")
    sys.exit(1)

if len(unsortedList) == 0:
    print("Ciąg ma zero elementów!")
    sys.exit(1)


def mergeSort(list, numOfMerges):
    if len(list) == 1:
        return list
    
    mid = len(list) // 2
 
    left = list[:mid]
    right = list[mid:]

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
sortedList = mergeSort(unsortedList, mergeCount)
endTime = time.time()

executionTime = (endTime - startTime) * 1000

# output
print(f"Execution Time: {executionTime:.3f} ms")
print(f"Ciąg wejściowy: {unsortedList}", end="\n")
print(f"Ciąg wyjściowy: {sortedList}", end="\n")
print(f"Liczba scaleń: {mergeCount[0]}", end="\n")
