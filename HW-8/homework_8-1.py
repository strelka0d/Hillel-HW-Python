# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.

import os

class Folder(object):
    def __init__(self, path):
        self._path = path
        self._saved_curdir = None

    def __enter__(self):
        self._saved_curdir = os.getcwd()
        os.chdir(self._path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            os.chdir(self._saved_curdir)
        except Exception:
            raise Exception

print(f'Current directory = {os.getcwd()}')

class Suppress(Exception):
    def