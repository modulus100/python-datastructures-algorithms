def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    middle_index = (start_index + end_index) // 2

    if array[middle_index] == target:
        return middle_index
    if array[middle_index] > target:
        return binary_search_recursive_soln(array, target, start_index, middle_index - 1)
    else:
        return binary_search_recursive_soln(array, target, start_index + 1, end_index)


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)
