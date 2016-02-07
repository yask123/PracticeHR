def quicksort(alist):
    quicksorthelper(alist, 0, len(alist) - 1)


def quicksorthelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quicksorthelper(alist, first, splitpoint - 1)
        quicksorthelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark += 1

        while leftmark <= rightmark and alist[rightmark] >= pivot_value:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            alist[rightmark], alist[leftmark] = alist[leftmark], alist[rightmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

quicksort(alist)
print alist
