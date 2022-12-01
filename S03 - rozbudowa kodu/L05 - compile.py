import math
import time


formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

results_list = []

start = time.time()

for x in argument_list:
    results_list.append(eval(formulas_list[0]))

print(min(results_list))
print(max(results_list))

stop = time.time()

print(stop - start)

results_list = []

start = time.time()
source = compile(formulas_list[0], "xd", "eval")
for x in argument_list:
    results_list.append(eval(source))

print(min(results_list))
print(max(results_list))

stop = time.time()

print(stop - start)

results_list = []

start = time.time()

for x in argument_list:
    results_list.append(eval(formulas_list[1]))

print(min(results_list))
print(max(results_list))

stop = time.time()

print(stop - start)

results_list = []

start = time.time()
source = compile(formulas_list[1], "xd", "eval")
for x in argument_list:
    results_list.append(eval(source))

print(min(results_list))
print(max(results_list))

stop = time.time()

print(stop - start)