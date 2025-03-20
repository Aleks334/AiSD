from heapsort import kopcowanie as heapSort
from merge_sort import mergeSort
from shell_sort import shellSort
from quicksort_iteration import quickSortIteracyjny
from quicksort_recursion import quickSortRekurencyjny

import data_generator as gen

algorithms = {
    "heap sort": heapSort,
    "merge sort": mergeSort,
   # "shell sort": shellSort,
    #"quick sort iteracyjny": quickSortIteracyjny,
    #"quick sort rekurencyjny": quickSortRekurencyjny
}

results = {}

for algorithmName, sortFn in algorithms.items():
    sortResults, seqItemsCount = gen.defaultTest(algorithmName, sortFn, True, 1000, 5000)
    results[algorithmName] = (sortResults, seqItemsCount)

#print(results)

transformedResults = {}

seqTypes = results["heap sort"][0].keys()

for algorithm, data in results.items():
    seqTypes = results[algorithm][0].keys()
    for seqType in seqTypes:
        transformedResults[seqType] = {
            algorithmName: results[algorithmName][0][seqType]
            for algorithmName in results
        }

#print(transformedResults)

sequenceLengthsByAlgorithm = {}

for algorithmName, data in results.items():
    sequenceLengthsByAlgorithm[algorithmName] = data[1]

#print(sequenceLengthsByAlgorithm)

gen.plotGraphsForSeqType(transformedResults, sequenceLengthsByAlgorithm)