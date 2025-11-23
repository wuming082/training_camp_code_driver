import requests
import threading
import queue
from queue import Queue


def text():
    url = 'https://eci-2ze16y1445hrnexjpdy5.cloudeci1.ichunqiu.com:80/js/'
    strs = 'abcmlyx'
    num = '0123456789'
    for i in strs:
        for j in strs:
            for h in num:
                for l in num:
                    for n in num:
                        new_url = url + i + j + 'ctf' + h + l + n + '.js'
                        q.put(new_url)


def requ():
    while not q.empty():
        u = q.get(True, 1)
        try:
            r = requests.get(u).text
            if '404' not in r:
                print(r)
            q.task_done()
        except:
            q.put(u)


if __name__ == '__main__':
    q = Queue()
    text()
    for each in range(300):
        t = threading.Thread(target=requ)
        t.daemon = True
        t.start()

    q.join()