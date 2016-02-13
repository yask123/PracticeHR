def findOccurance( A, k, first):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) / 2

        if A[mid] == k:
            if first:
                high = mid - 1
                result = mid
            else:
                low = mid + 1
                result = mid
        elif A[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return result

print findOccurance([1,2,2,2,2,3,4,4,5],2,False)
