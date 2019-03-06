# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```


def coroutine(func):
    def wrapper(*args, **kwargs):
        crtn = func(*args, **kwargs)
        crtn.send(None)
        return crtn
    return wrapper


@coroutine
def grep(pattern, func):
    while True:
        line = yield
        if pattern in line:
            print(func)
            func.send(pattern)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


@coroutine
def dispenser(greps):

    while True:
        x = yield
        for i in greps:
            i.send(x)


def follow(file,disp):
    while True:
        line = file.readline()
        if not line:
            break
        disp.send(line)


# ```
#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#
# ```
f_open = open('log.txt')  # подключаемся к файлу
greps = [
           grep('python', printer()),  # отслеживаем
           grep('is', printer()),     # заданные
           grep('great', printer()),  # сигнатуры
       ]
disp = dispenser(greps)

follow(f_open, disp)
