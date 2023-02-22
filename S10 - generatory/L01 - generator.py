def Combinations(products, promos, clients):
    for i in products:
        for j in promos:
            for k in clients:
                yield [k, j, i]


products = ["Product {}".format(i) for i in range(1, 5)]

promotions = ["Promotion {}".format(i) for i in range(1, 5)]

customers = ['Customer {}'.format(i) for i in range(1, 5)]

combinations = Combinations(products, promotions, customers)

print(next(combinations))
print(next(combinations))
print(next(combinations))

for i in combinations:
    print(i)
