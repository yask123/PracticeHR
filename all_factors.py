import math


def allFactors(self, A):
    results = []
    for i in range(2, int(math.sqrt(A)) + 1):
        if A % i == 0:
            results.append(i, A / i)
    return results
