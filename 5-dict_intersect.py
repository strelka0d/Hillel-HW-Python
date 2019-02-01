dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}


def common_keys(*args):
    result = []
    for key_1 in [dict_one.keys()]:
        if key_1 in [dict_two.keys()]:
            result = result.append(key_1)
    if result == []:
        return 'There is no common keys'
    else:
        return result


print(common_keys(dict_one, dict_two))

