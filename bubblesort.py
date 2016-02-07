def bubblesort(alist):
    for i in range(len(alist)):
        for j in range(len(alist) - i - 1):
            if alist[j + 1] < alist[j]:
                alist[j + 1], alist[j] = alist[j], alist[j + 1]
    return alist


print bubblesort([54, 23, 1, 445, 45, 231324, 34])
