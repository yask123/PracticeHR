def anagram(s1, s2):
    count_s1_char = {}
    count_s2_char = {}

    for each in s1:
        try:
            count_s1_char[each] += 1
        except:
            count_s1_char[each] = 1

    for each in s2:
        try:
            count_s2_char[each] += 1
        except:
            count_s2_char[each] = 1

    for each_key in count_s1_char:
        try:
            if count_s1_char[each_key] != count_s2_char[each_key]:
                return False
        except:
            return False

    for each_key in count_s2_char:
        try:
            if count_s1_char[each_key] != count_s2_char[each_key]:
                return False
        except:
            return False

    return True


print anagram('abcd', 'dcba')
