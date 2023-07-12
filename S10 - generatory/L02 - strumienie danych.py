import random


def random_to_sum(amount, val):
    trials = 0
    numbers = list(range(amount))
    while True:
        trials += 1
        for i in range(amount):
            numbers[i] = random.randint(1, val+1)
        if sum(numbers) == val:
            yield trials, numbers
            trials = 0


for i in range(10):
    print(next(random_to_sum(3, 100)))
