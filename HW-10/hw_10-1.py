# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем


def gen_string(file):
    with open(file, 'r') as f:
        auxiliary_lst = []
        for line in f:
            if line not in auxiliary_lst:
                print(line)
                auxiliary_lst.append(line)
                yield line


gen = gen_string('text.txt')

next(gen)
next(gen)
next(gen)

