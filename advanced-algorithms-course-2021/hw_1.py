a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]
print(a)


def unique_numbers(a):
    b = []
    for a_index, a_element in enumerate(a):
        not_found = True
        for b_element in a[a_index + 1: len(a)]:
            if a_element == b_element:
                not_found = False
        if not_found:
            b.append(a_element)
    return b


def member(element, a):
    if len(a) == 0:
        return False
    if element == a[0]:
        return True
    return member(element, a[1: len(a)])


def unique_numbers_recursive(a):
    if len(a) == 1:
        return a
    if not member(a[0], a[1: len(a)]):
        return [a[0]] + unique_numbers_recursive(a[1: len(a)])
    return unique_numbers_recursive(a[1: len(a)])


print(unique_numbers(a))
print(unique_numbers_recursive(a))