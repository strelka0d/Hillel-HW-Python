# Описать с использованием @contexmanager
# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.

import contextlib
import os

@contextlib.contextmanager
def Folder(path):
    saved_cd = os.getcwd()
    try:
        os.chdir(path)
    except Exception as e:
        print(f'error:{e}')
    finally:
        os.chdir(saved_cd)
