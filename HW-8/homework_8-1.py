# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.

import os

class Folder(object):

    def __init__(self, path, exc_type, suppress_ex):
        self._path = path
        self.suppress_ex = suppress_ex
        self.exc_type = exc_type
        self._saved_curdir = None

    def __enter__(self):
        if self.suppress_ex is not None:
            self._saved_curdir = os.getcwd()
            os.chdir(self._path)
        else:
            raise self.exc_type

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self._saved_curdir)
        # return True


print(f'I\'m in directory {os.getcwd()}')


class Suppress(Exception):

    def __init__(self, suppress_ex):
        self.suppress_ex = suppress_ex

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        a = exc_type is not None and isinstance(exc_type, self.suppress_ex)
        return a


try:
    folder = "./Lessons"  # folder doesn't exist
    # folder = "./New_folder"  # folder exist
    cd = Folder(folder, exc_type=FileNotFoundError, suppress_ex=True)
    with cd:
        print(f'Now I\'m in directory {os.getcwd()}')
except cd.exc_type as e:
    if cd.suppress_ex is True:
        Suppress(e)
        print(f'Exception {type(e).__name__} is suppressed')
        print(f'I\'m still in {os.getcwd()}')
    else:
        raise cd.exc_type
