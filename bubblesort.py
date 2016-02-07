def bubblesort(alist):
    '''
    :param alist: a list
    :return: sorted list
    '''
    for i in range(len(alist)):
        exchanges = False
        for j in range(len(alist) - i - 1):
            if alist[j + 1] < alist[j]:
                exchanges = True
                alist[j + 1], alist[j] = alist[j], alist[j + 1]
        if not exchanges:
            break
    return alist


print bubblesort([1, 2, 3, 4, 5, 6, 8])
