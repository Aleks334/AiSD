import csv
import random, time, os
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_PATH = "sorting-algorithms/output"

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

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
    """Measures execution time based on sorting function and dict of k sequences for each seq type. Time is calculated in milliseconds."""
    avgTimes = {}
    stdDevs = {}

    for seqType, seqList in sequences.items():
        times = []

        for seq in seqList:
            startTime = time.time()
            sortFn(seq.copy())
            endTime = time.time()

            times.append((endTime - startTime) * 1000) # in ms

        avgTimes[seqType] = np.mean(times)
        stdDevs[seqType] = np.std(times)

    return avgTimes, stdDevs

def plotGraphForAlgorithm(seqSizes, data, algorithmName):
    """Draws a graph of the dependence of sorting time on data size."""
    plt.figure(figsize=(10, 6))

    for seqType, avgTimes in data.items():
        plt.plot(seqSizes, avgTimes, marker='o', label=seqType)
    
    plt.title(f"Wykres zależności czasu sortowania od wielkości danych dla {algorithmName}")
    plt.xlabel("Liczba elementów w ciągu")
    plt.ylabel("Średni czas sortowania (ms)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{OUTPUT_PATH}/{algorithmName.replace(' ', '-')}.png")

def exportResultsToCSV(filename, seqSizes, avgData, stdData):
    """Exports sorting times and standard deviations to a CSV file."""
    csvPath = os.path.join(OUTPUT_PATH, f"{filename}.csv")

    with open(csvPath, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Sequence Type", "Sequence Size", "Average Time (ms)", "Standard Deviation (ms)", "Standard Deviation (%)"])

        for seqType in avgData.keys():
            for i, seqSize in enumerate(seqSizes):
                avgTime = avgData[seqType][i]
                stdDev = stdData[seqType][i]

                avgTimeStr = f"{avgTime:.6f}".replace('.', ',')
                stdDevStr = f"{stdDev:.6f}".replace('.', ',')
                stdDevPercentageStr = round((stdDev / avgTime) * 100, 2)

                writer.writerow([seqType, seqSize, avgTimeStr, stdDevStr, stdDevPercentageStr])


def defaultTest(algorithmName, sortFn, shouldDrawGraph, minN, maxN, shouldGenCsv=True):
    sequencesItemsCount = generateSeqItemsCount(minN, maxN, 10)

    avgSortResults = {seqType: [] for seqType in generateSequences(0).keys()}
    stdDevResults = {seqType: [] for seqType in generateSequences(0).keys()}

    for n in sequencesItemsCount:
        sequences = generateSequences(n)
        avgTimes, stdDevs = measureSortTime(sortFn, sequences)

        for seqType in avgSortResults:
            avgSortResults[seqType].append(avgTimes[seqType])
            stdDevResults[seqType].append(stdDevs[seqType])

    if shouldGenCsv:
        exportResultsToCSV(algorithmName.replace(" ", "-"), sequencesItemsCount, avgSortResults, stdDevResults)

    if shouldDrawGraph:
        plotGraphForAlgorithm(sequencesItemsCount, avgSortResults, algorithmName)
    
    return (avgSortResults, sequencesItemsCount)

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
        plt.savefig(f"{OUTPUT_PATH}/{seqType.replace(' ', '-')}")
