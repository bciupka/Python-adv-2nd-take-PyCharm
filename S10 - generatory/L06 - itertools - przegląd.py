import itertools
import time


def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False


candidates = [i for i in range(1, 101)]
filtered = []

for i in itertools.filterfalse(lambda x: x != sum(get_factors(x)), candidates):
    filtered.append(i)

for i in filtered:
    print(i, get_factors(i))

start = time.perf_counter()
primes = list(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
print(primes[:10])
stop = time.perf_counter()
print(stop-start)

start = time.perf_counter()
primes2 = itertools.islice(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)), 10)
print(list(primes2))
stop = time.perf_counter()
print(stop-start)
