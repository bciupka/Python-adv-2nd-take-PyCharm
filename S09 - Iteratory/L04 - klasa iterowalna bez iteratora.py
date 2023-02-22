class CombinationsNext:
    def __init__(self, products, promos, clients):
        self.products = products
        self.promos = promos
        self.clients = clients
        self.curr_product = 0
        self.curr_promo = 0
        self.curr_client = 0

    def __next__(self):
        if self.curr_client >= len(self.clients):
            self.curr_client = 0
            self.curr_promo += 1

        if self.curr_promo >= len(self.promos):
            self.curr_promo = 0
            self.curr_product += 1

        if self.curr_product >= len(self.products):
            self.curr_product = 0
            raise StopIteration()

        item = [self.products[self.curr_product], self.promos[self.curr_promo], self.clients[self.curr_client]]
        self.curr_client += 1
        return item


class Combinations:

    def __init__(self, products, promos, clients):
        self.products = products
        self.promos = promos
        self.clients = clients
        self.iter = CombinationsNext(self.products, self.promos, self.clients)

    def __iter__(self):
        return self.iter


products = ["Product {}".format(i) for i in range(1, 500)]

promotions = ["Promotion {}".format(i) for i in range(1, 50)]

customers = ['Customer {}'.format(i) for i in range(1, 500)]

combinations = Combinations(products, promotions, customers)

it = iter(combinations)

print(next(it))
print(next(it))
print(next(it))


for i in combinations:
    pass
