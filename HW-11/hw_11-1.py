# Написать функцию которая будет выполнять запросы на https://httpbin.org/ с использованием нескольких потоков

import time
from threading import Thread
import requests


links = ['https://httpbin.org/'] * 10
#links = ['https://google.com', 'https://ukr.net', 'https://www.youtube.com/', 'https://snig.info/']

def main(links):
    tstart = time.time()
    for link in links:
        ts = time.time()
        requests.get(link)
        print(f'I needed {time.time() - ts} sec to do for request to link {link}')
    print(f'I needed {time.time() - tstart} sec to do all requests')




t1 = Thread(target=main, args=((link for link in links), ))
t2 = Thread(target=main, args=((link for link in links), ))
threads = [t1, t2]

threads = [Thread(target=main, args=((link for link in links), ))]


for t in threads:
    t.start()
    t.join()
