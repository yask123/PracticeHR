'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of
S = { S1, S2, .. , Sm}  valued coins,
how many ways can we make the change?
'''


def count(list_of_coins, m, change):
    if change == 0:
        return 1

    if change < 0:
        return 0

    if m < 0:
        return 0
    print change
    return count(list_of_coins, m - 1, change - list_of_coins[m]) + count(list_of_coins, m - 1, change)


print count([1, 2, 3], 2, 4)
