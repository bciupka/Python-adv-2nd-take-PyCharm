import itertools
import math


notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for i in itertools.permutations(notes, 4):
    print(i)

amount = math.factorial(len(notes))/math.factorial(len(notes)-4)
print(int(amount))

results = []
for x in itertools.product(notes, repeat=4):
    print(x)
    results.append(x)

amount = pow(len(notes), 4)
print(int(amount))
print(len(results))

# results = []
# for x in itertools.combinations_with_replacement(notes, 4):
#     print(x)
#     results.append(x)
#
# print(len(results))

