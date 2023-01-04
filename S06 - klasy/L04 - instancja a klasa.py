class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def showInfo(self):
        print("{}\nKind:\t\t{}\nTaste:\t\t{}".format(self.name.upper(), self.kind, self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for i in self.additives:
                print("\t\t\t{}".format(i))
        if len(self.filling) > 0:
            print("Filling:\t{}".format(self.filling))
        print(30 * "-", "\n")

    def setFilling(self, newFilling):
        self.filling = newFilling

    def addAdditives(self, newAdditives):
        self.additives.extend(newAdditives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

# cake04.showInfo()

for i in Cake.bakery_offer:
    i.showInfo()

print(isinstance(cake01, Cake))
print(type(cake01))

print(vars(cake01))
print(dir(Cake))