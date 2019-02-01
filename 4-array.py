array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]


def non_double_array(args):
    array_non_doubled = []
    for i in array:
        if i not in array_non_doubled:
            array_non_doubled.append(i)
    return array_non_doubled


def max3_elements(args):
    lst_sort = sorted(array)
    return lst_sort[-3:]


def min_index(args):
    return array.index(min(array))


def reverse_array(args):
    return array[::-1]


print('1.', non_double_array(array))
print('2.',  max3_elements(array))
print('3.', min_index(array))
print('4.', reverse_array(array))
