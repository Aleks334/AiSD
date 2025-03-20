import heapsort, merge_sort, quicksort_iteration, quicksort_recursion, shell_sort

def heap(arr):
    heapsort.kopcowanie(arr)

def merge(arr):
    merge_sort.mergeSort(arr)

def quickIteration(arr):
    quicksort_iteration.quickSortIteracyjny(arr)

def quickRecursion(arr):
    quicksort_recursion.quickSortRekurencyjny(arr)

def shell(arr):
    shell_sort.shellSort(arr)