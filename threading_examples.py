import threading
import random
from time import sleep
import queue

num_iter = 100
counter = 0
sum_ = 0
c_lock = threading.Lock() #compute-lock
print_queue = queue.Queue()

def fuzz():
    sleep(random.random()/10)

def print_queue_watcher():
    while True:
        item = print_queue.get()
        fuzz()
        print(item)
        fuzz()
        print_queue.task_done()
        fuzz()


def do_work():
    global counter
    global sum_

    fuzz()
    with c_lock:
        counter += 1
        next_sum = sum_ + counter
        print_queue.put(f'{sum_} + {counter} = {next_sum}')
        print_queue.put('-'*20)
        sum_ = next_sum

    fuzz()


if __name__ == '__main__':
    threads = []

    threading.Thread(target=print_queue_watcher, daemon=True).start()
    for i in range(num_iter):
        threads.append(threading.Thread(target=do_work))

    for thread in threads:
        thread.start()
        fuzz()

    for thread in threads:
        thread.join()

    print_queue.join()
    print(f'Done: solution = {sum_}')