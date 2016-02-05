open_brackets = '{,[,('

brackets_stack = []

inp = '{{[[(())]]}}'


def get_reversed(bracket):
    if bracket == '{':
        return '}'
    elif bracket == '(':
        return ')'
    elif bracket == '[':
        return ']'


def bracket_tes(inp):
    for each in inp:
        if each in open_brackets:
            brackets_stack.append(each)
            # print brackets_stack

        else:
            popped_bracket = brackets_stack.pop()
            reversed_closing_bracket = get_reversed(popped_bracket)
            if reversed_closing_bracket != each:
                return False

    return True


print bracket_tes(inp)
