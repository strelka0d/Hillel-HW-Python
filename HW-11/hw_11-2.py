#Созадть очередь из задач. Создать воркеров которые будут делать выборки из очереди и  выполнять эти задачи.
# Количество воркеров - опциональный аргумент. Количество задач - опциональный аргумент.  1 воркер == 1 тред

import queue
import time
from threading import Thread


def work(worker):
    print(f'Worker {worker} has started to work')
    while True:
        task = q.get()
        if task == None:
            break
        do_task()
        print(f'Worker {worker} finished its work')
        q.task_done()


def do_task():
    time.sleep(2)


q = queue.Queue()

for worker in range(7):
    t = Thread(target=work, args=(worker,))
    t.setDaemon(True)
    t.start()

for i in range(7):
    q.put(i)

q.join()

