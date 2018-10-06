import time
import threading
from threading import Event


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1


t = threading.Thread(target=countdown, args=(12, ))

t.start()

if t.is_alive():
    print("[(*)] alive")
else:
    print("[(*)] done.")


class CountdownThread(threading.Thread):
    def __init__(self, n, *args, **kwargs):
        super(CountdownThread, self).__init__(*args, **kwargs)
        self.n = 0

    def run(self):
        while self.n > 0:
            print("T-minus", self.n)
            time.sleep(5)

c = CountdownThread(12)
c.start()


def countdowned(n, started_evt):
    started_evt.set()

    while n > 0:
        n -= 1
        time.sleep(10)


started_evt = Event()


print("[(*)] launching countdowned.")

th = threading.Thread(target=countdowned, args=(12, started_evt))

th.start()

started_evt.wait()

print("[(*)] runing")