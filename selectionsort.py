def select_sort(alist):
    for i in range(len(alist)):
        max_num = alist[0]
        for j in range(len(alist) - i):
            if alist[j] >= max_num:
                max_num = alist[j]
                max_num_index = j
        alist[max_num_index], alist[len(alist) - i - 1] = alist[len(alist) - i - 1], alist[max_num_index]
    return alist


print select_sort([32, 21, 345, 123, 435231, 324123, 213])
