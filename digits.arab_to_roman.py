# Написать функцию которая принимает целое число и преобразует его в римскую систему счета


class Convertion(object):

    def __init__(self, number):
        self._number = number
        self._result = ''

    def arab_to_roman(self):
        ROMANS = (('M', 1000),
                  ('CM', 900),
                  ('D', 500),
                  ('CD', 400),
                  ('C', 100),
                  ('XC', 90),
                  ('L', 50),
                  ('XL', 40),
                  ('X', 10),
                  ('IX', 9),
                  ('V', 5),
                  ('IV', 4),
                  ('I', 1))
        numb = self._number
        for i in ROMANS:
            roman, arab = i
            self._result += self._number // arab * roman
            self._number %= arab
        return f'Number {numb} in arabic is {self._result} in Roman'


number1 = Convertion(33)
number2 = Convertion(1001)
number3 = Convertion(499)
number4 = Convertion(999)

print(number1.arab_to_roman())
print(number2.arab_to_roman())
print(number3.arab_to_roman())
print(number4.arab_to_roman())
