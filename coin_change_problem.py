'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of
S = { S1, S2, .. , Sm}  valued coins,
how many ways can we make the change?
https://projecteuler.net/problem=31
'''


def count(list_of_coins, m, change, cache):
    if cache[change][m]:
        return cache[change][m]

    if change == 0:
        return 1

    if change < 0:
        return 0

    if m < 0:
        return 0
    cache[change][m] = count(list_of_coins, m, change - list_of_coins[m], cache) + count(list_of_coins, m - 1, change,
                                                                                         cache)
    return cache[change][m]


cache = [[0 for x in range(8)] for x in range(201)]
print count([1, 2, 5, 10, 20, 50, 100, 200], 7, 200, cache)
