# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу

import os
import json
from pprint import pprint


class Jsonfile(object):

    def __init__(self, file1, file2):
        self._file1 = file1
        self._file2 = file2

    def read(self):
        with open(self._file1) as input_file:
            file = json.load(input_file)
        pprint(file)

    def write(self, data):
        with open(self._file2, 'w') as input_file:
            return json.dump(data, input_file, indent=2)

    def merge(self):
        with open(self._file1, 'r') as file1:
            json_data1 = json.load(file1)
        with open(self._file2, 'r') as file2:
            json_data2 = json.load(file2)
        inside_file =[]
        inside_file.append(json_data1)
        inside_file.append(json_data2)
        with open('final_file.json', 'w') as final_file:
            json.dump(inside_file, final_file, indent=2)
        return final_file

    @staticmethod
    def relative_path(file):
        return os.path.relpath(file, '/home')

    @staticmethod
    def abs_path(file):
        return os.path.abspath(file)

file1 = 'test.json'
file2 = 'test2.json'
json_file = Jsonfile(file1, file2)
json_file.read()
data = {"user2": []}
data["user2"].append({"firstName": "Adam",
  "lastName": "Black",
  "age": 30,
  "address": {
    "streetAddress": "21 5nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3101"
  }
})

json_file.write(data)
json_file.merge()
print(f"The absolute path of {file1} is {json_file.abs_path(file1)}")
print(f"The relative path of {file1} is {json_file.relative_path(file1)}")

