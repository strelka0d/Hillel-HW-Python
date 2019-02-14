# Описать с использованием @contexmanager
# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.

from contextlib import contextmanager
import os


@contextmanager
def change_folder(path, exc_type, suppress_ex):
    saved_cd = os.getcwd()
    print(f'I\'m in directory{saved_cd}')
    try:
        os.chdir(path)
    except exc_type:
        if suppress_ex is True:
            print(f'Error {exc_type.__name__} is suppresed')
        else:
            raise exc_type
    try:
        yield {}
    except RuntimeError as e:
        print(f'There\'s an error:{e}')
    finally:
        print(f'Now I\'m in directory {os.getcwd()}')


path = "./New_folder"  # folder exist
# path = "./Lessons"  # folder doesn't exist


with change_folder(path,  FileNotFoundError, True) as cf:
    pass

