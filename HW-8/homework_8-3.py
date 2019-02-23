# Создать менеджер контекста который будет подсчитывать время выполняния блока инсрукций

import time


class Timer(object):

    def __init__(self):
        self._start_time = None

    def __enter__(self):
        self._start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self._start_time
        print(duration)


with Timer():
    print(2**3)
