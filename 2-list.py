def generate_list():
    lst = []
    for i in range(101):
        if i % 2 == 0:
            lst.append(i)
    return lst


result = generate_list()

print(result)
