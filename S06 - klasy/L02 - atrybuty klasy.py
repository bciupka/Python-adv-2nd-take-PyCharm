class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling


cheesecake = Cake("cheesecake", "sweet", "cheezy", "chocolate", "none")
gingerbread = Cake("gingerbread", "christmas", "spicy", "frosting", "none")

bakeryOffer = [cheesecake, gingerbread]

for i in bakeryOffer:
    print(i.name, i.kind, i.taste, i.additives, i.filling)
