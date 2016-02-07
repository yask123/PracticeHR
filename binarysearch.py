def binSearch(alist, item):
    found = False
    start = 0
    end = len(alist) - 1

    while start <= end and not found:
        mid = (start + end) / 2
        if alist[mid] == item:
            found = True
            return mid
        else:
            if item < alist[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


print binSearch([1, 2, 3, 4, 5], 2)
