def longestConsecutive(A):
    A = sorted(A)
    prev = A[0]
    count = 0
    max_count = 0

    for each in range(1, len(A)):
        current = A[each]
        if current == prev + 1:
            count += 1
            if count > max_count:
                max_count = count
        elif current == prev:
            pass
        else:
            count = 0
        prev = current

    return max_count + 1


alist = (1, 1, 2, 2, 3, 3, 4, 4, 5, 5)
print longestConsecutive(alist)
