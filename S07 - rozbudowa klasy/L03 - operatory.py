class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __str__(self):
        return f"{self.name} of kind {self.kind} with {self.additives}"

    def __iadd__(self, other):
        if type(other) is list:
            newAdditives = self.additives.copy()
            newAdditives.extend(other)
            return Cake(self.name, self.kind, self.taste, newAdditives, self.filling)
        elif type(other) is str:
            newAdditives = self.additives.copy()
            newAdditives.append(other)
            return Cake(self.name, self.kind, self.taste, newAdditives, self.filling)
        else:
            raise Exception("Nie ten format")


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
print(cake01)

cake01 += ["white chocolate", "biscuit"]
print(cake01)

cake01 += "jelly"
print(cake01)

cake01 += 5
