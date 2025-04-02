import random

def generateSeqItemsCount(start, stop, count):
    step = (stop - start) // (count - 1)
    return [start + i * step for i in range(count)]


def generateSequences(n, k = 10):
    """For each sequence type, it generates k n-element integer sequences in the interval <1,k*n>"""
    limit = k * n

    sequences = {
        "random": [random.sample(range(1, limit + 1), n) for _ in range(k)],
        "ascending": [list(range(1, n + 1)) for _ in range(k)],
    }
    return sequences