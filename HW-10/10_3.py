#Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.


def coroutine(func):
    def wrapper(*args, **kwargs):
        crtn = func(*args, **kwargs)
        crtn.send(None)
        return crtn
    return wrapper

def source(function):
    x = 0
    while x < 10:
        try:
            x += 1
            function.send(x)
        except StopIteration:
            print('Coroutine1 is closed')
            break

@coroutine
def coroutine1(corout2):
    while True:
        value = yield
        try:
            print(f'Coroutine1 get {value}')
            corout2.send(value)
        except (GeneratorExit, StopIteration):
            print('Coroutine2 is closed')
            break



@coroutine
def coroutine2():
    while True:
        value = yield
        print(f'Coroutine2 get {value}')


corout2 = coroutine2()
corout1 = coroutine1(corout2)

source(corout1)
corout2.close()
source(corout1)
