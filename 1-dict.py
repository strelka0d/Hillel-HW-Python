lst_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def generate_list(args):
    dict_key = {}
    for i in lst_keys:
        dict_key[i] = i * i
    return dict_key


result = generate_list(lst_keys)

print(result)
