'''
https://www.interviewbit.com/courses/programming/topics/binary-search/problems/sqrt/
'''


def sqrt(n):
    if n == 0:
        return 0

    start = 1
    end = n
    ans = 0

    while start <= end:
        mid = (start + end) / 2

        if n / mid >= mid:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans


a = [74, 90, 85, 58, 69, 77, 90, 85, 18, 36]
a.sort()

print a[-1]
