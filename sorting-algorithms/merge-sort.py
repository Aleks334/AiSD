import sys

# input
arrStr = input("Podaj n-elementowy ciąg liczb naturalnych (elementy oddzielone spacjami), n<=10\n")
unsortedList = list(map(int, arrStr.split()))

if len(unsortedList) > 10:
    print("Ciąg powinien mieć n<=10 elementów!")
    sys.exit(1)

if len(unsortedList) == 0:
    print("Ciąg ma zero elementów!")
    sys.exit(1)


def mergeSort(list):
    if len(list) == 1:
        return list
    
    splitIndex = len(list) // 2
 
    left = list[:splitIndex]
    right = list[splitIndex:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    sortedList = []
    i = j = 0

    while i < len(left) and j < len(right):
        # sort descending
        if left[i] > right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1

    sortedList.extend(left[i:])
    sortedList.extend(right[j:])

    return sortedList

   
sortedList = mergeSort(unsortedList)

# output
print("Ciąg wejściowy: ", unsortedList, end="\n")
print("Ciąg wyjściowy: ", sortedList, end="\n")