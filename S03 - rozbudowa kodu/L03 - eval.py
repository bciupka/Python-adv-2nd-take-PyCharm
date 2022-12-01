import math

argument_list = []

for i in range(101):
    argument_list.append(i/10)

equation = input()

for i in argument_list:     #for x in ...
    x = i
    print(eval(equation))

