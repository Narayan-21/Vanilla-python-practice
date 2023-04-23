import math
import threading
from time import perf_counter

num_intervals = 10_000_000
num_threads = 10000
results = []

def func(x):
    return math.sqrt(1-x*x) # A semi-circle

def riemann_sum(func, delta, a, i_start, i_end):
    area = 0
    for i in range(i_start, i_end):
        x = a + delta*i
        area += func(x)*delta
    results.append(area)

def split(num_intervals, n):
    k, m = divmod(num_intervals, n)
    return [(i*k + min(i,m), (i+1) * k + min(i+1, m)) for i in range(n)]


if __name__ == '__main__':
    start = perf_counter()
    a = -1
    b = 1
    delta = (b-a) / num_intervals

    # Split the intervals into num_threads
    chunks = split(num_intervals, num_threads)

    # Create the threads
    threads = []
    for i_start, i_end in chunks:
        threads.append(
            threading.Thread(target=riemann_sum, args=(func, delta, a, i_start, i_end))
        )

    # Start and join the threads
    for thread in threads:
        thread.start()
        thread.join()

    area = sum(results)
    end = perf_counter()
    print(f"Area: {area:.10f}, pi/2 = {math.pi/2:.10f}")
    print(f"Elapsed: {end - start:.4f} seconds")