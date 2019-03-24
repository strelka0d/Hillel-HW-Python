# У вас есть пулл адрессов (можно использовать https://httpbin.org/ ).
# Создать 2-3 функции которые будут делать реквесты к этому адресу.
# Ваши реквесты должны быть асинхронны с использованием asyncio

import asyncio
import requests
import time

urls1 = ['https://httpbin.org/'] * 5
urls2 = ['https://stackoverflow.com/'] * 5


async def request_url1(url1):
    ts = time.time()
    requests.get(url1)
    print(f'I\'m doing request to {url1} for {time.time() - ts} sec.')
    await asyncio.sleep(0)


async def request_url2(url2):
    ts = time.time()
    requests.get(url2)
    print(f'I\'m doing request to {url2} for {time.time() - ts} sec.')
    await asyncio.sleep(0)


ioloop = asyncio.get_event_loop()
tasks = []
for url1 in urls1:
    tasks.append(ioloop.create_task(request_url1(url1)))
for url2 in urls2:
    tasks.append(ioloop.create_task(request_url2(url2)))
st = time.time()
waite_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(waite_tasks)

print(f'For all requests I need {time.time() - st} sec')

ioloop.close()
