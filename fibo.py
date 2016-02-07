def fib(n):
    a, b = 0, 1
    count = 3

    if n == 1:
        print a
    elif n == 2:
        print b
    else:
        for i in range(n - 2):
            c = a + b
            a, b = b, c
        print c


print fib(20)
