def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

number = 3

transformations = [double, square, div2, negative]

tmp_return_value = number

for i in transformations:
    tmp_return_value = i(tmp_return_value)
    print((tmp_return_value))

transformations2 = [square, square, div2, double]

tmp_return_value = number

for i in transformations2:
    tmp_return_value = i(tmp_return_value)
    print((tmp_return_value))
