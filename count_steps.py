def count(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count(n - 1) + count(n - 2) + count(n - 3)


print count(3)
