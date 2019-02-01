import random

consonats = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
str_check = input()


def change_letter(str_check):
    result = str_check
    for letter in result:

        if letter in consonats:
            result = result.replace(letter, random.choice(vowels))
    return result


print(change_letter(str_check))
