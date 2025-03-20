# draws all graphs:
# each sorting algorithm with all sequence types
# each sequence type with all sorting algorithms

import data_generator as gen, sorts as sort

heapSortResults, heapSortSeqItemsCount = gen.defaultTest("heap sort", sort.heap, True, 5000, 25_000)
mergeSortResults, mergeSortSeqItemsCount = gen.defaultTest("merge sort", sort.merge, True, 5000, 25_000)
quickSortItResults, quickSortItSeqItemsCount = gen.defaultTest("quick sort iteracyjny", sort.quickIteration, True, 1000, 5000)
quickSortRecResults, quickSortRecSeqItemsCount = gen.defaultTest("quick sort rekurencyjny", sort.quickRecursion, True, 1000, 5000)
shellSortResults, shellSortSeqItemsCount  = gen.defaultTest("shell sort", sort.shell, True, 5000, 25_000)

print(heapSortResults, heapSortSeqItemsCount)
print(mergeSortResults, mergeSortSeqItemsCount)
print(quickSortItResults, quickSortItSeqItemsCount)
print(quickSortRecResults, quickSortRecSeqItemsCount)
print(shellSortResults, shellSortSeqItemsCount)
