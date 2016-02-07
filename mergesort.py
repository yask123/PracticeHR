def mergesort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1


alist = [54, 342, 463, 213, 435, 7652, 21, 23, 4, 56]

mergesort(alist)
print alist
