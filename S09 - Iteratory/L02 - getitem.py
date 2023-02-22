class Combinations:

    def __init__(self, products, promos, clients):
        self.products = products
        self.promos = promos
        self.clients = clients
    #     self.curr_product = 0
    #     self.curr_promo = 0
    #     self.curr_client = 0
    #
    # def __next__(self):
    #     if self.curr_client >= len(self.clients):
    #         self.curr_client = 0
    #         self.curr_promo += 1
    #
    #     if self.curr_promo >= len(self.promos):
    #         self.curr_promo = 0
    #         self.curr_product += 1
    #
    #     if self.curr_product >= len(self.products):
    #         self.curr_product = 0
    #         raise StopIteration()
    #
    #     item = [self.products[self.curr_product], self.promos[self.curr_promo], self.clients[self.curr_client]]
    #     self.curr_client += 1
    #     return item
    #
    # def __iter__(self):
    #     return self

    def __getitem__(self, i):
        if i >= (len(self.products) * len(self.promos) * (len(self.clients))):
            raise StopIteration()
        else:
            c = i // (len(self.clients) * len(self.promos))
            i = i % (len(self.clients) * len(self.promos))
            b = i // (len(self.clients))
            i = i % (len(self.clients))
            a = i
        return [self.clients[a], self.promos[b], self.products[c]]


products = ["Product {}".format(i) for i in range(1, 5)]

promotions = ["Promotion {}".format(i) for i in range(1, 5)]

customers = ['Customer {}'.format(i) for i in range(1, 5)]

combinations = Combinations(products, promotions, customers)

print(combinations[0])

it = iter(combinations)

print((next(it)))
print((next(it)))
print((next(it)))

