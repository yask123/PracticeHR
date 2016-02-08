inp = 'aaaabbbrr'
alist = []

for each in inp:
    alist.append(each)

prev = alist[0]
count = 1
first_char_index = 0
for i in range(1, len(alist)):
    current = alist[i]

    if current == prev:
        alist[i] = ''
        count += 1

    else:
        alist[first_char_index] = prev + str(count)
        count = 1
        prev = current
        first_char_index = i
alist[first_char_index] = prev + str(count)

for each in alist:
    if each != '':
        print each,
