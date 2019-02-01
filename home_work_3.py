# Задача-1
#
# Дан произвольный текст. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в тексте.
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".

print('task_1')
text = "How are you? Eh, ok. Low or Lower? Ohhh."


def upper_letters(text):
    result = ''
    lst_upper = []
    for letter in text:
        if letter.isupper():
            lst_upper.append(letter)
    return ''.join(lst_upper)


print(upper_letters(text))


# Задача-2
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.

print('task_2')

input_array = input('write an array of numbers using space for splitting').split(' ')

def multiply_elements(input_array):
    i = 0
    input_array[0] = input_array[i]
    sum_el = int(input_array[i])
    for el in input_array:
        if input_array.index(el, i) % 2 == 0:
            sum_el += int(el)
            i += 1
    return sum_el * int(input_array[-1])


print(multiply_elements(input_array))


# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все

print('task_3')


def first_word(string):
    string = string.replace('.', ' ')
    string = string.replace(',',' ')
    string = string.lstrip()
    string = string.split(' ')
    word = str(string[0])
    return str(word)


string = input('print your string')

print(first_word(string))

# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.

print('task 4')

string = input('please input string')


def new_string(string):
    if len(string) == 2 or len(string) == 3:
        return string[::-1]
    else:
        return string[-1] + string[1:-1] + string[0]


print(new_string(string))

# Задача-5
# Дан тапл(tuple), необходимо его конвертнуть в стринг.
# Например:
# ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's') == 'exercises'git fetch


print('task 5')


income_tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')


def convert(income_tuple):
    outcome_string =''.join(income_tuple)
    return outcome_string


print(convert(income_tuple))
