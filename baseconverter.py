def base_converter(digits, base):
    rem_stack = []

    while (digits > 0):
        rem = digits % base
        rem_stack.append(rem)
        digits = digits // base

    for each in reversed(rem_stack):
        print each,


print base_converter(10, 2)
