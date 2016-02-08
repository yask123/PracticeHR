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
        print prev, count,
        print 'first char index ', first_char_index
        alist[first_char_index] = prev + str(count)
        count = 1
        prev = current
        first_char_index = i
alist[first_char_index] = prev + str(count)
print ''

for each in alist:
    if each != '':
        print each,
