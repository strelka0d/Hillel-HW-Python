# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

print('TASK - 1')

import re

def del_words(file):
    checking_file = open(file, 'r')
    lines = checking_file.readlines()
    res_file = open('text_res.txt', 'w')
    for line in lines:
        line = re.sub(r'[.,;:?\n!*-]', '', line)
        print(line)
        line_lst = line.split(' ')
        print(line_lst)
        bad_words = []
        for word in line_lst:
            if 3 <= len(word) <= 5:
                bad_words.append(word)
        print(len(bad_words))
        if len(bad_words) % 2 == 0:
            for word in bad_words:
                if word in bad_words:
                    line_lst.remove(word)
            res_file.write(' '.join(line_lst) + '\n')
        else:
            res_file.write(line + '\n')

    checking_file.close()
    res_file.close()


del_words('text.txt')

# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.

print('Task - 2')


def phone_book():
    book = open("phonebook.txt", "r")
    lines = book.readlines()
    new_book = open("newphonebook.txt", "w")
    for line in lines:
        line_lst = line.split(' ')
        if line_lst[0][0] == 'К' or line_lst[0][0] == 'С':
            new_book.write(line)
    book.close()
    new_book.close()
    return new_book


phone_book()

print('Result is in the file newphonebook.txt')