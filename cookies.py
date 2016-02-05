k = 47245
a = '3554 2227 8866 9890 212 8669 2423 7651 3878 3379 1419 6134 5767 859 2848 9309 1449 8408 8041 3367 6676 6382 4136 4871'
cookies = [int(e) for e in a.split()]


def all_greater_than_k(cookies, k):
    for each in cookies:
        if each < k:
            return False

    return True


def calc(cookies):
    steps = 0
    while len(cookies) > 1:
        cookies.sort()
        if (all_greater_than_k(cookies, k)):
            return steps
        # print cookies
        first = cookies.pop(0)
        second = cookies.pop(0)
        cookies.insert(0, first * 1 + second * 2)
        steps += 1
    if len(cookies):
        if cookies[0] >= k:
            return steps
    else:
        return -1


print calc(cookies)
