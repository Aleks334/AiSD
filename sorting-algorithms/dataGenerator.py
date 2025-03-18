import random
import time

def generateSeqItemsCount(start, stop, count):
    step = (stop - start) // (count - 1)
    return [start + i * step for i in range(count)]

def generateSequences(n, k = 10):
    """For each sequence type, it generates k n-element integer sequences in the interval <1,k*n>"""
    limit = k * n

    sequences = {
        "random": [random.sample(range(1, limit + 1), n) for _ in range(k)],
        "ascending": [list(range(1, n + 1)) for _ in range(k)],
        "descending": [list(range(n, 0, -1)) for _ in range(k)],
        "A-shaped": [sorted(random.sample(range(1, limit + 1), n//2)) + sorted(random.sample(range(1, limit + 1), n - n//2), reverse=True) for _ in range(k)],
        "V-shaped": [sorted(random.sample(range(1, limit + 1), n//2), reverse=True) + sorted(random.sample(range(1, limit + 1), n - n//2)) for _ in range(k)]
    }
    return sequences

def measureSortTime(sortFn, sequences):
    """Measures execution time based on sorting function and dict of k sequences for each seq type. Time is calculated in miliseconds."""
    totalTime = 0
    avgTimes = {}

    for seqType, seqList in sequences.items():
        for seq in seqList:
            startTime = time.time()
            sortFn(seq.copy())
            endTime = time.time()

            totalTime += (endTime - startTime) * 1000 # in ms

        avgTimes[seqType] = totalTime / len(seqList)

    return avgTimes

def exampleTest():
    sequencesItemsCount = generateSeqItemsCount(10_000, 50_000, 10)
    sortResults = {}

    # results dict setup
    for seqType in generateSequences(0).keys():
        sortResults[seqType] = []

    for n in sequencesItemsCount:
        sequences = generateSequences(n)
        avgTimes = measureSortTime(sorted, sequences) # built-in python sort function

        for seqType in sortResults:
            sortResults[seqType].append(avgTimes[seqType])

    print(sortResults)