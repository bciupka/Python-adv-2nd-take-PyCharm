import functools
import time


@functools.lru_cache(100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

def fib2(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.perf_counter()
print(fib2(120))
stop = time.perf_counter()
print(stop-start)



start = time.perf_counter()
print(fib(120))
stop = time.perf_counter()
print(stop-start)



start = time.perf_counter()
result = 0
n1 = 1
n2 = 1
result = 0
for n in range(2, 120):
    result = n1 + n2
    n1 = n2
    n2 = result
print(result)
stop = time.perf_counter()
print(stop-start)


