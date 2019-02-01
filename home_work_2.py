#1)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

#1.1) отсортировать массив из словарей по значению ключа ‘age' 
#1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :
# result = {
#    'Kiev': [
#       {'name': 'Viktor', 'age': 30 },
#       {'name': 'Andrey', 'age': 34}],
#
#    'Dnepr': [ {'name': 'Maksim', 'age': 20 },
#               {'name': 'Artem', 'age': 50}],
#    'Lviv': [ {'name': 'Vladimir', 'age': 32 },
#              {'name': 'Dmitriy', 'age': 21}]
# }
print('task 1:')


def get_age(data):
    return data['age']


data_age = sorted(data, key = get_age)

print(data_age)

data_city = {}

for info in data:
    data_city[info.get('city')] = data_city.get(info.get('city'), [])
    data_city.get(info.get('city'), [])
    data_city[info.get('city')].append(info)
    del info['city']

print(data_city)

# =======================================================
# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

print('task 2:')


def most_frequent(list_var):
    dict_el = {}
    for element in list_var:
          dict_el[element] = int(dict_el.get(element, 0)) + 1
    max_num = max(dict_el.keys())
    return max_num


k = most_frequent(['a', 'a', 'bi', 'bi', 'bi'])

print(k)

# =======================================================
# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

print('task 3:')


def mult_num(num):
    result = 1
    for i in str(num):
        if not int(i):
            continue
        result *= int(i)
    return result


print(mult_num(int(input('please enter number'))))

# =======================================================
# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.

array = input('write an array using space for splitting').split(' ')
n = int(input('write index'))

print('task 4:')


def found_el(array, n):
    if n >= len(array) or n < 0:
        return '-1'
    else:
        return int(array[n]) ** n


print(found_el(array, n))
# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

print('task 5:')

string_input = input('write string for 5 task')


def cheking_string(string_input):
    counter_words = 0
    for el in string_input.split(' '):
        if el.isalpha():
            counter_words += 1
        else:
            counter_words = 0
        if counter_words == 3:
            return True
    return False


print(cheking_string(string_input))