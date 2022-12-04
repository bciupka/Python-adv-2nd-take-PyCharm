import time
import functools

def wrapper(func):

    def funcWrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return result
    return funcWrapped

@wrapper
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v



print(get_sequence(19))

# gsw = wrapper(get_sequence)

# print(gsw(19))