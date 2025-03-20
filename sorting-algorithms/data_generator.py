import random
import time
import matplotlib.pyplot as plt

import os

outputPath = "output"

if not os.path.exists(outputPath):
    os.makedirs(outputPath)


def generateSeqItemsCount(start, stop, count):
    step = (stop - start) // (count - 1)
    return [start + i * step for i in range(count)]

def generateSequences(n, k = 10):
    """For each sequence type, it generates k n-element integer sequences in the interval <1,k*n>"""
    limit = k * n

    sequences = {
        "losowy": [random.sample(range(1, limit + 1), n) for _ in range(k)],
        "rosnący": [list(range(1, n + 1)) for _ in range(k)],
        "malejący": [list(range(n, 0, -1)) for _ in range(k)],
        "A-kształtny": [sorted(random.sample(range(1, limit + 1), n//2)) + sorted(random.sample(range(1, limit + 1), n - n//2), reverse=True) for _ in range(k)],
        "V-kształtny": [sorted(random.sample(range(1, limit + 1), n//2), reverse=True) + sorted(random.sample(range(1, limit + 1), n - n//2)) for _ in range(k)]
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

def plotGraphForAlgorithm(seqSizes, data, algorithmName):
    """ Draws a graph of the dependence of sorting time on data size."""
    plt.figure(figsize=(10, 6))

    for seqType, avgTimes in data.items():
        plt.plot(seqSizes, avgTimes, marker='o', label=seqType)
    
    plt.title(f"Wykres zależności czasu sortowania od wielkości danych dla {algorithmName}")
    plt.xlabel("Liczba elementów w ciągu")
    plt.ylabel("Średni czas sortowania (ms)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{outputPath}/{algorithmName.replace(" ", "-")}")

def defaultTest(algorithmName, sortFn, shouldDrawGraph, minN, maxN):
    sequencesItemsCount = generateSeqItemsCount(minN, maxN, 10)
    sortResults = {}

    # results dict setup
    for seqType in generateSequences(0).keys():
        sortResults[seqType] = []

    for n in sequencesItemsCount:
        sequences = generateSequences(n)
        avgTimes = measureSortTime(sortFn, sequences)

        for seqType in sortResults:
            sortResults[seqType].append(avgTimes[seqType])

    if shouldDrawGraph:
        # print(sortResults)
        plotGraphForAlgorithm(sequencesItemsCount, sortResults, algorithmName)
    
    return (sortResults, sequencesItemsCount)

def plotGraphsForSeqType(transformedResults, sequenceLengthsByAlgorithm):
    for seqType, algorithms_data in transformedResults.items():
        plt.figure(figsize=(10, 6))  
        
        for algorithm, times in algorithms_data.items():
            plt.plot(sequenceLengthsByAlgorithm[algorithm], times, marker='o', label=algorithm)

        plt.title(f"Wydajność algorytmów dla typu ciągu - {seqType}")
        plt.xlabel("Liczba elementów w ciągu")
        plt.ylabel("Średni czas sortowania (ms)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"output/{seqType.replace(' ', '-')}")